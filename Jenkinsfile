pipeline {
    agent any

    environment {
        PATH = "${WORKSPACE}/miniconda/bin:$PATH"
    }

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

        // Test install conda stage
        stage("Test conda installed") {
            steps {
                sh "exec bash"
                sh "conda init bash"
            }
        }

        // Install pipenv
        stage("Install Pipenv") {
            steps {
                sh "python3 install --user pipenv"
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

        /*
        // New install conda
        stage("Install conda try") {
            steps {
                echo "[INFO] Attempting to install conda"
                sh """
                    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh -O miniconda.sh
                    echo "[INFO] Successfully downloaded miniconda" 
                    echo "[INFO] Attempting to install Conda"
                    chmod +x miniconda.sh
                    ./miniconda.sh -b -p ${WORKSPACE}/miniconda
                    hash -r
                    conda config --set always_yes yes --set changeps1 no
                    exec bash
                    conda init bash
                    echo "[INFO] Successfully installed Conda."
                """
            }
        }
        */

        /*
        // Create Python Environment
        stage("Create Python Env") {
            environment {
                myEnv = "my-env3"
            }

            steps {
                sh """
                    echo "[INFO] Attempting to create Python environment"
                    conda create -n ${myEnv} python=3.9
                    echo "conda activate" >> /var/lib/jenkins/.bashrc
                    conda activate ${myEnv}
                    echo "[INFO] Enviroment successfully created and activated."
                """
            }
        }
    }
    */
}