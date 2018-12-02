import re
import glob
from datetime import datetime as dt

# fileNamePattern="log"
# path=/home/airavata/develop-deployment/api-orchestrator
# logDestination=""

# Regex used to match relevant loglines (in this case, a specific IP address)
# mystring="2018-11-09 00:10:15,756 [pool-31-thread-5] INFO  o.a.a.m.c.i.ExperimentConsumer  -  Message Received with message id 'LAUNC.HEX.P9207c058f82-43cfabda5a662afd6535' and with message type 'EXPERIMENT'  for experimentId: Gaussian_on_Nov_8,_2018_7:08_PM_707ff593-2c6e-417b-9db8-edb713d7e9ea"

msg_id_regex = re.compile("with message id\s(\S+)")
msg_type_regex = re.compile("with message type\s(\S+)")
exp_id_regex = re.compile("for experimentId:\s(\S+)")
# exp_start_time = re.compile("o.a.a.m.c.i.RabbitMQPublisher  - Creating the channel for thread")
exp_start_time = re.compile("Airavata retrieved experiments for user")
flag_exp_submitted=0


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
                # Getting Experiment start time
                if exp_start_time.search(line):
                    timestamp_exp_start=getTime(line)

                if (msg_id_regex.search(line)):
                    msgID=msg_id_regex.search(line).group(1)
                if (msg_type_regex.search(line)):
                    msgType=msg_type_regex.search(line).group(1)
                if(exp_id_regex.search(line)):
                    expID=exp_id_regex.search(line).group(1)
			        #set msg id and msg type
                    expDetails[expID]={'msgID':msgID,'msgType':msgType}

                if(expID!=0):
                    # print("EXPID:",expID)
                    exp_gateway_id = re.compile(expID+"\sgateway Id:\s(\S+)")
                    if(exp_gateway_id.search(line)):
                        expGateway=exp_gateway_id.search(line).group(1)
                        expDetails[expID]["gateway"]=expGateway
                        exp_submitted = re.compile("Experiment with expId:\s"+expID+" was submitted in gateway with gatewayID:\s"+expGateway)
                        flag_exp_submitted = 1

                    reqHandling_time_regex = re.compile("Message Received with message id\s"+msgID)
                    launch_time_start_regex = re.compile("Launching experiment with experimentId:\s"+expID)
                    launch_time_end_regex = re.compile("expId:\s"+expID+", Launched experiment")
                    helix_time_start_regex = re.compile("expId:\s"+expID+", processId:"+"\s\S+"+"\s:-\s"+"Process status changed event received for status STARTED")
                    helix_time_end_regex = re.compile("expId:\s"+expID+", processId:"+"\s\S+"+"\s:-\s"+"Process status changed event received for status COMPLETED")
                    exp_save_to_db =  re.compile("experiment details with expId:\s"+expID+" saved to experiment catalog")
                    exp_time_end_regex = re.compile("expId :\s"+expID+"\s:-\s"+"Experiment status updated to COMPLETED")

                    if(reqHandling_time_regex.search(line)):
                        timestamp_reqHandling=getTime(line)

                    if exp_save_to_db.search(line):
                        timestamp_save_db = getTime(line)

                    if flag_exp_submitted == 1 and exp_submitted.search(line):
                        timestamp_exp_submitted = getTime(line)
                        #print("submit",timestamp_exp_submitted)

                    if(launch_time_start_regex.search(line)):
                        timestamp_launch_start=getTime(line)

                    if(launch_time_end_regex.search(line)):
                        timestamp_launch_end=getTime(line)

                    if(helix_time_start_regex.search(line)):
                        timestamp_helix_start=getTime(line)
                    if(helix_time_end_regex.search(line)):
                        timestamp_helix_end=getTime(line)

                    if(exp_time_end_regex.search(line)):
                        timestamp_exp_end=getTime(line)





	# b=dt.strptime(date[1], "%Y-%m-%d")
	# print(min(datelist))
	# StartTime=min(datelist)
print("Experiment Start time:", timestamp_exp_start)
print("Experiment Save to DB time:",getDelta(timestamp_save_db,timestamp_exp_start))
print("Experiment Submitted time:",getDelta(timestamp_exp_submitted,timestamp_exp_start))

print("ReqHandling:",getDelta(timestamp_reqHandling,timestamp_exp_start))
print("Experiment Launch Time:",getDelta(timestamp_launch_end,timestamp_launch_start))
print("Helix start time:",getDelta(timestamp_helix_start,timestamp_launch_end))
print("Helix end time:",getDelta(timestamp_helix_end,timestamp_launch_start))
print("Total Execution",getDelta(timestamp_exp_end,timestamp_exp_start))
    #



# pie chart depiction
# import the pyplot librar


# The slice names of a population distribution pie chart

#pieLabels1              = 'Asia', 'Africa', 'Europe', 'North America'
pieLabels2             = 'India', 'china', 'Europe', 'japan'
pieLabels3             = 'bangalore', 'mangalore', 'Europe', 'karwar'
pieLabels1 = 'ReqHandling', 'ExperimentLaunchTime', 'GfacStartTime', 'GfacEndTime'
sizes = [0.548, 2.341, 0.956, 147.098]


# Population data

populationShare     = [25,25,25,25]



#figureObject, axesObject = plotter.subplots()
fig, ax = plotter.subplots(1,2)

ax1, ax2 = ax.flatten()

# Draw the pie chart

#plotter.title("Experiment Execution in Airavata: System Analysis", bbox={'facecolor':'0.8', 'pad':5})
ax1.title.set_text('First Plot')
texts = ax1.pie(sizes,startangle=90)
ax1.legend(pieLabels1, loc="best")




# Aspect ratio - equal means pie is a circle

ax1.axis('equal')


ax2.pie(populationShare,
        labels=pieLabels2 ,

        autopct='%1.2f',

       startangle=90)


ax2.title.set_text('Second Plot')
# # Aspect ratio - equal means pie is a circle
ax2.axis('equal')


# ax3.pie(populationShare,

#         labels=pieLabels3 ,

#         autopct='%1.2f',

#         startangle=90)



# # Aspect ratio - equal means pie is a circle

# ax3.axis('equal')

plotter.axis('off')

plotter.show()
