import json
import boto3

event = {
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "csv-s3-lambda-dynamodb",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::example-bucket"
        },
        "object": {
          "key": "test.csv",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb', region_name = "ap-southeast-1")
table = dynamodb.Table('employees')

def lambda_handler(event):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]    
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)

    data = resp['Body'].read().decode('utf-8')
    print("resp type: ", type(resp))
    print("resp['Body'] type: ", type(resp['Body']))
    print("resp['Body'].read() type: ", type(resp['Body'].read()))
    print("resp['Body'].read().decode('utf-8') type: ", type(resp['Body'].read().decode('utf-8')))
    print(data)

    employees = data.split("\n")
    for emp in employees:
        print(emp)
        emp_data = emp.split(",")
        table.put_item(
            Item = {
                "id": emp_data[0],
                "name": emp_data[1],
                "location": emp_data[2]
            }
        )

if __name__ == "__main__":
    lambda_handler(event)