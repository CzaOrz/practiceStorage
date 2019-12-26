from flask import Blueprint, render_template

bp_crawler = Blueprint("crawler", __name__, url_prefix="/crawler")


@bp_crawler.route("/")
def index(): return render_template("crawler/scheduling.html")
