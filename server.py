from flask import Flask
import requests
import json
from flask.json import jsonify
from flask import render_template, request
from flask_cors import CORS, cross_origin
from kafka import KafkaProducer
from kafka.errors import KafkaError

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/job',methods=['POST','OPTIONS','GET'])
@cross_origin(supports_credentials=True)

def job_info():
   
   full_time=""
   userVal=request.values.to_dict(flat=True)
   desc=userVal['desc']
   jobType=userVal['jobType']
   email=userVal['email']

   if 'city' in userVal:
      city=userVal['city']
   if 'title' in userVal:
      title=userVal['title']
   

   if jobType=="true":
      full_time="true"
   elif jobType=="false":
      full_time="false"
   else:
      # print('jobType',jobType)
      return jsonify({"error": "jobType not passed as true/false"}), 400

   if (isinstance(desc, str)):
      pass
   else:
      #print(type(desc)),desc
      return jsonify({"error": "desc not passed as string"}), 400


   
   
   

   if city=="" and title=="":
      

      
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time)
      


   elif city =="":
      if (isinstance(title, str)):
         pass
      else:
         return jsonify({"error": "title not passed as string"}), 400
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time+"&search="+title)

   elif title =="":
      if (isinstance(city, str)):
         pass
      else:
         return jsonify({"error": "city not passed as string"}), 400
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time+"&location="+city)

   else:

      if (isinstance(city, str)):
         pass
      else:
         return jsonify({"error": "city not passed as string"}), 400
      if (isinstance(desc, str)):
         pass
      else:
         return jsonify({"error": "desc not passed as string"}), 400
      if (isinstance(title, str)):
         pass
      else:
         return jsonify({"error": "title not passed as string"}), 400
      
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time+"&location="+city+"&search="+title)
         

   try:
        producer = KafkaProducer(bootstrap_servers=['149.165.170.124:9092'])
        descKafka = bytes(desc, encoding= 'utf-8')
        emailKafka = bytes(email,encoding= 'utf-8')
        future = producer.send('sample',key=emailKafka,value=descKafka)
        record_metadata=future.get(timeout=10)
        #print(record_metadata.topic)
        #print(record_metadata.offset)
        #print(email)

   except:
        print("Kafka error")
	



   
   info=json.loads(response.text)
   
   return jsonify({"result":info}) ,200
   

@app.route('/jobs/testing',methods=['POST','OPTIONS','GET'])
@cross_origin(supports_credentials=True)

def jobs_apiTesting():
   return jsonify({"result":'US Naukri'}), 200

@app.route('/jobs/total',methods=['POST','OPTIONS','GET'])
@cross_origin(supports_credentials=True)

def jobs_total():
   userVal=request.values.to_dict(flat=True)
   #userVal=request.get_json()
   
   full_time=""
   try:
      desc=userVal['desc']
   except (KeyError, TypeError):
      return jsonify({"error": "desc not passed"}), 400
   try:
      jobType=userVal['jobType']
   except (KeyError, TypeError):
      return jsonify({"error": "jobType not passed"}), 400

   if jobType=="true":
      full_time="true"
   elif jobType=="false":
      full_time="false"
   else:
      # print 'jobType',jobType
      return jsonify({"error": "jobType not passed as true/false"}), 400


   if (isinstance(desc, str)):
      pass
   else:
      return jsonify({"error": "desc not passed as string"}), 400

   # try:
   #    if (isinstance(city, str)):
   #       pass
   #    else:
   #       return jsonify({"error": "city not passed as string"}), 400
   # except:
   #    pass


   try:
      response=requests.get("https://jobs.github.com/positions.json?search="+desc+"&full_time="+full_time)
   except ValueError:
      return jsonify({"error": "desc not passed"}), 400


   total=json.loads(response.text)
         
   return jsonify({"result":len(total)}), 200


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000) 
