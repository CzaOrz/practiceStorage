# -*- coding: utf-8 -*-
import threading
from flask import Flask, render_template, request, abort
from crawler import bp_crawler
from other import bp_other
from setting import FlaskConfig
from node_scheduler import scheduler, scheduler_socket, all_online_nodes, close_node_process, clear_dirty_node_process

# for flask
app = Flask(__name__)
cfg = FlaskConfig()
app.config.from_object(cfg)
# for blueprint
app.register_blueprint(bp_crawler)
app.register_blueprint(bp_other)
# for apschedule
scheduler.init_app(app)
scheduler.start()


@app.route("/")
def index():
    return render_template("index.html")


@app.before_request
def api_authentication():
    if str(request.url_rule).startswith((
            '/scheduler/jobs/nodes',
            '/scheduler/jobs/<node>',
            '/scheduler/jobs/<job_id>')):
        token = request.cookies.get('token')
        if token and token == 'czaissg':
            return
        return abort(403)


scheduler._add_url_route("clear_dirty_node_process", '/jobs/nodes/dirty/process/clear',
                         clear_dirty_node_process, 'POST')
scheduler._add_url_route("close_node_process", '/jobs/<node>/<process_id>/close', close_node_process, 'POST')
scheduler._add_url_route("all_online_nodes", '/jobs/online/nodes', all_online_nodes, 'GET')

if __name__ == '__main__':
    thread = threading.Thread(target=scheduler_socket)
    thread.setDaemon(True)
    thread.start()
    app.jinja_env.auto_reload = True  # debug
    app.run(host="0.0.0.0", port=cfg.port)
