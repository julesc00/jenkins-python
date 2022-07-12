pipeline {
    environment {
        PATH = "${WORKSPACE}/poetry/bin:bin${PATH}"
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
                sh "pip3 install poetry"
                // sh "${HOME}/.poetry/bin/poetry install --no-root"
                echo "[INFO] Poetry was installed successfully."
                 sh "pwd"
            }
        }

        // Create pipenv environment
        stage("Create poetry environment") {
            steps {
                sh "mkdir app5 && cd app5 && pwd"
                sh "${WORKSPACE}/poetry/bin/poetry new django_app"
                sh "${WORKSPACE}/poetry/bin/poetry shell"
                sh "${WORKSPACE}/poetry/bin/poetry add 'django djangorestframework pytest pytest-django'"
            }
        }
    }
}