pipeline{
    options{timestamps()}

    agent any
    stages{
        stage('Check scm'){
            agent any
            steps{
                checkout scm
            }
        }
        stage('Build'){
            steps{
                echo "Building...${BUILD_NUMBER}"
                echo "Building completed"
                
            }
        }
        stage('Test'){
            agent { 
                docker {
                    image 'alpine'
                    args '-u=root'
                }
            }
            steps {
                sh 'apk add --update python3 py3-pip'
                sh 'pip install xmlrunner --break-system-packages'
                sh "python3 Lab_3_UnitTest.py"
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Something went wrong!"
                }
            }
            
        }
        stage('Docker Build'){
            steps {
                sh 'pwd'
                sh 'docker build -t lab3 /var/jenkins_home/workspace/Lab3/Lab3'
            }

        }
        stage('Build Docker Image Info') {
            steps {
                script {
                    // Отримати хеш коміту для тегу образу
                    def commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    // Створити тег образу
                    def imageTag = "alexeyprvz/jenkins_lab3"
                    // Записати тег образу у файл
                    writeFile file: 'docker-image-tag', text: imageTag
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def imageTag = readFile 'docker-image-tag'
                    // Створити Docker образ та позначити його тегом
                    def myimageTag = "alexeyprvz/jenkins_lab3"
                    sh "docker build -t ${myimageTag} /var/jenkins_home/workspace/Lab3/Lab3"
                }
            }
        }
        stage('Docker Hub Login') {
            steps {
                script {
                    sh "docker logout"
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                        sh "docker login --username=${DOCKER_HUB_USERNAME} --password=${DOCKER_HUB_PASSWORD}"
                        def imageTag = readFile 'docker-image-tag'
                        // Надіслати Docker образ на Docker Hub
                        sh "docker push alexeyprvz/jenkins_lab3"
                    }
                }
            }
        }
        
    }
}