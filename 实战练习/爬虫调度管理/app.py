# -*- coding: utf-8 -*-
import threading
from minitools import to_md5
from flask import Flask, request, abort, make_response, redirect
from crawler import bp_crawler
from other import bp_other
from setting import FlaskConfig
from rpc_pipe.server import RPCServer
from node_scheduler import scheduler, all_online_nodes, close_node_process

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
    token = request.args.get('token')
    if token and to_md5(token) == 'e67224f2f17d8a4c2327f6f05cbb4ab7':
        response = make_response(redirect('/crawler'))
        response.set_cookie('token', token, max_age=3600)
        return response
    abort(404)


@app.before_request
def api_authentication():
    if str(request.url_rule).startswith((
            '/scheduler/jobs/nodes',
            '/scheduler/jobs/<node>',
            '/scheduler/jobs/<job_id>')):
        token = request.cookies.get('token')
        if token and to_md5(token) == 'e67224f2f17d8a4c2327f6f05cbb4ab7':
            return
        return abort(403)


scheduler._add_url_route("close_node_process", '/jobs/<node>/<process_id>/close', close_node_process, 'POST')
scheduler._add_url_route("all_online_nodes", '/jobs/online/nodes', all_online_nodes, 'GET')

if __name__ == '__main__':
    RPCServer().run()
    app.jinja_env.auto_reload = True  # debug
    app.run(host="0.0.0.0", port=cfg.port)
