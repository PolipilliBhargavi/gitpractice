# DevOps Health Check

## Overview

Python automation tool that verifies the health of a Dockerized Flask application.

## Tech Stack

- Python
- Flask
- Docker
- Requests
- Logging
- Environment Variables
- Subprocess

## Features

✓ Health endpoint
✓ Docker container verification
✓ Logging
✓ Environment variables
✓ Exception handling

## Run

docker build -t flask-app:v1 .

docker run -d -p 5000:5000 flask-app:v1

python health_checker.py