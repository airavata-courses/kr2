import re
import glob
from datetime import datetime as dt
import matplotlib.pyplot as plotter




# Regex used to match relevant loglines 

msg_id_regex = re.compile("with message id\s(\S+)")
msg_type_regex = re.compile("with message type\s(\S+)")
exp_id_regex = re.compile("experiment details with expId:\s(\S+)")
# exp_start_time = re.compile("o.a.a.m.c.i.RabbitMQPublisher  - Creating the channel for thread")
exp_start_time=re.compile("Airavata serching experiments for user")
exp_retr_user = re.compile("Airavata retrieved experiments for user")
exp_created = re.compile("Airavata created project with project Id")
exp_gateway_id = re.compile("GatewayID:\s(\S+)")


flag_exp_submitted=0


#assuming for a single experiment



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
                if exp_retr_user.search(line):
                    timestamp_retr_user=getTime(line)

                if(exp_id_regex.search(line)):
                    expID=exp_id_regex.search(line).group(1)
                    # print(expID)
                    #set msg id and msg type
                if(exp_created.search(line)):
                    timestamp_exp_created=getTime(line)
                if(exp_gateway_id.search(line)):
                        expGateway=exp_gateway_id.search(line).group(1)
                        # print(expGateway)
    
                
                if (msg_id_regex.search(line)):
                    msgID=msg_id_regex.search(line).group(1)
                    print(msgID)
                    airavata_server_launched_regex = re.compile("Message Received with message id\s"+msgID)

                if (msg_type_regex.search(line)):
                    msgType=msg_type_regex.search(line).group(1)
                    expDetails[expID]['msg']={'msgID':msgID,'msgType':msgType}



                if(expID!=0):
                    # print("EXPID:",expID)
                    
                    expDetails[expID]=expGateway
                    exp_submitted = re.compile("Experiment with expId:\s"+expID+" was submitted in gateway with gatewayID:\s"+expGateway)
                        

                    orchestrator_launch = re.compile("Launching experiment with experimentId:\s"+expID)
                    orchestrator_launched = re.compile("expId:\s"+expID+", Launched experiment")
                    helix_time_start_regex = re.compile("expId:\s"+expID+", processId:"+"\s\S+"+"\s:-\s"+"Process status changed event received for status STARTED")
                    helix_time_end_regex = re.compile("expId:\s"+expID+", processId:"+"\s\S+"+"\s:-\s"+"Process status changed event received for status COMPLETED")
                    exp_save_to_db =  re.compile("experiment details with expId:\s"+expID+" saved to experiment catalog")
                    exp_retr_output = re.compile("Airavata retrieved experiment output for expID:\s"+expID)
                    exp_time_end_regex = re.compile("expId :\s"+expID+"\s:-\s"+"Experiment status updated to COMPLETED")
                    batch_queue = re.compile("experiment_id="+expID+",\sgateway_id="+expGateway+"\s-\sValidation of org.apache.airavata.orchestrator.core.validator.impl.BatchQueueValidator is SUCCESSFUL")
                    status_queue = re.compile("experiment_id="+expID+",\sgateway_id="+expGateway+"\s-\sValidation of org.apache.airavata.orchestrator.core.validator.impl.ExperimentStatusValidator is SUCCESSFUL") 

                    if(airavata_server_launched_regex.search(line)):
                        timestamp_airavata_server_launch=getTime(line)

                    if exp_save_to_db.search(line):
                        timestamp_save_db = getTime(line)

                    if exp_submitted.search(line):
                        timestamp_exp_submitted = getTime(line)
                        #print("submit",timestamp_exp_submitted)

                    if(orchestrator_launch.search(line)):
                        timestamp_orchestrator_launch_start=getTime(line)

                    if(orchestrator_launched.search(line)):
                        timestamp_orchestrator_launch_end=getTime(line)

                    if(helix_time_start_regex.search(line)):
                        timestamp_helix_start=getTime(line)
                    if(helix_time_end_regex.search(line)):
                        timestamp_helix_end=getTime(line)
                    if exp_retr_output.search(line):
                        timestamp_retrieve_output = getTime(line)
                    if(exp_time_end_regex.search(line)):
                        timestamp_exp_end=getTime(line)

                    if(batch_queue.search(line)):
                        timestamp_batch_queue=getTime(line)
                        print(timestamp_batch_queue)
                    if(status_queue.search(line)):
                        timestamp_status_queue=getTime(line)
                        print(timestamp_status_queue)





	
print("Experiment Start time:", timestamp_exp_start)
print("Experiment Save to DB time:",getDelta(timestamp_save_db,timestamp_exp_start))
print("Experiment Submitted time:",getDelta(timestamp_exp_submitted,timestamp_exp_start))

print("ReqHandling:",getDelta(timestamp_airavata_server_launch,timestamp_exp_start))
print("Experiment Launch Time:",getDelta(timestamp_orchestrator_launch_end,timestamp_orchestrator_launch_start))
print("Helix start time:",getDelta(timestamp_helix_start,timestamp_orchestrator_launch_end))
print("Helix end time:",getDelta(timestamp_helix_end,timestamp_orchestrator_launch_start))
print("Experiment retrieved output time:",getDelta(timestamp_retrieve_output,timestamp_exp_start))
print("Total Execution",getDelta(timestamp_exp_end,timestamp_exp_start))
    












# pie chart depiction


# The slice names of a population distribution pie chart

# pieLabels2 = 'India', 'china', 'Europe', 'japan'
# pieLabels1 = 'ReqHandling', 'ExperimentLaunchTime', 'HelixStartTime', 'HelixEndTime'

# sizes = [0.548, 2.341, 0.956, 147.098]




# populationShare     = [25,25,25,25]



# #figureObject, axesObject = plotter.subplots()
# fig, ax = plotter.subplots(1,2)

# ax1, ax2 = ax.flatten()

# # Draw the pie chart

# #plotter.title("Experiment Execution in Airavata: System Analysis", bbox={'facecolor':'0.8', 'pad':5})
# ax1.title.set_text('First Plot')
# texts = ax1.pie(sizes,startangle=90)
# ax1.legend(pieLabels1, loc="best")




# # Aspect ratio - equal means pie is a circle

# ax1.axis('equal')


# ax2.pie(populationShare,
#         labels=pieLabels2 ,

#         autopct='%1.2f',

#        startangle=90)


# ax2.title.set_text('Second Plot')
# # # Aspect ratio - equal means pie is a circle
# ax2.axis('equal')


# # ax3.pie(populationShare,

# #         labels=pieLabels3 ,

# #         autopct='%1.2f',

# #         startangle=90)



# # # Aspect ratio - equal means pie is a circle

# # ax3.axis('equal')

# plotter.axis('off')

# plotter.show()
