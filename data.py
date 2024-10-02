import boto3


#Initalize AWS resources

dynamodb = boto3.resource('dynamodb')

def insert_movie(title, release_year, genre, cover_url):
	table = dynamodb.Table('Movies')
	table.put_item(
		Item={
			'titile': title,
			'releaseYear': release_year,
			'genre': genre,
			'coverUrl': cover_url
		}
	)
	print(f"Movie '{title}' inserted into DynamoDB.")

if __name__ == "__main__":

	#Add movies here.....
