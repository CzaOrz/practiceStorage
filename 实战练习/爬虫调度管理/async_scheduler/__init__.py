# -*- coding: utf-8 -*-
import logging
from minitools.db.amqp.rabbitmq import get_rabbitmq

rabbitmq = get_rabbitmq("test", ("czaorz", "czasg0.0"))
logger = logging.getLogger(__name__)


def async_scheduler(*args, **kwargs):
    print(args, kwargs)
    # rabbitmq.push("this is a test")
    logger.debug("schedule success!")
