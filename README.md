# IDS 706 Individual Project 4 [![CI](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-4/actions/workflows/cicd.yml)

[https://interviewq.azurewebsites.net](url)

## Overview
* This repository includes the components for Individual Project 4 - Auto Scaling Flask App Using Serverless Platform

## Goal
* Build and deploy a scaleable **web-hosted app** that **generates interview questions** for data science students, powered by GPT 3.5 Turbo
* Build a publicly accessible **auto-scaling container** using Azure App Services and Flask

## Key Components in the Repo:
* app.py (Python script for the Flask web app)
* templates/index.html (hidden, the HTML template for the app UI)
* Dockerfile (provided to containerize the Flask app)
* OpenAI API (provides the functionality for text generation)
* Makefile
* devcontainer
* requirements.txt
* GitHub Actions

## App Introduction
The web app that I built, **InterviewQ**, has the following features:
* A **'Behavioral Question'** button to generate a new behavioral interview question
* A **'Technical Question'** button to generate a new technical interview question
* A **textbox** for displaying the generated text from the OpenAI API
* Users can keep generating new questions to help them get practiced on a variety of scenarios
* The GPT model has been meticulously fine-tuned to replicate the role of a recruiter from a top-tier tech company, enhancing the relevance and authenticity of the generated interview questions to closely resemble those used in actual interview settings
  
## Key Steps
1. Git clone the repo, the environment will automatically be set up with necessary dependencies installed
2. Get an OpenAI API key from their website, create an `.env` file and put in `OPENAI_API_KEY=<insert api key>`
3. Use the following command to build the docker image and launch the app on a locally hosted website using port 5000
```
docker build interviewq
docker run -p 5000:5000 myapp
```
4. Use the following command to log into DockerHub and push to your container
```
docker login --<username>
docker build -t <username>/<repo> .
docker push <username>/<repo>
```
5. Create a new app service on Azure, select Docker Container and deploy the DockerHub image
6. Navigate to **Configuration** -> **Application Settings**, and add `WEBSITES_PORT` with a value of 5000, and `OPENAI_API_KEY` with your personal key
7. You should be able to launch your web app using the domain provided on Azure
