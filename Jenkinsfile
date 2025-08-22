pipeline {
    agent any
    environment {
        PYPI_REPO = "http://localhost:8081/repository/python-hosted/"
        PYPI_CRED = credentials('nexus-username')  // single Jenkins credential
    }
    stages {
        stage('Setup & Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip setuptools wheel twine flask
                    python setup.py sdist bdist_wheel
                '''
            }
        }

        stage('Upload to Nexus') {
            steps {
                sh '''
                    . venv/bin/activate
                    twine upload --repository-url $PYPI_REPO -u $PYPI_CRED_USR -p $PYPI_CRED_PSW dist/*
                '''
            }
        }

        stage('Test Package Installation') {
            steps {
                sh '''
                    python3 -m venv test_env
                    . test_env/bin/activate
                    pip install --upgrade pip
                    pip install dist/*.whl
                    python -c "from python_nexus_app import app; print('Package import successful')"
                '''
            }
        }

        stage('Test Flask App') {
            steps {
                sh '''
                    . venv/bin/activate
                    export FLASK_APP=app.py
                    flask run --host=0.0.0.0 --port=5000 &
                    APP_PID=$!
                    echo "Waiting for Flask to start..."
                    sleep 10
                    curl -f http://localhost:5000
                    kill $APP_PID
                '''
            }
        }
    }
}
