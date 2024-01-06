import boto3
client = boto3.client('ec2', region_name = 'ap-south-1')
resp = client.describe_instances()