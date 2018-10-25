pipeline {
    agent any

    stages {
        stage('Build React App') {
            steps {
                sh '/home/ubuntu/test_node.sh'
                sh 'sudo npm install -g create-react-app'
                dir('userinterface'){
                   sh 'npm install'
                   //sh 'npm start'
                   sh '''
                sudo kill -9 $(sudo lsof -t -i:2181)
                sudo /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties &
                sudo kill -9 $(sudo lsof -t -i:2182)
                sudo /opt/kafka/bin/zookeeper-server-start.sh /etc/zookeeper/conf/zoo-1.cfg &
                pid=`ps ax | grep -i \'kafka.Kafka\' | grep -v grep | awk \'{print $1}\'`
                if [ -n "$pid" ]
                    then
                   sudo kill -9 $pid
                fi
                sudo /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties &
                '''
                
                }
                
            }
        }
    }
       
    post {
        success{
             build 'Deploy_to_prod_react'            
        }
    }
        
      }
    
