import json
import time
import socket
import logging
import threading
import subprocess
from concurrent.futures import ProcessPoolExecutor
from minitools.db.amqp.rabbitmq import get_rabbitmq
from minitools.db.redisdb import get_redis_client
from minitools.db.mongodb import get_mongodb_client
from utils.node import decode_node_task, encode_node_task, email, timekiller

logger = logging.getLogger(__name__)


def save_task(task=None):
    if task:
        content = ""
        try:
            max_line = 300
            max_rows = 1024
            with open(task["log_path"], "r", encoding="utf-8") as f:
                while max_line:
                    line = f.readline(max_rows)
                    if line:
                        content += line
                        max_line -= 1
                    else:
                        break
        except:
            pass
        client = get_mongodb_client()
        coll = client["scheduler"]["done"]
        task.setdefault("log_content", content or "log read error!")
        task.setdefault("end_time", timekiller.get_now().strftime("%Y-%m-%d %H:%M:%S"))
        coll.insert_one(task)
        client.close()


def worker(data, value=None):
    try:
        json_data = json.loads(data)
        task_name = json_data.get("task_name")
        if not task_name:
            raise Exception(f"there is not task {task_name}")
        redis_client = get_redis_client()
        task = decode_node_task(task_name)
        if task:
            task = task()
            process = subprocess.Popen(task.command, shell=True)
            key, value = encode_node_task(task, process.pid)
            dumps_value = json.dumps(value, ensure_ascii=False)
            value.setdefault("log_path", task.log_file)
            redis_client.hset("spider:scheduler:node:pool:tasks", key, dumps_value)
            process.wait()  # run task with safe, even task is being killed.
            redis_client.hdel("spider:scheduler:node:pool:tasks", key)
            logger.info(f"{task_name} task done...")
    except Exception as e:
        email.send("task abnormal", e)
    save_task(value)

    return True


def run():
    rabbitmq = get_rabbitmq("test", ("guest", "guest"))
    rabbitmq.start_consuming(worker)


class ConsumerProcess:

    @classmethod
    def run(cls):
        with ProcessPoolExecutor() as process:
            while True:
                process.submit(run)


if __name__ == '__main__':
    def scheduler_socket():
        while True:
            sch_node = socket.socket()
            sch_node.connect(("127.0.0.1", 8867))
            sch_node.send(b"online74")
            while True:
                try:
                    data = sch_node.recv(4096).decode()
                    print(f"kill {data}")
                except:
                    pass
            time.sleep(10)


    thread = threading.Thread(target=scheduler_socket)
    thread.setDaemon(True)
    thread.start()
    ConsumerProcess.run()
