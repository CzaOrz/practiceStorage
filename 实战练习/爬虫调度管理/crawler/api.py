# -*- coding: utf-8 -*-
import json
from minitools.db.mongodb import get_mongodb_client
from minitools import timekiller
from flask import jsonify, request
from .bp import bp_crawler

try:
    from local_setting import ConsumerConfig
except:
    from setting import ConsumerConfig


@bp_crawler.route("/api/ziru/data")
@bp_crawler.route("/api/ziru/data/<int:day>")
def api_ziru(day=15):
    mongodb_ziru_statistics = get_mongodb_client()["housePrice"]["ziru_zufang_statistics"]
    documents = mongodb_ziru_statistics.find(
        {"timestamp": {"$gte": timekiller.get_past_day(day).timestamp()}}, {"_id": 0})
    documents = list(documents)
    return jsonify({
        "status": 0,
        "data": {"ziru": documents}
    })


@bp_crawler.route("/api/lagou/data")
def api_lagou():
    query = request.args.get("query", "python")
    mongodb_lagou_statistics = get_mongodb_client()["job_lagou"][f"city_statistics_{query}"]
    document = mongodb_lagou_statistics.find_one({"timestamp": timekiller.get_today().timestamp()}, {"_id": 0})
    if document:
        return jsonify({
            "status": 0,
            "data": {"lagou": json.loads(document["statistics"])},
            "msg": "success",
        })
    else:
        return jsonify({
            "status": 2,
            "data": "",
            "msg": "Not query data",
        }), 404


@bp_crawler.route("/api/logs/<log_id>")
@bp_crawler.route("/api/logs/")
def api_log_list(log_id=None):
    col = get_mongodb_client()[ConsumerConfig.mongodb_dbs_task][ConsumerConfig.mongodb_col_task]
    if log_id:
        doc = col.find_one({"_id": log_id}, {"log_content": 1})["log_content"]
        return f"<pre>{doc}</pre>"
    documents = col.find({}, {"pid": 0, "log_content": 0}). \
        sort([('_id', -1)]).skip(0).limit(5)
    return jsonify(list(documents))
