
# Weather Forecast App with GitHub Actions and Docker

## Overview
The Weather Forecast App is a Python-based GUI application that provides weather updates for a given city. It fetches real-time weather data using an API and displays it in a user-friendly interface. This project also includes a CI/CD pipeline using GitHub Actions to automate building and pushing a Docker image to Docker Hub.

## Features
- Fetches real-time weather data for any city
- User-friendly graphical interface (Tkinter-based GUI)
- Automated build and deployment using GitHub Actions
- Containerized application using Docker

## Requirements
- Python 3.9 (Main programming language)
- Tkinter (GUI framework)
- Requests (For API calls)
- Docker (Containerization)
- GitHub Actions (CI/CD automation)

## Setup Instructions
- Clone the repository:
```bash
 git clone https://github.com/NainaGhosh01/GitHub-Action-Weather_Forecast-app.git
 cd GitHub-Action-Weather_Forecast-app 
```
- Install Dependencies
```bash
  pip install -r requirements.txt 
```
- Run the game:
```bash
  python main.py  
```
## Docker Setup
- Build Docker Image
```bash
   docker build -t nainaghosh/weather-app:latest .
```
- Run the Docker Container
```bash
   docker run -it --rm nainaghosh/weather-app
```
## GitHub Actions CI/CD Workflow
This project uses GitHub Actions to automate the build and push of the Docker image to Docker Hub.
### Workflow Steps:
- Trigger: Push or pull request to the main branch
- Build Docker Image
- Login to Docker Hub
- Push Docker Image to Docker Hub

