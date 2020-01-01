from minitools import current_file_path


class FlaskConfig:
    secret_key = 'https://github.com/CzaOrz'
    JSON_AS_ASCII = False
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = {"default": {"type": "mongodb"}}  # db:apscheduler, coll:jobs

    SEND_FILE_MAX_AGE_DEFAULT = 0  # debug

    host = "0.0.0.0"
    port = 8867


class ConsumerConfig:
    node_id = ""
    node_dir = current_file_path("spiders", __file__)
    log_dir = current_file_path("logs", __file__)
    project_dir = node_dir
