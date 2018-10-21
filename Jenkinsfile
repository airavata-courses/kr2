pipeline {
    agent any
    environment {
    GOROOT="/var/lib/jenkins/go"    
    GOPATH = "/var/lib/jenkins/go-path"
    PATH="$PATH:$GOROOT/bin:$GOPATH/bin"    
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
        
        echo 'build done'
        
        }
        }
    }

    

    stage('Test') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get -y upgrade'
                sh 'cd /opt/'
                sh 'wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz'
                sh 'sudo tar -xvf go1.8.linux-amd64.tar.gz'
                sh 'sudo mkdir -p /var/lib/jenkins/go'
                sh'''
                if [ "$(ls -A /var/lib/jenkins/go)" ]; then
                echo "Take action  Go DIR is not Empty"
                else
                sudo mv go /var/lib/jenkins/
                '''
                //sh 'sudo mv go /var/lib/jenkins/'
                sh 'sudo mkdir -p /var/lib/jenkins/go-path'

                //sh 'sudo echo -n \'export GOROOT="/var/lib/jenkins/go"\' >> ~/.bashrc'
                //sh 'sudo echo -n \'export GOPATH="/var/lib/jenkins/go-path"\' >> ~/.bashrc' 
                //sh 'sudo echo -n \'export PATH="$PATH:$GOROOT/bin:$GOPATH/bin"\' >> ~/.bashrc'

                //sh 'sudo source ~/.bashrc'

                echo "go version"

                sh 'go version'
                sh 'echo $GOPATH'
                //sh 'export GOPATH=$HOME/go'
                
                //sh 'echo $GOPATH'
                //sh 'go get -u github.com/golang/lint/golint'
                //echo 'Linting'
                //sh 'golint'
                //sh 'go env'
                //sh 'go build'
                sh 'go get github.com/gin-contrib/cors'
                sh 'go get github.com/gin-gonic/gin'
                sh 'go run main.go &'
                echo 'testing API'
                sh 'go test -v .' 
            }
        }

      }
    }
