from setuptools import setup, find_packages

setup(
    name='python-nexus-app',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests'
    ],
)
