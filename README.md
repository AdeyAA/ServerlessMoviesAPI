# ServerlessMoviesAPI


##  Description:

	- The **Serverless Movies API** is a cloud-based application designed to provide movie information through a set of serverless functions. This API allows users to retrieve a list of movies, filter movies by release year, and access AI-generated summaries for specific movies. This project uses AWS services such as DynamoDB for data storage, S3 for image hosting , and Lambda for serverless functions.


## Features

- **Get Movies**: Returns a JSON list of all movies stored in the database, including titles, release years, genres, and cover image URLs.

- **Get Movies by Year**: Retrieves a list of movies released in a specified year.

- **Get Movie Summary**: Returns an AI-generated summary for a specified movie. 



## API Endpoints

- 






## Getting Started

- Prerequisites
	- AWS Account
	- AWS CLI installed and configured
	-Python 3.x
	-Python packages (see requiremnets.txt)

- Installation
	- Clone the repository and change into the directory:
	`git clone https://github.com/AdeyAA/ServerlessMoviesAPI.git`
	`cd ServerlessMoviesAPI`
	
	- Install Dependencies:
	`pip install -r requirements.txt

- Setting up AWS resources
	- Create IAM User: Make sure that you have an IAM user that has the necessary permissions for DynamoDB, S3, Lambda, and API Gateway

- Create DynamoDB Table: Use the provided Python script to set up the DynamoDB table for storing movie data.

- Upload Movie Data: Prepare your movie data (csv/json) and upload it to the DynamoDB table.

- Store Images in S3: Upload a movie cover imagess to an S3 bucket.

- Deploy Serverless Functions: Deploy the serverless functions using AWS Lambda


## Acknowledgments
 -  https://aws.amazon.com/documentation/
 -  https://www.serverless.com/


