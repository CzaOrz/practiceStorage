from minitools import current_file_path


class FlaskConfig:
    secret_key = 'https://github.com/CzaOrz'
    JSON_AS_ASCII = False
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = {"default": {"type": "mongodb"}}  # db:apscheduler, coll:jobs

    SEND_FILE_MAX_AGE_DEFAULT = 0  # debug

    # scheduler socket will bind (host, port + 1), and the port will be used by flask
    host = "127.0.0.1"
    port = 8867


class ConsumerConfig:
    node_id = "default"  # need pointed
    node_dir = current_file_path("spiders", __file__)
    log_dir = current_file_path("logs", __file__)
    project_dir = node_dir

    # max worker process
    MAX_WORKER_PROCESS = 1

    # log config
    log_max_line = 300  # read max line from log
    log_max_rows = 1024  # read max string from one row

    # redis config
    redis_node_pool_tasks = "spider:scheduler:node:pool:tasks"

    # mongodb config
    mongodb_dbs_task = "scheduler"
    mongodb_col_task = "done"

    # flag for clear dirty node process
    CLEAR_DIRTY_NODE_PROCESS = b"DirtyProcessClear"


class RabbitMQConfig:
    # rabbit-mq config
    rabbitmq_queue = "test"
    rabbitmq_auth = ("guest", "guest")
    rabbitmq_conn_params = {}
    rabbitmq_exchange_params = {}
