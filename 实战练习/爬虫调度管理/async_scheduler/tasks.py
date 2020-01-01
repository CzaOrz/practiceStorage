from uuid import uuid4
from minitools import timekiller, to_path
from utils.node import check_dir

try:
    from local_setting import ConsumerConfig
except:
    raise RuntimeError("Please copy setting file as to local_setting and config it")


class BaseTask(ConsumerConfig):
    name = None  # show in web
    spider = None  # spider file.__name__

    def __init__(self):
        now = timekiller.get_now()
        year, month, day = now.year, now.month, now.day
        log_path = to_path(self.log_dir, str(year), str(month), str(day))
        check_dir(log_path)
        self.log_file = to_path(log_path, f"{uuid4()}.log")
        self.command = f"python {to_path(self.project_dir, self.spider)}.py >{self.log_file} 2>&1"  # add source environment


class ZiRuSpider(BaseTask):
    name = "ZiruHousePrice"
    spider = "ziru_spider"
