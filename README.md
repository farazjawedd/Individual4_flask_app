# Text Summarization with bart
[![CiCd](https://github.com/farazjawedd/Individual4_flask_app/actions/workflows/cicd.yml/badge.svg)](https://github.com/farazjawedd/Individual4_flask_app/actions/workflows/cicd.yml)

Link to youtube video: https://www.youtube.com/watch?v=r9K6ZB45f6s

## Project Overview

This project focuses on building an auto-scaling Flask application hosted on Azure, incorporating BART (Bidirectional and Auto-Regressive Transformers) for text summarization. Users can input text, specify minimum and maximum tokens for summarization, and receive a summarized output. The application is containerized using Docker and deployed on Azure Web App Service.


## Requirements

### Dependencies
- Python
- Flask
- Docker
- Azure Account with App Services

## The Web App

Link: https://gsummarizer.azurewebsites.net/

### Project Structure

### `/summarizer_app`

This directory contains the core components of the Flask application:

- **`/summarizer_app/app.py`**: The main Flask application file responsible for handling routes and user interactions.

- **`/summarizer_app/app_logic.py`**: The logic module where BART text summarization is implemented. This file holds the essential functionality of the summarization process.

- **`/summarizer_app/templates`**: This directory houses HTML templates for the frontend. These templates define the structure and layout of the user interface.

- **`/summarizer_app/static`**: CSS files reside here, providing styles for the frontend, ensuring an aesthetically pleasing user experience.

- ** `/summarizer_app/Dockerfile`**: This file encompasses Docker configuration, enabling the containerization of the application for easy deployment and scalability.


## Features:

Homepage (default):
<img width="938" alt="Screenshot 2023-12-10 at 5 47 20 PM" src="https://github.com/farazjawedd/Individual4_flask_app/assets/101464414/7362f01f-d726-47dd-97bc-66340434d252">

This page allows you to enter text and specify how long you want the summary to be.

Let's summarize some text:
<img width="884" alt="Screenshot 2023-12-10 at 5 48 35 PM" src="https://github.com/farazjawedd/Individual4_flask_app/assets/101464414/adc2102d-ce85-4893-b34b-c57f8a60e76d">

Summary page:
<img width="912" alt="Screenshot 2023-12-10 at 5 49 04 PM" src="https://github.com/farazjawedd/Individual4_flask_app/assets/101464414/931f9295-9972-44f9-807c-4fc15ce181de">


Error handling is also done here which returns an error if you don't enter any text.

## Use of Dockerhub

The app was containerized using docker and the image was put on public on dockerhub:

<img width="971" alt="Screenshot 2023-12-10 at 5 50 16 PM" src="https://github.com/farazjawedd/Individual4_flask_app/assets/101464414/f976a583-b9c9-4855-92e4-fb2fcfa5dfaf">

## Hosted on Azure

In order for the app to be scaleable and used by multiple users at the same time, I deployed this app using Azure. 

Here are the screenshots for it:

<img width="1463" alt="Screenshot 2023-12-10 at 5 52 25 PM" src="https://github.com/farazjawedd/Individual4_flask_app/assets/101464414/60e52d1c-b485-46eb-85df-caf07e43af0f">

The scale plan:

<img width="1293" alt="Screenshot 2023-12-10 at 5 52 44 PM" src="https://github.com/farazjawedd/Individual4_flask_app/assets/101464414/7d35088f-7ab6-4bfc-a39a-c9639e58ad7b">



## Usage

This auto-scaling Flask app simplifies text summarization using BART, providing an intuitive user experience. Follow these steps to harness its capabilities:

1. **Access the App:**
   Open the application in your web browser at `http://gsummarizer.azurewebsites.net/` or on your local host port `8080` after running the Docker container incase you clone this repository.

2. **Input Text:**
   Enter the text you wish to summarize in the designated input field.

3. **Specify Token Parameters:**
   Tailor your summary by indicating the minimum and maximum tokens desired. This allows you to control the length and depth of the summarization.

4. **Initiate Summarization:**
   Click the "Summarize" button to trigger the BART summarization process. Witness the application's efficiency in distilling complex text into concise summaries.

5. **Review Results:**
   The summarized output will be displayed on the webpage, providing you with a clear and digestible version of the original text.

6. **Experiment and Refine:**
   Feel free to experiment with different texts, token parameters, and summarization scenarios. Refine your usage to match specific content types and summarization needs.

7. **Explore Docker and Azure Deployment:**
   For a broader experience, explore deploying the app using Docker and Azure Web App. Evaluate its scalability and accessibility in a production environment.

8. **Share and Collaborate:**
   Share your summarized content or collaborate with others by demonstrating the app's functionalities. Encourage exploration and feedback within the user community.

By following these usage instructions, you can seamlessly harness the power of BART text summarization through a user-friendly interface, making complex information more accessible and manageable.


-------------


The Github Action workflow and pipeline has the following:

- Dockerfile for containerization
- .devcontainer.json for Visual Studio Code development containers
- Makefile for common project tasks
- requirements.txt for managing dependencies
- main.py for your project code
- test_main.py for testing your code

This project passes the Github Workflow and CICD Pipeline.

## Getting Started

1. Clone this repository to your local machine.
2. Install Python 3.x on your system.
3. Run the app.py in the summarizer_app folder.
4. You can give out any port from your computer or run the dockerized version.

- This also includes a docker container for running your scripts on a virtual envt. 
