# CI/CD Pipeline Demo App

This project demonstrates a **full CI/CD pipeline** using GitHub Actions, Docker, and AWS EC2.

## Project Overview

This is a small FastAPI app that returns a JSON response. The main goal of this project is to demonstrate a **fully automated CI/CD pipeline**:

* Code is tested automatically on push to GitHub
* Docker image is built and pushed to DockerHub
* The EC2 instance automatically pulls the new image and runs the container
* The app is live and accessible in a browser

## Features

* FastAPI backend app returning JSON
* Unit tests with `pytest`
* Dockerized for consistent deployment
* Automated CI/CD using GitHub Actions
* Live deployment on AWS EC2

## Tech Stack

* Python 3.12, FastAPI
* Docker & DockerHub
* GitHub Actions
* AWS EC2

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ci-cd-pipeline-demo

```
### 2. Local Setup

Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
# Install dependencies

pip install -r requirements.txt
```bash
# Run tests
pytest app/test_app.py -v
```
### 3. Docker
# Build Docker container
```bash
docker build -t ci-cd-demo-app:latest .
```
# Run Docker container locally
```bash
docker run -d -p 8000:8000 --name demo-app ci-cd-demo-app:latest
```
# Test the app in your terminal
```bash
curl http://localhost:8000
```

CI/CD Deployment
The GitHub Actions workflow performs the following on every push to the main branch:

* Setup Python & install dependencies

* Run tests (pytest)

* Build Docker image and push to DockerHub

* SSH into EC2, stop/remove the old container, pull the latest image, and run the new container

GitHub Secrets Required
* You will need to add the following secrets to your GitHub repository for the pipeline to work:

* DOCKER_USERNAME: Your DockerHub username

* DOCKER_PASSWORD: Your DockerHub Personal Access Token

* EC2_HOST: The public IP or hostname of your EC2 instance

* EC2_USER: The EC2 SSH user (e.g., ubuntu)

* EC2_SSH_KEY: The private key for SSH (add this as a multiline secret


<img width="2420" height="1250" alt="Screenshot from 2025-09-27 19-03-17" src="https://github.com/user-attachments/assets/36f9e500-c36f-423f-b30f-bf3d9fc9e343" />

<img width="1810" height="424" alt="Screenshot from 2025-09-27 19-02-42" src="https://github.com/user-attachments/assets/d4f64a19-2205-4974-8b0b-c5aded2504b0" />
<img width="2402" height="1136" alt="Screenshot from 2025-09-27 19-00-58" src="https://github.com/user-attachments/assets/8038beb4-1b05-48f0-a462-17a1c3c4c7e9" />



