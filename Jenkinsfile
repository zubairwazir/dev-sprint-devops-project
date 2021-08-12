pipeline{
    agent any
    environment{
        DATABASE_URI= os.getenv('DATABASE_URI')
        DOCKERHUB_CREDENTIALS= ..
    }
    stages{
        stage('Unit Testing'){
            steps{
                sh "bash scripts/test.sh"
            }
        }   
    stages{
        stage('Build Images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }
    stages{
        stage('Push Images'){
            steps{
                sh "bash scripts/push.sh"
            }
        }
    stages{
        stage('Configure & Deploy'){
            steps{
                sh "bash scripts/deploy.sh"
            }
        }
    }
}