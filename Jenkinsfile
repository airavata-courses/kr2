pipeline {
    agent any
    environment {
    GOPATH = "$HOME/go"
    //PATH="$PATH:$GOROOT/bin:$GOPATH/bin"    
  }

    stages {

        stage('Build image') {
        steps{
        /* This builds the actual image; synonymous to
         * docker build on the command line */
         //sh 'sudo usermod -aG docker $USER'
         //sh 'newgrp docker'

    dockerfile {
        filename 'Dockerfile'
        
        label 'jobRec'
        args '-p 3050:3050 -v /var/run/docker.sock:/var/run/docker.sock'
        
        }
        }
    }

    

    stage('Test') {
            steps {

                sh 'go version'
                sh 'echo $GOPATH'
                //sh 'export GOPATH=$HOME/go'
                
                //sh 'echo $GOPATH'
                //sh 'go get -u github.com/golang/lint/golint'
                //echo 'Linting'
                //sh 'golint'
                sh 'go env'
                //sh 'go build'
                sh 'go run main.go &'
                echo 'testing API'
                sh 'go test -v .' 
            }
        }

      }
    }
