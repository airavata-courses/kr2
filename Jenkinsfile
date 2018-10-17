pipeline {
    agent any

    stages {
        stage('Build and Start React App') {
            steps {
                dir('userinterface'){
                   sh 'npm install'
                   sh 'npm start >/dev/null 2>&1 &'
                
                }
                
            }
        }

      }
      }
    
