pipeline {
    agent any
    stages{
        stage("Git checkout") {
            steps {
                echo "Hi there world!"
            }
        }

        stage("Run Python Script") {
            sh "python3 script.py"
        }
    }
}