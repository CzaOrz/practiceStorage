# -*- coding: utf-8
from flask import jsonify
from flask_apscheduler import APScheduler
from rpc_pipe.server import nodes, online_heartbeat
from minitools.db.redisdb import get_redis_client

try:
    from local_setting import ConsumerConfig
except:
    from setting import ConsumerConfig

scheduler = APScheduler()


def close_node_process(node, process_id):
    node_id = node.split("_")[-1]
    if node_id not in nodes:
        return "", 404
    node_info = get_redis_client().hget(ConsumerConfig.redis_node_pool_tasks, node)
    if node_info and process_id in node_info.decode():
        try:
            nodes[node_id].send(f"{process_id}_{node}".encode())
        except:
            pass
    return ""


def all_online_nodes():
    online_heartbeat()
    data = get_redis_client().hgetall(ConsumerConfig.redis_node_pool_tasks)
    return jsonify({
        "nodes": list(nodes.keys()),
        "tasks": [(key.decode(), eval(value.decode())) for key, value in data.items()],
    })
