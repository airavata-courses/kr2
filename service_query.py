from flask import Flask
import json
from flask.json import jsonify
from flask import render_template, request
from flask_cors import CORS, cross_origin
# import zc.zk
from kazoo.client import KazooClient

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/service_query',methods=['POST','OPTIONS','GET'])
@cross_origin(supports_credentials=True)

def service_query():

    zk = KazooClient(hosts='149.165.170.124:2182')
    zk.start()
    url_flask,stat = zk.get("/usNaukri/flask")
    url_java ,stat = zk.get("/usNaukri/java")
    url_node ,stat = zk.get("/usNaukri/node")
    # print url_flask,url_java,url_node
    return jsonify({"flask":url_flask,"java":url_java,"node":url_node})
    # return "ok"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
   #app.run()
