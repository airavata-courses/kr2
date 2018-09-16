from flask import Flask
import requests
import json
from flask.json import jsonify
from flask import render_template, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/job',methods=['POST','OPTIONS','GET'])
@cross_origin(supports_credentials=True)

def job_info():
   
   full_time="false"
   userVal=request.values.to_dict(flat=True)

   city=userVal['city']
   title=userVal['title']
   desc=userVal['desc']
   jobType=userVal['jobType']

   print type(city),type(title),desc,jobType

   if jobType == "Full Time":
      full_time="true"
      #print "Full time"

   

   if city=="" and title=="":
      # print "options null"
      # print 'full_time',full_time
      # print("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time)

      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time)

   elif city =="":
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time+"&search="+title)

   elif title =="":
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time+"&location="+city)

   else:
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time+"&location="+city+"&search="+title)
         



   # tech=test[0][0]
   #response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&search="+jobType)
   # print "karan"
   # print response.text
   l=json.loads(response.text)
   
   return jsonify({"result":l})
   

# @app.route('/python/')
# def hello_python():
#    return 'Hello Python'

if __name__ == '__main__':
   app.run()
