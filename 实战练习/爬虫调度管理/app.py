from flask import Flask, render_template
from crawler import bp_crawler
from flask_apscheduler import APScheduler

app = Flask(__name__)


class Config:
    secret_key = 'https://github.com/CzaOrz'
    JSON_AS_ASCII = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SCHEDULER_API_ENABLED = True


app.config.from_object(Config())
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route("/")
def index(): return render_template("index.html")


if __name__ == '__main__':
    app.register_blueprint(bp_crawler)
    app.run(host="0.0.0.0", port=8866, debug=False)
