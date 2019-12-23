from vlog.vlog import api, render_template

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test.html")


if __name__ == '__main__':
    app.register_blueprint(api)
    app.run(host='127.0.0.1', port=8888, debug=False)

