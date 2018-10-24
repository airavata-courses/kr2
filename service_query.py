from flask import Flask
import requests
import json
from flask.json import jsonify
from flask import render_template, request
from flask_cors import CORS, cross_origin
import zc.zk

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/service_query',methods=['POST','OPTIONS','GET'])
@cross_origin(supports_credentials=True)

def service_query():
    zk = zc.zk.ZooKeeper('149.165.170.124:2182')
    url_java = zk.children('/usNaukri/java')
    url_flask = zk.children('/usNaukri/flask')
    url_node = zk.children('/usNaukri/node')
    url_java=['149.165.170.240:9090']
    url_flask=['149.165.170.151:5000']
    url_node=['149.165.170.57:4000']
    # print sorted(url_java),sorted(url_flask),sorted(url_node)

    return jsonify({"flask":url_flask[0],"java":url_java[0],"node":url_node[0]})
    # return "ok"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
   # app.run()
