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
    
