from flask import Flask, render_template
from crawler import bp_crawler
from flask_apscheduler import APScheduler
from setting import FlaskConfig

# for flask
app = Flask(__name__)
app.config.from_object(FlaskConfig())
# for blueprint
app.register_blueprint(bp_crawler)
# for apschedule
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route("/")
def index(): return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8866, debug=False)
