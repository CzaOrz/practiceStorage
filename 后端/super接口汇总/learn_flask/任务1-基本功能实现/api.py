# -*- coding: utf-8 -*-
from flask import (
    Flask,
    request,
    jsonify,
    abort,
    render_template,
    redirect, url_for,
    session,
    make_response,
)
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['cza'] = 'cza'
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index(): return f"hello world, {app.config['cza']}"


@app.route('/01/')
def api_01(): return "hello, this is api_01"


@app.route('/02/')  # 没有段代码, 就无法访问02接口了
@app.route('/02/<int:multi_path>/')  # 好吧-二者原来支持的程度差不多啊, 不过这玩意为什么后缀需要/斜杆呢
def api_02(multi_path=None): return f"hello, this is {multi_path}"


@app.route('/03')
def api_03():
    args = dict(request.args)
    cza = request.args.get('cza')
    return f"hello, this is {args}, and cza is {cza}"


@app.route('/04', methods=['POST'])
def api_04():
    form_data = dict(request.form)  # 参数为空, 此处返回{}, 也是可以的
    cza = form_data.get('cza')
    return jsonify({'status': 1, 'cza': cza, 'form': form_data})


@app.route('/05', methods=['POST'])
def api_05():
    json_data = request.json  # 没有json, 此处返回None
    cza = (json_data or {}).get('cza')
    return jsonify({'status': 1, 'cza': cza, 'json': json_data})


@app.route('/06')
def api_06():
    cookies = request.cookies  # cookies为空, 此处返回{}
    cza = cookies.get('cza')
    return jsonify({'status': 1, 'cza': cza, 'cookies': cookies})


@app.route('/07', methods=['POST'])
def api_07():
    cookies = request.cookies  # cookies为空, 此处返回{}
    cza = cookies.get('cza')
    return jsonify({'status': 1, 'cza': cza, 'cookies': cookies})


@app.route('/08')
def api_08(): abort(404)


@app.route('/09')
def api_09(): abort(404)


@app.route('/10', methods=['POST'])
def api_10(): abort(404)


@app.route('/11', methods=['POST'])
def api_11(): abort(404)


@app.errorhandler(404)
def api_404(error_text): return render_template('errors/error_404.html', error_text=error_text, error_code=404), 404


@app.route('/12')
def api_12(): return render_template('test/index.html', remarks="this is just a joke")  # 包括js/css等文件的加载


@app.route('/13')
def api_13(): return redirect(url_for('api_12'))  # 这里的url_for, 原来指定的不是path, 是函数名字.


@app.route('/14', methods=['POST'])
def api_14():
    dict(request.files)  # 没有参数的话是一个{}
    file = request.files['file']
    file.save(secure_filename(file.filename))
    return jsonify({'status': 1, 'path': 'path'})


@app.route('/15')
def api_15():
    session['api_15'] = "This is api-15"
    return redirect(url_for('api_15_redirect'))


@app.route('/15/redirect')
def api_15_redirect(): return f"hello, the value of session is {session.get('api_15')}"  # 在前端把cookie清掉就完事了


@app.route('/16')
def api_16(): return "Hello, this is api-16"


@app.before_request  # 添加钩子, 进来之前会执行此段函数
def api_16_before_request_0():
    cza = request.cookies.get('cza')
    if cza == 'cza-is-sg':
        return None
    abort(404)


@app.before_request  # 添加钩子, 接着上面之后执行
def api_16_before_request_1():
    orz = request.cookies.get('orz')
    if orz == 'cza-is-sg':
        return None
    resp = make_response(render_template('test/index.html', remarks="You Have No Permission!"))
    resp.set_cookie('userIdentity', 'temporary')
    resp.stpath_infoatus_code = 403
    return resp


@app.route('/17', methods=['OPTIONS'], provide_automatic_options=True)
def api_17():
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Headers': 'content-type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST'
    }
    return make_response((jsonify({'error_code': 0}), 200, headers))


@app.after_request
def add_default_headers(response):
    response.header.extend({
        'Content-Type': 'application/json',
        'Access-Control-Allow-Headers': 'content-type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST'
    })
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=False)
