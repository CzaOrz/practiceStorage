import requests

# print(requests.get("http://127.0.0.1:8867/scheduler/jobs").text)

# print(requests.post("http://127.0.0.1:8867/scheduler/jobs", json={
#     "id": "test_1",
#     "func": "async_scheduler:async_scheduler",
#     # "args": ("ZiruHousePrice",),
#     "kwargs": dict(task_name="ZiruHousePrice"),
#     "trigger": "cron",
#     "second": 5,
# }).text)

# print(requests.post("http://127.0.0.1:8867/scheduler/jobs/test_1/pause").text)

# print(requests.post("http://127.0.0.1:8867/scheduler/jobs/test_1/resume").text)

# print(requests.delete("http://127.0.0.1:8867/scheduler/jobs/test_1").text)

# print(requests.post("http://127.0.0.1:8867/scheduler/jobs/node/process/close").text)

# print(requests.patch("http://127.0.0.1:8867/scheduler/jobs/test_1", json={
#     # "trigger": "interval",
#     # "seconds": 5,
#     "trigger": "cron",
#     "second": 5,
# }).text)


# import time
# import socket
#
# import threading
# import select
# import selectors
#
# soc = socket.socket()
# soc.bind(("127.0.0.1", 8866))
# soc.listen(3)
#
# socks = {}
#
#
# def test():
#     while True:
#         if socks:
#             so = socks["test"]
#             try:
#                 so.setblocking(False)
#                 print(so.recv(1))
#             except (BlockingIOError, socket.timeout):
#                 print("报错了")
#             except ConnectionError:
#                 print("估计连接断开了")
#
#         print("pass")
#         time.sleep(5)
#
#
# threading.Thread(target=test).start()
#
# while True:
#     sock, address = soc.accept()
#     name = sock.recv(1024).decode()
#     socks[name] = sock
