import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/test", methods=["POST"])
def test_post():
    print("接收到post请求")
    data = json.loads(request.data)
    print("data: {}".format(data))
    return ""


@app.route("/testfile", methods=["POST"])
def test_file():
    print("收到post请求")
    for k, v in request.files.items():
        print("{}".format(k))
        v.save(k)
    return ""


if __name__ == '__main__':
    app.run("0.0.0.0", 9999)
