pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'git@github.com:Mushmat/calculator-cli.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "No build required for Python CLI"'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 calculator.py <<EOF\n+\n5\n3\nEOF'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t calculator-cli .'
            }
        }
    }
}
