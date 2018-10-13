pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python server.py &'
            }
        }
        stage('Test') {
            steps {
                cd test
                sh 'python -m pytest' 
            }
        }

      }
    }
