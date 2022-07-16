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
                    echo "Python version before activating environment"
                    ls -als
                    python3 --version
                    python3 -m venv my_env
                    source ${WORKSPACE}/my_env/bin/deactivate
                    source ${WORKSPACE}/my_env/bin/activate
                    python --version
                    pip list
                    pip install -r requirements.txt
                    pip list
                """

                echo "Run pytest"
                // sh "cd /var/lib/jenkins/workspace/${JOB_NAME}/"
                sh "ls -als"
                sh "python manage.py test"
                sh "python -m pytest -vv"
            }
        }
    }
}