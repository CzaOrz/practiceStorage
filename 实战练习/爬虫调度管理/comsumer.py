# -*- coding: utf-8 -*-
import json
import time
import socket
import logging
import threading
import subprocess

from utils.node import decode_node_task, encode_node_task, email, \
    timekiller, kill_pid
from concurrent.futures import ProcessPoolExecutor
from minitools import init_logging_format
from minitools.db.redisdb import get_redis_client
from minitools.db.mongodb import get_mongodb_client
from minitools.db.amqp.rabbitmq import RestartRabbitMQ

try:
    from local_setting import FlaskConfig, ConsumerConfig, RabbitMQConfig
except:
    from setting import FlaskConfig, ConsumerConfig, RabbitMQConfig

init_logging_format()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def save_task(task=None):
    if task:
        content = ""
        try:
            max_line = ConsumerConfig.log_max_line
            max_rows = ConsumerConfig.log_max_rows
            with open(task["log_path"], "r") as f:
                while max_line:
                    line = f.readline(max_rows)
                    if line:
                        content += line
                        max_line -= 1
                    else:
                        break
        except Exception as e:
            content += "log read error!\n\n"
            content += e.__repr__()
        client = get_mongodb_client()
        coll = client[ConsumerConfig.mongodb_dbs_task][ConsumerConfig.mongodb_col_task]
        task.setdefault("log_content", content)
        task.setdefault("end_time", timekiller.get_now().strftime("%Y-%m-%d %H:%M:%S"))
        coll.insert_one(task)
        client.close()


def worker(data, value=None):
    try:
        json_data = json.loads(data)
        task_name = json_data.get("task_name")
        if not task_name:
            raise Exception(f"there is not task {task_name}")
        logger.info(f"get task {task_name}")
        redis_client = get_redis_client()
        task = decode_node_task(task_name)
        if task:
            task = task()
            process = subprocess.Popen(task.command, shell=True)
            key, value = encode_node_task(task, process.pid)
            dumps_value = json.dumps(value, ensure_ascii=False)
            value.setdefault("log_path", task.log_file)
            redis_client.hset(ConsumerConfig.redis_node_pool_tasks, key, dumps_value)
            process.wait()  # run task with safe, even task is being killed.
            redis_client.hdel(ConsumerConfig.redis_node_pool_tasks, key)
            logger.info(f"{task_name} task done...")
    except Exception as e:
        logger.warning("task abnormal...")
        email.send("task abnormal", e)
    save_task(value)
    return True


def run():
    rabbitmq = RestartRabbitMQ(queue=RabbitMQConfig.rabbitmq_queue,
                               conn_auth=RabbitMQConfig.rabbitmq_auth,
                               conn_params=RabbitMQConfig.rabbitmq_conn_params,
                               exchange_params=RabbitMQConfig.rabbitmq_exchange_params)
    rabbitmq.start_consuming(worker)


class ConsumerProcess:

    @classmethod
    def run(cls):
        with ProcessPoolExecutor(1) as executor:
            executor.submit(run)
            logger.info("process start...")


if __name__ == '__main__':
    def scheduler_socket():
        while True:
            try:
                sch_node = socket.socket()
                sch_node.connect((FlaskConfig.host, FlaskConfig.port + 1))
                sch_node.send(ConsumerConfig.node_id.encode())
            except:
                time.sleep(10)
                continue
            while True:
                try:
                    pid_node = sch_node.recv(1024).decode()
                    pid, node = pid_node.split("_", 1)
                    print(f"kill {kill_pid(pid)} success")
                    get_redis_client().hdel(ConsumerConfig.redis_node_pool_tasks, node)
                except:
                    break
            sch_node.close()


    thread = threading.Thread(target=scheduler_socket)
    thread.setDaemon(True)
    thread.start()
    ConsumerProcess.run()
