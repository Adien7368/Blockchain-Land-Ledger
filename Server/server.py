import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ipList = []

@app.route('/', methods=['GET'])
def home():
    if request.url_root in ipList:
        return ipList[-1]
    else:
        ipList.append(request.url_root)
        return ipList[0]

app.run()
