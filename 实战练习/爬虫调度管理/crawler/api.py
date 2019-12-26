# -*- coding: utf-8 -*-
from minitools.db.mongodb import get_mongodb_client
from minitools import timekiller
from flask import jsonify
from .bp import bp_crawler

mongodb_ziru = get_mongodb_client()["housePrice"]["ziru_zufang"]
mongodb_ziru_statistics = get_mongodb_client()["housePrice"]["ziru_zufang_statistics"]


@bp_crawler.route("/api/ziru/data")
@bp_crawler.route("/api/ziru/data/<int:day>")
def api_ziru(day=15):
    # 1、需要总量，然后相减，画出近15日统计增量折线图
    # 2、需要各地域的数据，左边诶总量，右边为日增量
    documents = mongodb_ziru_statistics.find(
        {"timestamp": {"$gte": timekiller.get_past_day(day).timestamp()}}, {"_id": 0})
    documents = list(documents)
    documents.sort(key=lambda di: di["timestamp"])
    count_statistics = [document["all_count"] for document in documents]
    return jsonify({
        "status": 0,
        "ziru": documents,
    })
