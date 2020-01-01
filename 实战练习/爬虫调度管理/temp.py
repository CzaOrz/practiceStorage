# import requests

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
