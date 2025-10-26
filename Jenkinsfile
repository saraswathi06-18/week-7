pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/saraswathi06-18/week-7.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t week7-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat 'docker stop week7-container || exit 0'
                    bat 'docker rm week7-container || exit 0'
                    bat 'docker run -d -p 5000:5000 --name week7-container week7-app'
                }
            }
        }
    }
}
