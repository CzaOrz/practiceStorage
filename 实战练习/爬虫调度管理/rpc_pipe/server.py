import socket
from setting import FlaskConfig
from .base import RPC

nodes = {}
import socketserver


class RPCServer(RPC):

    def serving(self):
        sch_host = socket.socket()
        sch_host.bind(("0.0.0.0", FlaskConfig.port + 1))
        sch_host.listen(3)
        while True:
            try:
                soc, host = sch_host.accept()
                node_id = soc.recv(1024).decode()
                nodes[node_id] = soc
            except:
                pass
