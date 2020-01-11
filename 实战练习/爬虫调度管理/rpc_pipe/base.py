import threading


class RPC:

    def serving(self):
        raise NotImplementedError

    def run(self):
        thread = threading.Thread(target=lambda: None)
        thread.setDaemon(True)
        thread.start()
