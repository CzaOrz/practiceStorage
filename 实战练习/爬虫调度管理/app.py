from flask import Flask, render_template
from crawler import bp_crawler

app = Flask(__name__)
app.secret_key = 'https://github.com/CzaOrz'
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def index(): return render_template("index.html")


if __name__ == '__main__':
    app.register_blueprint(bp_crawler)
    app.run(host="0.0.0.0", port=8866, debug=False)
