pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    stages {
        stage('run backend server') {
            steps {
                script {
                    sh 'nohup python3 rest_app.py &'
                }
            }
        }

        stage('run frontend server') {
            steps {
                script {
                    sh 'nohup python3 web_app.py &'
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv .venv'
            }
        }
        stage('Activate Virtual Environment') {
            steps {
                sh '. .venv/bin/activate' // Linux/macOS
                //sh '. .venv\Scripts\activate' // Windows - Uncomment if needed
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install pymysql'
            }
        }
        stage('run backend_testing') {
            steps {
                script {
                    sh 'python3 backend_testing.py'
                }
            }
        }
        stage('Deactivate Virtual Environment') {
            steps {
                sh 'deactivate'
            }
        }

        stage('run frontend_testing') {
            steps {
                script {
                    sh 'python3 frontend_testing.py'
                }
            }
        }

        stage('run combined_testing') {
            steps {
                script {
                    sh 'python3 combined_testing.py'
                }
            }
        }

        stage('run clean_environment') {
            steps {
                script {
                    sh 'python3 clean_environment.py'
                }
            }
        }
    }
}