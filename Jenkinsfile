pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //sh 'kill -9 $(lsof -t -i:5000)'
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
        stage('Deploy') {
            steps {
                
                sh 'python3 server.py &'
            }
        }

      }
    }
