pipeline {
    /*
    environment {
        PATH = "${WORKSPACE}/poetry/bin:bin$PATH"
    }
    */
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
                sh "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"
                sh "${HOME}/.poetry/bin/poetry install --no-root"
                echo "[INFO] Poetry was installed successfully."
                // sh "which poetry"
            }
        }

        // Create pipenv environment
        stage("Create poetry environment") {
            steps {
                sh "mkdir app2 && cd app2"
                sh "${HOME}/.poetry/bin/poetry new 'django_app'"
                sh "${HOME}/.poetry/bin/poetry shell"
                sh "${HOME}/.poetry/bin/poetry add 'django djangorestframework pytest pytest-django'"
            }
        }
    }
}