import json
import boto3

dynamodb = boto3.resource('dynamodb')

def get_movies(event, context):
	table = dynamodb.Table('Movies')
	response = table.scan()
	movies = response['Items']

	return {
		'statusCode': 200,
		'body': json.dumps(movies)
	}


def get_movies_by_year(event, context):
	year = event['pathParameters']['year']
	table = dynamodb.Table('Movies')
	response = table.scan(FilterExpression=boto3.dynamodb.conditions.Attr('releaseYear').eq(year))
	movies = response['Items']

	return {
		'statusCode': 200,
		'body': json.dumps(movies)
	}



def get_movie_summary(event, context):
	title = event['pathParameters']['title']
	table = dynamodb.Table('Movies')
	response = table.get_item(Key={'title': title})
	movie = response.get('Item')

	if movie:
		generated_summary = f"A summary for {title}."   #Placeholder for summary
		movie['generatedSummary'] = generated_summary
		return {
			'statusCode': 200,
			'body': json.dumps(movie)
		}
	else:
		return {
			'statusCode': 404, 
			'body': json.dumps({"error": "Movie not found"})
		}
		
