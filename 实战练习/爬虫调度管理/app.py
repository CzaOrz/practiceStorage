import socket
import threading
from flask import Flask, render_template
from crawler import bp_crawler
from flask_apscheduler import APScheduler
from setting import FlaskConfig

# for flask
app = Flask(__name__)
cfg = FlaskConfig()
app.config.from_object(cfg)
# for blueprint
app.register_blueprint(bp_crawler)
# for apschedule
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
# for nodes scheduler socket
nodes = {}


@app.route("/")
def index(): return render_template("index.html")


if __name__ == '__main__':
    def scheduler_socket():
        sch_host = socket.socket()
        sch_host.bind((cfg.host, cfg.port + 1))
        sch_host.listen(3)
        while True:
            try:
                soc, host = sch_host.accept()
                node_id = soc.recv(1024).decode()
                nodes[node_id] = soc
            except:
                pass


    thread = threading.Thread(target=scheduler_socket)
    thread.setDaemon(True)
    thread.start()
    app.run(host=cfg.host, port=cfg.port, debug=False)
