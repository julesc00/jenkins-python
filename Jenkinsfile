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
            when {
                expression {
                    ${env.WORKSPACE}/miniconda
                }
            }
            steps {
                echo "Miniconda is already installed."
                sh "exec bash"
                sh "conda init bash"
            }
        }

        // New install conda
        stage("Install conda try") {
            when {
                expression {
                    !${WORKSPACE}/miniconda
                }
            }
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

        // Create Python Environment
        stage("Create Python Env") {
            environment {
                myEnv = "my-env2"
            }

            steps {
                sh """
                    echo "[INFO] Attempting to create Python environment"
                    conda create -n ${myEnv} python=3.9
                    conda activate ${myEnv}
                    echo "[INFO] Enviroment successfully created and activated."
                """
            }
        }
    }
}