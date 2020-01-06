# -*- coding: utf-8 -*-
import json
import jieba
from minitools import current_file_path
from flask import request, abort, jsonify
from .bp import bp_other

try:
    from local_setting import ConsumerConfig
except:
    from setting import ConsumerConfig


def cutTitle(title):
    return [i for i in jieba.lcut(title) if len(i.strip()) > 1]


@bp_other.route('/news/classify', methods=["POST"])
def news_classification():
    title = request.json.get("title", None)
    if title:
        with open(current_file_path('allUniqueLabel.json', __file__), 'r') as f:
            json_data = json.loads(f.read())
        index_dict = {}
        for word in cutTitle(title):
            if word in json_data:
                index_dict[json_data.index(word)] = index_dict.get(json_data.index(word), 0) + 1
        wordLabel = None
        wordValue = 0
        with open(current_file_path('train.txt', __file__), 'r') as f:
            for content in f:
                json_data, label = content.strip().split('|')
                trainSet = json.loads(json_data)
                wordValueTemp = 0
                for key, value in index_dict.items():
                    trainKey = trainSet.get(str(key), None)
                    if trainKey:
                        wordValueTemp += value * trainKey
                if wordValueTemp > wordValue:
                    wordValue = wordValueTemp
                    label = '公示公告' if '公示' in label else label
                    label = '其他信息' if '住房资讯' in label else label
                    wordLabel = '其他信息' if '畜牧兽医' in label else label
        return jsonify({'classify': wordLabel, 'version': 'v3', 'status': 1})
    abort(403)


@bp_other.route('/house/predict', methods=["POST"])
def house_predict():
    city = request.json.get("city", None)
    area = request.json.get("area", None)
    house_area = request.json.get("house_area", None)
    if all((city, area, house_area)):
        with open(current_file_path('house_price.json', __file__), 'r') as f:
            try:
                json_data = json.loads(f.read())
                k, b, min_, ave_, max_ = json_data[city][area]
                return jsonify([int(house_area) * k + b, min_, ave_, max_])
            except:
                return abort(503)
    abort(403)


@bp_other.route('/house/predict/areas')
def house_predict_areas():
    try:
        with open(current_file_path('house_price.json', __file__), 'r') as f:
            json_data = json.loads(f.read())
            res = dict()
            for key in json_data:
                res[key] = list(json_data[key].keys())
            return jsonify(res)
    except:
        abort(403)
