# -*- coding: utf-8 -*-
import json
import logging
from minitools.db.amqp.rabbitmq import get_rabbitmq

try:
    from local_setting import RabbitMQConfig
except:
    from setting import RabbitMQConfig

rabbitmq = get_rabbitmq(queue=RabbitMQConfig.rabbitmq_queue,
                        conn_auth=RabbitMQConfig.rabbitmq_auth,
                        conn_params=RabbitMQConfig.rabbitmq_conn_params,
                        exchange_params=RabbitMQConfig.rabbitmq_exchange_params)
logger = logging.getLogger(__name__)


def async_scheduler(*args, **kwargs):
    if kwargs and "task_name" in kwargs:
        rabbitmq.push(json.dumps(kwargs, ensure_ascii=False))
        logger.info("schedule success!")
