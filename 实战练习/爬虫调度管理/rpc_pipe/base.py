import threading

try:
    from local_setting import FlaskConfig, ConsumerConfig
except:
    from setting import FlaskConfig, ConsumerConfig


class RPC:
    host = FlaskConfig.host
    port = FlaskConfig.port + 1
    node_id = ConsumerConfig.node_id
    redis_node_pool_tasks = ConsumerConfig.redis_node_pool_tasks
    consumerConfig = ConsumerConfig

    def serving(self):
        raise NotImplementedError

    def run(self):
        thread = threading.Thread(target=self.serving)
        thread.setDaemon(True)
        thread.start()
