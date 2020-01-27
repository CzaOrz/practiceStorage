from flask import Flask, render_template, request, jsonify
from collections import defaultdict
app = Flask(__name__)
data = {}
database = defaultdict(list)
transaction_db = [{None: {1: 100}}, {None: {4: 200}}, {None: {49: 300}}, {None: {1: 1100}}]  # save [{None: {lot: price}}, ]

@app.route("/api/get/lottery/count")
def api_api():
    detail = defaultdict(list)
    for transaction in transaction_db:
        for username, dict_value in transaction.items():
            for lot, price in dict_value.items():
                detail.setdefault(lot, [0])
                detail[lot][0] = detail.get(lot, [0])[0] + price
                detail[lot].append(transaction)
    detail_data = []
    for key, value in detail.items():
        detail_data.append({key: value})
    return jsonify({
        "lottery_count": sorted(detail_data, key=lambda lis: list(lis.values())[0], reverse=True),
        "history_data": transaction_db,
    })

@app.route("/api/add/lottery", methods=["POST"])
def add_lottery():
    username = request.json.get("username", None)
    lottery_num = request.json.get("lottery_num", None)
    lottery_price = request.json.get("lottery_price", 0)
    if lottery_num:
        global transaction_db
        transaction_db.append({username: {lottery_num: lottery_price}})
    return ""

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,PATCH'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,application/json'
    return response

if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['JSON_AS_ASCII'] = True
    app.jinja_env.auto_reload = True  # debug
    app.run(debug=False)
