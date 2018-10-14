pipeline {
    agent {dockerfile true}

    stages {

        stage('Build image') {
        steps{
        /* This builds the actual image; synonymous to
         * docker build on the command line */

    dockerfile {
        filename 'Dockerfile'
        
        label 'jobRec'
        args '-p 3050:3050'
        }
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
