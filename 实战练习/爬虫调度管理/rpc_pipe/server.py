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

"""
是的，规模大了以后 nginx 也可能成为瓶颈。但处理同样数量的并发，
uwsgi 消耗的资源要比简单做转发的 nginx 多，
所以一台 nginx 机器可以给多台 uwsgi 机器做均衡负载。
规模更大的情况下，会在 nginx 前再加 LVS, 这个就只做网络层的转发，
不做缓冲和协议转换了，还可以通过改包，让回包不经过 LVS.
更大的规模下，网络链路都可能成为瓶颈了。
这时就会从 anycast 和域名解析上做负载均衡了。
"""