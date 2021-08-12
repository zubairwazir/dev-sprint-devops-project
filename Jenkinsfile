pipeline{
    agent any
    environment{
    }
    stages{
        stage('Unit Testing'){
            steps{
                sh "bash scripts/test.sh"
            }
        }   
        stage('Build Images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }
        stage('Push Images'){
            steps{
                sh "bash scripts/push.sh"
            }
        }
        stage('Configure & Deploy'){
            steps{
                sh "bash scripts/deploy.sh"
            
            }
        }
    }
}