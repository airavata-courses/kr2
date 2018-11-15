# kr2



## Airavata Profiler

This project is an attempt to profile Apache Airavata based on the logs generated by the Airavata Orchestrator.
We have executed a Gaussian experiment on Airavata api dev server through the django portal and collected the respective logs.
Our profiler would parse the logs and report the time profile for each of the components.

#### Pre-requisites
1. Python3
2. matplotlib

#### Command to run
1. git clone <repo_id>
2. cd kr2
3. Run the below file
``python3 appParser.py``

#### Expected Output
Pie chart with time profiles for each components.

