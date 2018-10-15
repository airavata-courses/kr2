pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'npm install --save-dev mocha'
                sh 'npm install --save-dev chai'
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
                sh 'mongo ds151612.mlab.com:51612/userprofile -u admin -p root99'
                sh 'db.userprofiles.remove({email:"john@gmail.com"})'
            }
        }

      }
    }
