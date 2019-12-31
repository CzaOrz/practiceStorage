class FlaskConfig:
    secret_key = 'https://github.com/CzaOrz'
    JSON_AS_ASCII = False
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = {"default": {"type": "mongodb"}}  # db:apscheduler, coll:jobs

    SEND_FILE_MAX_AGE_DEFAULT = 0  # debug


class ConsumerConfig:
    node_id = None
    node_dir = None
    command = None
