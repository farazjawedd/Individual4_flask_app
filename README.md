# Text Summarization with bart
[![CI](https://github.com/farazjawedd/python-template-ids706/actions/workflows/cicd.yml/badge.svg)](https://github.com/farazjawedd/python-template-ids706/actions/workflows/cicd.yml)

Demo video: xxxxxxxx

## Project Overview

This project focuses on building an auto-scaling Flask application hosted on Azure, incorporating BART (Bidirectional and Auto-Regressive Transformers) for text summarization. Users can input text, specify minimum and maximum tokens for summarization, and receive a summarized output. The application is containerized using Docker and deployed on Azure Web App Service.


## Requirements

### Dependencies
- Python
- Flask
- Docker
- Azure Account with App Services

## The Web App

Link: 

### Project Structure

### `/summarizer_app`

This directory contains the core components of the Flask application:

- **`/summarizer_app/app.py`**: The main Flask application file responsible for handling routes and user interactions.

- **`/summarizer_app/app_logic.py`**: The logic module where BART text summarization is implemented. This file holds the essential functionality of the summarization process.

- **`/summarizer_app/templates`**: This directory houses HTML templates for the frontend. These templates define the structure and layout of the user interface.

- **`/summarizer_app/static`**: CSS files reside here, providing styles for the frontend, ensuring an aesthetically pleasing user experience.

-  `/summarizer_app/Dockerfile`**: The file which dockerizes the entire app and makes it easy to host and deploy it.

This directory encompasses Docker configuration files, enabling the containerization of the application for easy deployment and scalability.












-------------


The Github Action workflow and pipeline has the following:

- Dockerfile for containerization
- .devcontainer.json for Visual Studio Code development containers
- Makefile for common project tasks
- requirements.txt for managing dependencies
- main.py for your project code
- test_main.py for testing your code

## Getting Started

1. Clone this repository to your local machine.
2. Install Python 3.x on your system.
3. (Optional) Install Docker for containerization.
4. (Optional) Install Visual Studio Code with the "Remote - Containers" extension.

## Usage

- Run your project's `main.py` script using Python.
- Test your code with the provided `test_main.py` script.
- Use the Makefile commands for common tasks, e.g., `make install-dependencies`, `make run`, `make test`.

- This also includes a docker container for running your scripts on a virtual envt. 
