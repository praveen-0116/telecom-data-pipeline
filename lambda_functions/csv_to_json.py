import json
import csv
import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket and file info from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download file from S3
    download_path = f"/tmp/{os.path.basename(key)}"
    upload_path = f"/tmp/{os.path.splitext(os.path.basename(key))[0]}.json"
    
    s3.download_file(bucket, key, download_path)

    # Convert CSV → JSON
    with open(download_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
    
    with open(upload_path, 'w') as json_file:
        json.dump(rows, json_file, indent=4)

    # Upload JSON back to S3
    json_key = f"processed/{os.path.splitext(key)[0]}.json"
    s3.upload_file(upload_path, bucket, json_key)

    return {
        'statusCode': 200,
        'body': f"Successfully converted {key} to {json_key}"
    }
