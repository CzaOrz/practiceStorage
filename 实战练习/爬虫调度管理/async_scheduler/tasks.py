import logging
import subprocess

logger = logging.getLogger(__name__)

try:
    from local_setting import ConsumerConfig
except:
    raise RuntimeError("Please copy setting file as to local_setting and config it")


class BaseTask(ConsumerConfig):
    command = None

    @classmethod
    def run_command(cls):
        subprocess.run(cls.command, shell=True)
        raise NotImplementedError


class ZiRuSpider(BaseTask):
    name = "ZiruHousePrice"  # show in web
    spider = "ziru_spider"  # spider file.__name__

    @classmethod
    def run_command(cls):
        command = cls.command
