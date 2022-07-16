pipeline {
    /*environment {
        PATH = "${WORKSPACE}/poetry/bin:bin${PATH}"
    }
    */
    agent any

    stages {
        stage("Git checkout") {
            steps {
                echo "Hi there world!"
            }
        }

        stage("Update Python Version") {
            steps {
                sh """
                    echo "[INFO] Updating Python version..."
                    yum update
                    yum -y install python39

                    python3.9 --version
                    yum install python39-pip -y
                """
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
        stage("Start Python environment") {
            steps {
                sh """
                    echo "[INFO] Python version before activating environment"
                    ls -als
                    python3 --version
                    python3 -m venv my_env
                    source my_env/bin/activate

                    echo "[INFO] Python version after activating environment"
                    python --version
                    pip list
                    pip install -r requirements.txt
                    pip list
                    python manage.py migrate

                    pytest --junitxml=./xmlReport/output.xml
                """

                echo "Run pytest"
                // sh "cd /var/lib/jenkins/workspace/${JOB_NAME}/"
                sh "pwd"
                sh "ls -als"
                sh "echo $PATH"
            }
        }
    }
}