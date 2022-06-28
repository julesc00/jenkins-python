pipeline {
    agent any
    stages{
        stage("Git checkout") {
            steps {
                sh "git branch: 'main', url: 'https://github.com/julesc00/jenkins-python.git'"
                echo "Hi there world!"
            }
        }
    }
}