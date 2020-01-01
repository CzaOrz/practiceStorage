# -*- coding: utf-8 -*-
import json
import logging
from minitools.db.amqp.rabbitmq import get_rabbitmq

rabbitmq = get_rabbitmq("test", ("guest", "guest"))
logger = logging.getLogger(__name__)


def async_scheduler(*args, **kwargs):
    if kwargs and "task_name" in kwargs:
        rabbitmq.push(json.dumps(kwargs, ensure_ascii=False))
        logger.debug("schedule success!")
