import subprocess
import multiprocessing


class BaseTask:
    dir = ""
    command = ""

    @classmethod
    def run(cls): multiprocessing.Process(target=cls.run_command).start()

    @classmethod
    def run_command(cls):
        subprocess.Popen("")
