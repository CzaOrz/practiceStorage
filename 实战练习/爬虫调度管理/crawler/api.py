# -*- coding: utf-8 -*-
import json
from minitools.db.mongodb import get_mongodb_client
from minitools import timekiller
from flask import jsonify
from .bp import bp_crawler


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
    mongodb_lagou_statistics = get_mongodb_client()["job_lagou"]["city_statistics_python"]
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
