pipeline {
    agent { docker { image 'python:2.7.15' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
