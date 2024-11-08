import boto3
import json


def populate_dynamodb():

	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('Movies')

	with open('movies.json') as f:
		movies = json.load(f)
	
	with table.batch_writer() as batch:
		for movie in movies:
			batch.put_item(Item=movie)

	print("DynamoDB table populated successfully.")

if __name__ ==  "__main__":
	populate_dynamodb()
