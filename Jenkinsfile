pipeline {
    agent any

    stages {
        stage('Install Dependecies') {
            steps {
                //sh 'kill -9 $(lsof -t -i:5000)'
                sh '/home/ubuntu/test_java.sh'
                sh 'sudo apt-get install maven -y'
                sh 'mvn -version'
                
                
            }
        }
        stage('Build Maven') {
            steps {
              dir('jobInterest'){
                   sh 'mvn clean install'
                   sh 'mvn install package'
                
                }
            
            }
        }
       }
    //post {
        //success{
             //build 'Deploy_to_prod_flask'            
        //}
        
    //}
    }
