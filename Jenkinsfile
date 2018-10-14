pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'sudo -S ./run.sh'
                
                
            }
        }
        stage('Test') {
            steps {
                sh 'go version'
                sh 'go get -u github.com/golang/lint/golint'
                echo 'Linting'
                sh 'golint'
                echo 'testing API'
                sh 'go test -v ./..' 
            }
        }

      }
    }
