pipeline {
    environment {
        PATH = "${WORKSPACE}/poetry/bin:bin$PATH"
    }
    agent any

    stages {
        stage("Git checkout") {
            steps {
                echo "Hi there world!"
            }
        }

        // Run simple Python script
        stage("Run Python script") {
            steps {
                sh "python3 script.py"
            }
        }

        // Install pipenv
        stage("Install Poetry") {
            steps {
                sh "pip3 install --user poetry"
                echo "[INFO] Pipenv was installed successfully."
                // sh "which poetry"
            }
        }

        // Create pipenv environment
        stage("Crete pipenv environment") {
            steps {
                sh "mkdir app && cd app"
                sh "poetry new ."
                sh "poetry shell"
                sh "poetry add django djangorestframework pytest pytest-django"
            }
        }
    }
}