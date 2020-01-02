import threading
from flask import Flask, render_template
from crawler import bp_crawler
from setting import FlaskConfig
from node_scheduler import scheduler, scheduler_socket, all_online_nodes, close_node_process

# for flask
app = Flask(__name__)
cfg = FlaskConfig()
app.config.from_object(cfg)
# for blueprint
app.register_blueprint(bp_crawler)
# for apschedule
scheduler.init_app(app)
scheduler.start()
# for nodes scheduler socket
nodes = {}


@app.route("/")
def index():
    return render_template("index.html")


scheduler._add_url_route("close_node_process", '/jobs/<node>/<process_id>/close', close_node_process, 'GET')
scheduler._add_url_route("all_online_nodes", '/jobs/online/nodes', all_online_nodes, 'GET')

if __name__ == '__main__':
    thread = threading.Thread(target=scheduler_socket)
    thread.setDaemon(True)
    thread.start()
    app.run(host="0.0.0.0", port=cfg.port)
