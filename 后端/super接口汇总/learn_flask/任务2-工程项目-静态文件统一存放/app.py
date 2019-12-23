from flask import Flask, render_template
from minitools import current_file_path

app = Flask(__name__, root_path=current_file_path("html", __file__))

@app.route("/")
def index():
    return render_template("error/error_404.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=False)
