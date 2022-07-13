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

        // Installing deps and creating/running Django project
        stage("Install deps to local environment") {
            steps {

                sh "pip3 install -r requirements.txt"
                sh """ 
                    python3 manage.py runserver
                """
                sh ""
            }
        }
    }
}