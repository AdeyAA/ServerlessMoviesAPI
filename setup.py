import boto3


#Initialize resources from AWS
dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')

#Create a DynamoDB table
def create_dynamodb_table():
	table = dynamodb.create_table(
		TableName='Movies',
		KeySchema=[
			{
				'AttributeName': 'title',
				'KeyType': 'HASH'  #Partition key
			}
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'title',
				'AttributeType': 'S'   #String type
			}
		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 5,
			'WriteCapacityUnits': 5
		}
	)
	table.wait_until_exists()
	print("DynamoDB table created.")



#Create an S3 bucket

def create_s3_bucket(bucket_name):
	s3.create_bucket(Bucket=bucket_name)
	print(f"S3 bucket '{bucket_name}' created.")

if __name__ == "__main__":
	create_dynamodb_table()
	create_s3_bucket('serverlessmovieapi')
