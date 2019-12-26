from minitools.db.mongodb import get_mongodb_client
from minitools import timekiller
from flask import jsonify
from .bp import bp_crawler

mongodb_ziru = get_mongodb_client()["housePrice"]["ziru_zufang"]
mongodb_ziru_statistics = get_mongodb_client()["housePrice"]["ziru_zufang_statistics"]


@bp_crawler.route("/api/ziru/data")
def api_ziru():
    doc = mongodb_ziru_statistics.find_one({"timestamp": timekiller.get_today().timestamp()}, {"_id": 0})
    return jsonify(doc)
