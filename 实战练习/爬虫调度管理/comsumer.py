import os
import logging
import subprocess
from concurrent.futures.process import ProcessPoolExecutor
from minitools.db.amqp.rabbitmq import get_rabbitmq
from minitools.db.redisdb import get_redis_client
from utils.node import decode_node_task

logger = logging.getLogger(__name__)


def worker(data):
    pid = os.getpid()
    get_redis_client().hset()
    task = decode_node_task(data)
    task.run_command()
    get_redis_client().hset()


class ConsumerProcess:

    @classmethod
    def run(cls):
        rabbitmq = get_rabbitmq("test", ("czaorz", "czasg0.0"))
        with ProcessPoolExecutor() as process:
            while True:
                process.submit(rabbitmq.start_consuming, Worker)
