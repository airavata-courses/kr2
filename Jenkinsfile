pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //sh 'kill -9 $(lsof -t -i:5000)'
                sh 'sudo apt-get install python3-pip -y'
                sh 'pip3 install -r requirements.txt'
                
                
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
