import os
from importlib import import_module
from minitools import Emailer, timekiller

email = Emailer


def gather_tasks():
    all_tasks = {}
    tasks = import_module("async_scheduler.tasks")
    for attr in dir(tasks):
        if attr.startswith("__"):
            continue
        task = getattr(tasks, attr)
        name = getattr(task, "name", None)
        if name and getattr(task, "spider", None):
            all_tasks.setdefault(name, task)
    return all_tasks


class TasksPool:
    tasks = {}

    @classmethod
    def query_task(cls, taskName):
        if not cls.tasks:
            cls.tasks = gather_tasks()
        if taskName not in cls.tasks:
            email.send("task abnormal", f"there is not task {taskName} in {cls.__name__}")
        else:
            return cls.tasks[taskName]


def encode_node_task(task, pid=None):
    return f"{os.getpid()}{task.node_id}", \
           {
               "task": task.name,
               "start_time": timekiller.get_now().strftime("%Y-%m-%d %H:%M:%S"),
               "pid": f"{pid or os.getpid()}",
           }


def decode_node_task(taskName):
    return TasksPool.query_task(taskName)


def check_dir(dir_path):
    os.makedirs(dir_path, exist_ok=True)
    os.chmod(dir_path, 0o777)
