from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    return {"request": request.get_json()}
