@Library("shared") _
pipeline {
    agent {
        label 'Node-1'
    }
   
    
     environment {
        IMAGE_NAME = 'sarthakk16/sarthak-flask'
        IMAGE_TAG = 'v1.02'
    }
    
    stages {
        stage("Greetings") {
            steps {
                echo "Hello from DevOps Team"
            }
        }

        stage("CHECKOUT") {
            steps {
                checkOut("https://github.com/Sarthu16/flaskci.git", "main")
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerBuild(
                        imageName: "${IMAGE_NAME}",
                        tag: "${IMAGE_TAG}"
                    )
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    dockerPush(
                        imageName: "${IMAGE_NAME}",
                        tag: "${IMAGE_TAG}",
                        credentialsId: 'docker-hub-creds'
                    )
                }
            }
        }   
        stage("DEPLOY") {
            steps {
                sh '''
                docker rm -f flask-container || true
                docker pull sarthakk16/sarthak-flask:v1.02
                docker run -d --name flask-container -p 5000:5000 sarthakk16/sarthak-flask:v1.02
                '''
            }
        }
    }
}
