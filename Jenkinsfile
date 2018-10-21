pipeline {
    agent any

    stages {
        stage('Build and Start React App') {
            steps {
                sh '/home/ubuntu/test_node.sh'
                sh 'sudo npm install -g create-react-app'
                dir('userinterface'){
                   sh 'npm install'
                   //sh 'npm start'
                
                }
                
            }
        }

      }
      }
    
