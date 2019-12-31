import os


def gather_tasks():
    all_tasks = {}
    from async_scheduler import tasks
    for attr in dir(tasks):
        if attr.startswith("__"):
            continue
        task = getattr(tasks, attr)
        name = getattr(task, "name", None)
        if name and hasattr(task, "command"):
            all_tasks.setdefault(name, task)
    return all_tasks


class TasksPool:
    tasks = {}

    @classmethod
    def query_task(cls, taskName):
        if not cls.tasks:
            cls.tasks = gather_tasks()
        if taskName not in cls.tasks:
            # todo, send error email
            return
        else:
            return cls.tasks[taskName]


def encode_node_task(task):
    return


def decode_node_task(taskName):
    return TasksPool.query_task(taskName)
