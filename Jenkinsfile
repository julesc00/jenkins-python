pipeline {
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
        stage("Install Pipenv") {
            steps {
                sh "pip3 install --user pipenv"
                echo "[INFO] Pipenv was installed successfully."
            }
        }

        // Create pipenv environment
        stage("Crete pipenv environment") {
            steps {
                sh "pipenv shell"
                sh "pipenv install -r requirements.txt"
            }
        }
    }
}