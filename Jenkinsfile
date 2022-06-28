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

        // Install conda
        stage("Install Conda") {
            steps {
                script {
                    try {
                        sh "chmod +x miniconda.sh"
                        sh "./miniconda.sh -b -p ${WORKSPACE}/miniconda"
                        sh "hash -r"
                        sh "conda config --set always_yes yes --set changeps1 no"
                        sh "conda init bash"
                        echo "[INFO] Successfully installed conda"
                    }catch(error) {
                        sh """
                            wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh -O miniconda.sh
                            echo "[INFO] Successfully downloaded miniconda" 
                            echo "[INFO] Attempting to install Conda"
                            chmod +x miniconda.sh
                            ./miniconda.sh -b -p ${WORKSPACE}/miniconda
                            hash -r
                            conda config --set always_yes yes --set changeps1 no
                            conda init bash
                            echo "[INFO] Successfully installed Conda."
                        """
                    }
                }
            }
        }

        // Create Python Environment
        stage("Create Python Env") {
            environment {
                myEnv = "my-env"
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