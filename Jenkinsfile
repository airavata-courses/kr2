pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '/home/ubuntu/test_node.sh'
                sh 'npm install --save-dev mocha'
                sh 'npm install --save-dev chai'
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        //stage('Deploy') {
            //steps {
                //sh 'node index.js &'

                 
            //}
        //}

      }
    }
