
import boto3
import requests


def upload_image_to_s3(image_url, bucket_name, s3_file_name):
	print("Creating S3 client..")
	s3 = boto3.client('s3')
	response = requests.get(image_url)

	if response.status_code == 200:
		s3.put_object(Bucket=bucket_name, Key=s3_file_name, Body=response.content)
		print(f"Uploaded {s3_file_name} to {bucket_name}.")
	else:
		print("Failed to retrieve the image.")

image_url = "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg"

bucket_name = "serverlessmovies"
s3_file_name = "The Shawshank Redemption.jpg"

upload_image_to_s3(image_url, bucket_name, s3_file_name)
