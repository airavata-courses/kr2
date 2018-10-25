pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //sh 'kill -9 $(lsof -t -i:5000)'
                sh 'sudo apt-get install python3-pip -y'
                sh 'pip3 install -r requirements.txt'
                //sudo kill -9 $(sudo lsof -t -i:2181)
                sh '''
                pidz1 = sudo lsof -t -i:2181
                pidz2 = sudo lsof -t -i:2182
                if [ -n "$pidz1" ]
                then
                :
                else 
                sudo /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties &
                fi
                if [ -n "$pidz2" ]
                then
                :
                else 
                sudo /opt/kafka/bin/zookeeper-server-start.sh /etc/zookeeper/conf/zoo-1.cfg &
                fi

                
                
                
                
                pid=sudo lsof -t -i:9092
                if [ -n "$pid" ]
                then
                    :
                else
                sudo /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties &
                fi
                
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
