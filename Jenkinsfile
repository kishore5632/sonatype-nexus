pipeline {
    agent any
    environment {
        PYPI_REPO = "http://localhost:8081/repository/pypi-group/"
        PYPI_USER = credentials('nexus-username')
        PYPI_PASS = credentials('nexus-password')
    }
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install --upgrade pip setuptools wheel twine'
            }
        }
        stage('Build') {
            steps {
                sh 'python setup.py sdist bdist_wheel'
            }
        }
        stage('Publish to Nexus') {
            steps {
                sh '''
                    twine upload --repository-url $PYPI_REPO -u $PYPI_USER -p $PYPI_PASS dist/*
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
