pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //sh 'kill -9 $(lsof -t -i:5000)'
                sh 'sudo apt-get install python3-pip -y'
                sh 'pip3 install -r requirements.txt'
                sh '''
                sudo kill -9 $(sudo lsof -t -i:2181)
                sudo /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties &
                pid=`ps ax | grep -i \'kafka.Kafka\' | grep -v grep | awk \'{print $1}\'`
                if [ -n "$pid" ]
                    then
                   sudo kill -9 $pid
                fi
                sudo /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties &
                '''
                
                
            }
        }
        stage('Test') {
            steps {
                //sh 'python3 server.py &'
                sh 'python3 -m pytest test/'
                //sh 'kill -9 $(lsof -t -i:5000)'
            }
        }
       }
    post {
        success{
             build 'Deploy_to_prod_flask'            
        }
        
    }
    }
