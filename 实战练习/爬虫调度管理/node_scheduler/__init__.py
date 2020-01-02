import json
import socket
from flask import jsonify
from flask_apscheduler import APScheduler
from setting import FlaskConfig, ConsumerConfig
from minitools.db.redisdb import get_redis_client

scheduler = APScheduler()
nodes = {}


def scheduler_socket():
    sch_host = socket.socket()
    sch_host.bind(("127.0.0.1", FlaskConfig.port + 1))
    sch_host.listen(3)
    while True:
        try:
            soc, host = sch_host.accept()
            node_id = soc.recv(1024).decode()
            nodes[node_id] = soc
        except:
            pass


def close_node_process(node, process_id):
    node_id = node.split("_")[-1]
    if node_id not in nodes:
        return "", 404
    node_info = get_redis_client().hget(ConsumerConfig.redis_node_pool_tasks, node)
    if node_info and process_id in node_info.decode():
        nodes[node_id].send(f"{process_id}_{node}".encode())
    return ""


def all_online_nodes():
    nodes_copy = nodes.copy()
    for node_id, node_socket in nodes_copy.items():
        try:
            node_socket.setblocking(False)
            node_socket.recv(1)
        except (BlockingIOError, socket.timeout):
            continue
        except ConnectionError:
            nodes.pop(node_id)
    data = get_redis_client().hgetall(ConsumerConfig.redis_node_pool_tasks)
    print(data, type(data))
    return jsonify({
        "nodes": list(nodes.keys()),
        "tasks": {key.decode(): eval(value.decode()) for key, value in data.items()},
    })
