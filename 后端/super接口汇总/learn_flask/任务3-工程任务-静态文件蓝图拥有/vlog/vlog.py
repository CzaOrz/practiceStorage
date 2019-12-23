from flask import Blueprint, render_template

# 加入template_folder参数可以指定文件使用当前路径下的资源
api = Blueprint("api", __name__, template_folder="html", url_prefix="/api")

@api.route("/")
def api_test():
    return render_template("test.html")