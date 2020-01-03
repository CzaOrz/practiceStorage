import os
import psutil
import subprocess
from importlib import import_module
from minitools import Emailer, timekiller

try:
    email = Emailer("", "", "")
except:
    class FakeEmail:
        @classmethod
        def send(cls, *args, **kwargs): """no execute anything"""


    email = FakeEmail


def gather_tasks():
    all_tasks = {}
    tasks = import_module("async_scheduler.tasks")
    for attr in dir(tasks):
        if attr.startswith("_"):
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
    return f"{pid}_{task.node_id}", \
           {
               "task": task.name,
               "start_time": timekiller.get_now().strftime("%Y-%m-%d %H:%M:%S"),
               "_id": f"{task.log_id}",
               "pid": f"{pid or os.getpid()}",
           }


def decode_node_task(taskName: str):
    if not isinstance(taskName, str):
        return
    return TasksPool.query_task(taskName)  # type: async_scheduler.tasks.BaseTasks


def check_dir(dir_path, by_git=None):
    if by_git:
        if os.path.exists(dir_path):
            subprocess.run(f"cd {dir_path} && git pull >/dev/null 2>&1", shell=True)
        else:
            dir_path = os.path.dirname(dir_path)
            os.makedirs(dir_path, exist_ok=True)
            subprocess.run(f"cd dir_path && git clone {by_git} >/dev/null 2>&1", shell=True)
    else:
        os.makedirs(dir_path, exist_ok=True)
        os.chmod(dir_path, 0o777)


def kill_pid(pid):
    try:
        pid = int(pid)
        psutil.Process(pid).kill()
    except:
        pass
    return pid


def check_pid(pid):
    try:
        psutil.Process(int(pid))
        return True
    except:
        return False
