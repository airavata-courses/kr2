import re

# import glob
from datetime import datetime as dt


# import matplotlib.pyplot as plotter




# Regex used to match relevant loglines

msg_id_regex = re.compile("with message id\s(\S+)")
msg_type_regex = re.compile("with message type\s(\S+)")
exp_id_regex = re.compile("experiment details with expId:\s(\S+)")
# exp_start_time = re.compile("o.a.a.m.c.i.RabbitMQPublisher  - Creating the channel for thread")
exp_start_time=re.compile("Airavata serching experiments for user")
exp_retr_user = re.compile("Airavata retrieved experiments for user")
exp_created = re.compile("Airavata created project with project Id")
exp_gateway_id = re.compile("GatewayID:\s(\S+)")
output_data_staging_regex = re.compile("Process status changed event received for status OUTPUT_DATA_STAGING")


flag_exp_submitted=0


#assuming for a single experiment



# Open input file in 'read' mode
expID=0
processId=0
msgID = 0
expDetails={}
# timestamp=[]
# date=[]
datelist=[]

def getTime(line):
    line=line.split(" ")
    time=line[1].split(",")
    ms=time[1]
    timestamp=line[0]+" "+time[0]+"."+ms
    return dt.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")

def getDelta(t1,t2):
    total_seconds=(t1-t2).total_seconds()
    return total_seconds

with open("airavata.log", "r") as in_file:
    for line in in_file:
        if exp_start_time.search(line):
            timestamp_exp_start=getTime(line)
        if exp_retr_user.search(line):
            timestamp_retr_user=getTime(line)

        if exp_id_regex.search(line):
            expID=exp_id_regex.search(line).group(1)
                    # print(expID)
                # set msg id and msg type
        if exp_created.search(line):
            timestamp_exp_created=getTime(line)

        if exp_gateway_id.search(line):
            expGateway=exp_gateway_id.search(line).group(1)
                # print(expGateway)

        if msg_id_regex.search(line):
            msgID=msg_id_regex.search(line).group(1)
            api_server_launched_regex = re.compile("Message Received with message id " + msgID)

        if (msg_type_regex.search(line)):
            msgType=msg_type_regex.search(line).group(1)
            # print("Message Type",msgType)
            expDetails[expID]={'Message ID': msgID,'Message Type': msgType}

        if expID != 0:
            expDetails[expID]=expGateway
            exp_submitted = re.compile("Experiment with expId: "+expID+" was submitted in gateway with gatewayID: "+expGateway)
            orchestrator_launch = re.compile("Launching experiment with experimentId: "+expID)
            orchestrator_launched = re.compile("expId: "+expID+", Launched experiment")
            exp_save_to_db = re.compile("experiment details with expId: " + expID + " saved to experiment catalog")
            exp_retr_output = re.compile("Airavata retrieved experiment output for expID: "+expID)
            exp_time_end_regex = re.compile("expId : "+expID+" :- "+"Experiment status updated to COMPLETED")
            batch_queue = re.compile("experiment_id="+expID+", gateway_id="+expGateway+" - Validation of org.apache.airavata.orchestrator.core.validator.impl.BatchQueueValidator is SUCCESSFUL")
            status_queue = re.compile("experiment_id="+expID+", gateway_id="+expGateway+" - Validation of org.apache.airavata.orchestrator.core.validator.impl.ExperimentStatusValidator is SUCCESSFUL")
            get_processId_regex = re.compile("expId: " +expID+", processId:\s(\S+)")
            helix_time_start_regex = re.compile("expId : "+expID+" :- Experiment status updated to EXECUTING")

            if helix_time_start_regex.search(line):
                timestamp_helix_start = getTime(line)

            if get_processId_regex.search(line):
                processId = get_processId_regex.search(line).group(1)

            if processId !=0:
                process_status_started_regex = re.compile("expId: "+expID+", processId: "+processId+" :- Process status changed event received for status STARTED")
                helix_time_end_regex = re.compile("expId: " + expID + ", processId: " + processId + " :- Process status changed event received for status COMPLETED")
                config_workspace_regex = re.compile("processId: "+processId+" :- Process status changed event received for status CONFIGURING_WORKSPACE")
                input_data_staging_regex = re.compile("processId: " + processId + " :- Process status changed event received for status INPUT_DATA_STAGING")
                process_executing_regex = re.compile("processId: " + processId + " :- Process status changed event received for status EXECUTING")

                if helix_time_end_regex.search(line):
                    timestamp_helix_end = getTime(line)

                if process_status_started_regex.search(line):
                    timestamp_process_status_started = getTime(line)
                    # print("Process executing", timestamp_process_executing)
                if config_workspace_regex.search(line):
                    timestamp_config_workspace = getTime(line)

                if input_data_staging_regex.search(line):
                    timestamp_input_data_staging = getTime(line)

                if process_executing_regex.search(line):
                    timestamp_process_executing = getTime(line)


            if msgID !=0:

                if api_server_launched_regex.search(line):
                    timestamp_api_server_launched=getTime(line)

            if exp_save_to_db.search(line):
                timestamp_save_db = getTime(line)

            if exp_submitted.search(line):
                timestamp_exp_submitted = getTime(line)

            if orchestrator_launch.search(line):
                timestamp_orchestrator_launch_start=getTime(line)

            if orchestrator_launched.search(line):
                timestamp_orchestrator_launch_end=getTime(line)

            if exp_retr_output.search(line):
                timestamp_retrieve_output = getTime(line)

            if exp_time_end_regex.search(line):
                timestamp_exp_end=getTime(line)

            if batch_queue.search(line):
                timestamp_batch_queue=getTime(line)

            if status_queue.search(line):
                timestamp_status_queue=getTime(line)

        if output_data_staging_regex.search(line):
            datelist.append(getTime(line))

timestamp_output_data_staging = getDelta(max(datelist), min(datelist))

Apiserver=getDelta(timestamp_api_server_launched,timestamp_exp_start)
Orchestrator=getDelta(timestamp_orchestrator_launch_end,timestamp_api_server_launched)
Helix=getDelta(timestamp_exp_end,timestamp_orchestrator_launch_end)

userPermissionChecks=getDelta(timestamp_retr_user,timestamp_exp_start)
saveToDB=getDelta(timestamp_save_db,timestamp_retr_user)
experimentCreation=getDelta(timestamp_exp_created,timestamp_save_db)
apiServerLaunch=getDelta(timestamp_api_server_launched,timestamp_exp_created)

queueValidation=getDelta(timestamp_batch_queue,timestamp_orchestrator_launch_start)
expStatusValidation=getDelta(timestamp_status_queue,timestamp_batch_queue)
orchestratorLaunch=getDelta(timestamp_orchestrator_launch_end,timestamp_orchestrator_launch_start)

processCreation=getDelta(timestamp_process_status_started,timestamp_orchestrator_launch_end)
helixProcessMapping=getDelta(timestamp_helix_start,timestamp_process_status_started)
t1_configWorkSpace=getDelta(timestamp_config_workspace,timestamp_helix_start)
t2_inputDataStaging=getDelta(timestamp_input_data_staging,timestamp_config_workspace)
# print(timestamp_output_data_staging)
t3_outputDataStaging=getDelta(max(datelist),timestamp_input_data_staging)
# computeResourceProcessExecution=getDelta()
# print(Apiserver,Orchestrator,Helix)
experimentCompletion=getDelta(timestamp_exp_end,max(datelist))



# get_Output_Data_Staging()
#
#
#
#
print("Experiment Start time:", timestamp_exp_start)
print("Retrieved experiment for user", timestamp_retr_user)
print("Experiment Save to DB time:",timestamp_save_db)
print("Experiment creation", timestamp_exp_created)
print("API Server Launch", timestamp_exp_submitted)
print("API Server Launched", timestamp_api_server_launched)
print("Orchestrator Launch",timestamp_orchestrator_launch_start)
print("Batch Queue Validator", timestamp_batch_queue)
print("Exp Status Validator", timestamp_status_queue)
print("Orchestrator Launched", timestamp_orchestrator_launch_end)
print("Process status started", timestamp_process_status_started)
print("Helix start", timestamp_helix_start)
print("Config WP", timestamp_config_workspace)
print("IP Data Staging", timestamp_input_data_staging)
print("Process status executing", timestamp_process_executing)
print("Output Data Staging",timestamp_output_data_staging)
print("Helix End", timestamp_helix_end)
print("Expirement end", timestamp_exp_end)




#
# print("ReqHandling:",getDelta(timestamp_airavata_server_launch,timestamp_exp_start))
# print("Experiment Launch Time:",getDelta(timestamp_orchestrator_launch_end,timestamp_orchestrator_launch_start))
# print("Helix start time:",getDelta(timestamp_helix_start,timestamp_orchestrator_launch_end))
# print("Helix end time:",getDelta(timestamp_helix_end,timestamp_orchestrator_launch_start))
# print("Experiment retrieved output time:",getDelta(timestamp_retrieve_output,timestamp_exp_start))
# print("Total Execution",getDelta(timestamp_exp_end,timestamp_exp_start))
#
#
#
#
#
#







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
