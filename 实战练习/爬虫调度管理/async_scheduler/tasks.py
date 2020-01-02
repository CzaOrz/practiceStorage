from minitools import timekiller, to_path, id_pool
from utils.node import check_dir

try:
    from local_setting import ConsumerConfig
except:
    from setting import ConsumerConfig


class BaseTask(ConsumerConfig):
    name = None  # show in web
    spider = None  # spider file.__name__
    project_git = None

    def __init__(self):
        now = timekiller.get_now()
        year, month, day = now.year, now.month, now.day
        log_path = to_path(self.log_dir, str(year), str(month), str(day))
        check_dir(log_path)
        check_dir(self.project_dir, self.project_git)
        self.log_id = id_pool.next_id()
        self.log_file = to_path(log_path, f"{self.log_id}.log")
        self.command = f"python {to_path(self.project_dir, self.spider)}.py >{self.log_file} 2>&1"  # todo, add source environment


class ZiRuSpider(BaseTask):
    name = "ZiruHousePrice"
    spider = "ziru_spider"


class LagouSpider(BaseTask):
    name = "LagouJob"
    spider = "ziru_spider"
