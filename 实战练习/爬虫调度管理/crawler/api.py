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
        "data": {"ziru": documents}
    })


@bp_crawler.route("/api/lagou/data")
def api_lagou():
    return jsonify({
        "status": 0,
        "data": {"lagou": [
            {"all_count": 101791, "timestamp": 1577030400, "上海": 13927, "北京": 14433, "南京": 7413, "天津": 4532, "广州": 4612,
             "成都": 6608, "杭州": 10123, "武汉": 32500, "深圳": 7643},
            {"all_count": 101822, "timestamp": 1577116800, "上海": 13937, "北京": 14441, "南京": 7413, "天津": 4540, "广州": 4614,
             "成都": 6611, "杭州": 10123, "武汉": 32500, "深圳": 7643},
            {"all_count": 102060, "timestamp": 1577203200, "上海": 14059, "北京": 14490, "南京": 7415, "天津": 4563, "广州": 4615,
             "成都": 6614, "杭州": 10123, "武汉": 32530, "深圳": 7651},
            {"all_count": 102440, "timestamp": 1577289600, "上海": 14067, "北京": 14736, "南京": 7416, "天津": 4632, "广州": 4617,
             "成都": 6622, "杭州": 10124, "武汉": 32565, "深圳": 7661},
            {"all_count": 103451, "timestamp": 1577376000, "上海": 14608, "北京": 15146, "南京": 7427, "天津": 4633, "广州": 4619,
             "成都": 6623, "杭州": 10131, "武汉": 32580, "深圳": 7684}]}
    })
