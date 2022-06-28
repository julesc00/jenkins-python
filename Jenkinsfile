pipeline {
    agent any
    stages{
        stage("Git checkout") {
            steps {
                echo "Hi there world!"
            }
        }

        stage("Run Python Script") {
            steps {
                sh "python3 script.py"
                sh """
                    conda activate my-env
                    pip install django
                """
            }
        }
    }
}