from flask import jsonify
from .bp import bp_crawler

@bp_crawler.route("")
def api_test():
    return jsonify({"hello": "test"})

