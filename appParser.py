import re
import glob
from datetime import datetime as dt
import matplotlib.pyplot as plt

# fileNamePattern="log"
# path=/home/airavata/develop-deployment/api-orchestrator
# logDestination=""

# Regex used to match relevant loglines (in this case, a specific IP address)
# mystring="2018-11-09 00:10:15,756 [pool-31-thread-5] INFO  o.a.a.m.c.i.ExperimentConsumer  -  Message Received with message id 'LAUNC.HEX.P9207c058f82-43cfabda5a662afd6535' and with message type 'EXPERIMENT'  for experimentId: Gaussian_on_Nov_8,_2018_7:08_PM_707ff593-2c6e-417b-9db8-edb713d7e9ea"

msg_id_regex = re.compile("with message id\s(\S+)")
msg_type_regex = re.compile("with message type\s(\S+)")
exp_id_regex = re.compile("for experimentId:\s(\S+)")
exp_start_time = re.compile("o.a.a.m.c.i.RabbitMQPublisher  - Creating the channel for thread")


#assuming for a single experiment

# print(line_regex.search(mystring).group(1))


# Open input file in 'read' mode
expID=0
expDetails={}
# timestamp=[]
# date=[]
datelist=[]
time=[]

def getTime(line):
	line=line.split(" ")
	
	time=line[1].split(",")
	ms=time[1]
	timestamp=line[0]+" "+time[0]+"."+ms
	return dt.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")

def getDelta(t1,t2):
	total_seconds=(t1-t2).total_seconds()
	return total_seconds

	# return timestamp


with open("airavata.log", "r") as in_file:
	        # Loop over each log line
	for line in in_file:
	# line_regex.search(mystring).group(0)
	  	# If log line matches our regex, print to console, and output file
		if (msg_id_regex.search(line)):

			# print(line)
			msgID=msg_id_regex.search(line).group(1)


		if (msg_type_regex.search(line)):
			msgType=msg_type_regex.search(line).group(1)

		if(exp_id_regex.search(line)):
			expID=exp_id_regex.search(line).group(1)
			#set msg id and msg type
			expDetails[expID]={'msgID':msgID,'msgType':msgType} 
			# print ("INFO::" + expID)

			

		if(expID!=0):
			exp_gateway_id = re.compile(expID+"\sgateway Id:\s(\S+)")
			# print ("DEBUG::" + expID)
			
			
			if(exp_gateway_id.search(line)):
				expGateway=exp_gateway_id.search(line).group(1)
				expDetails[expID]["gateway"]=expGateway

			
			reqHandling_time_regex = re.compile("Message Received with message id\s"+msgID)	
			launch_time_start_regex = re.compile("Launching experiment with experimentId:\s"+expID)
			launch_time_end_regex = re.compile("expId:\s"+expID+", Launched experiment")
			gfac_time_start_regex = re.compile("expId:\s"+expID+", processId:"+"\s\S+"+"\s:-\s"+"Process status changed event received for status STARTED")
			gfac_time_end_regex = re.compile("expId:\s"+expID+", processId:"+"\s\S+"+"\s:-\s"+"Process status changed event received for status COMPLETED")
			exp_time_end_regex = re.compile("expId :\s"+expID+"\s:-\s"+"Experiment status updated to COMPLETED")


			if(reqHandling_time_regex.search(line)):
				timestamp_reqHandling=getTime(line)
				# print(timestamp_reqHandling)

			if(launch_time_start_regex.search(line)):
				timestamp_launch_start=getTime(line)
				# print(timestamp_launch_start)
			if(launch_time_end_regex.search(line)):
				# print(line)
				timestamp_launch_end=getTime(line)
				# print(timestamp_launch_end)
			if(gfac_time_start_regex.search(line)):
				# print(line)
				timestamp_gfac_start=getTime(line)
			if(gfac_time_end_regex.search(line)):
				timestamp_gfac_end=getTime(line)
				# print(timestamp_gfac_start)
			if(exp_time_end_regex.search(line)):
				timestamp_exp_end=getTime(line)	

		if exp_start_time.search(line):
			# line=line.split(" ")
			# # date.append(line[0])

			# # time.append(line[1])
			# time=line[1].split(",")
			# ms=time[1]
			# # time=time[0].split(":")
			# timestamp=line[0]+" "+time[0]+"."+ms
			timestamp=getTime(line)
			datelist.append(timestamp)

			# print("date",date)
			# print("time",time)
	# print(date[0])
	
	# b=dt.strptime(date[1], "%Y-%m-%d")
	print(min(datelist))
	StartTime=min(datelist)

	print("ReqHandling:",getDelta(timestamp_reqHandling,StartTime))
	print("Experiment Launch Time:",getDelta(timestamp_launch_end,timestamp_launch_start))
	print("Gfac start time:",getDelta(timestamp_gfac_start,timestamp_launch_end))
	print("Gfac end time:",getDelta(timestamp_gfac_end,timestamp_launch_start))
	print("Total Execution",getDelta(timestamp_exp_end,StartTime))

	# Data to plot
labels = 'ReqHandling', 'ExperimentLaunchTime', 'GfacStartTime', 'GfacEndTime'
sizes = [0.548, 2.341, 0.956, 147.098]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0, 0, 0, 0,0)  # explode 1st slice
 
# # Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
 
# plt.axis('equal')
# plt.show()

patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()

	







# expLaunchtime=""
print(expDetails)
# print(timestamp)

# 4:54:35:949 - admele


 # 04:57:17,770 - exp1 full logs





	
		