import json
import boto3
from boto3.dynamodb.conditions import Key
import os

#Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def get_movies(event, context):
	try:
		response = table.scan()
		movies = response.get('Items', [])
		return {
			'statusCode': 200,
			'body': json.dumps(movies),
			'headers': {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*'
			}
		}
	except Exception as e:
		return {
			'statusCode': 500,
			'body': json.dumps({'error': str(e)}),
			'headers': {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*'
			}
		}

def get_movies_by_year(event, context):
	try:
		year = event['pathParameters']['year']
		response = table.scan(
			FilterExpression=Key('releaseYear').eq(year)
		)
		movies = response.get('Items', [])
		return {
			'statusCode':200,
			'body': json.dumps(movies),
			'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
		}
			
	
	except Exception as e:
		return {
			'statusCode': 500,
			'body': json.dumps({'error': str(e)}),
			'headers': {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*'
			}
	}


def get_movies_by_summary(event, context):
	try:
		title = event['pathParameters']['title']
		response = table.get_item(
			Key={'title': title}
		)
		movie = response.get('Item')
		if not movie:
		return {
			'statusCode': 404,
			'body': json.dumps({'error': 'Movie not found'}),
			'headers': {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*'
			}
		}

	generated_summary = f"A summary for the movie {title}."
	movie['generatedSummary'] = generated_summary

	return {
		'statusCode': 200,
		'body': json.dumps(movie),
		'headers': {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*'
		}
	}



	except Exception as e:
		return {
			'statusCode': 500,
			'body': json.dumps({'error': str(e)}),
			'headers': {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*'
			}
		}		
