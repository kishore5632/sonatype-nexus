pipeline {
    agent any
    environment {
        # Use the hosted repo for uploads, not the group
        PYPI_REPO = "http://localhost:8081/repository/python-hosted/"
        PYPI_CRED = credentials('nexus-username')  // single Jenkins credential
    }
    stages {
        stage('Setup, Build & Publish') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip setuptools wheel twine
                    python setup.py sdist bdist_wheel
                    twine upload --repository-url $PYPI_REPO -u $PYPI_CRED_USR -p $PYPI_CRED_PSW dist/*
                '''
            }
        }
        stage('Test Deployment') {
            steps {
                sh 'curl http://localhost:5000'
            }
        }
    }
}
