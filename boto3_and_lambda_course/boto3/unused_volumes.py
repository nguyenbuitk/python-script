# This script send list of unused volume to email

import boto3

AWS_REGION = 'ap-southeast-1'
ec2_client = boto3.client('ec2', region_name = AWS_REGION)
sns_client = boto3.client('sns', region_name = AWS_REGION)

volumes = ec2_client.describe_volumes() # return dict
unused_volumes = []

for volume in volumes['Volumes']:
    if len(volume["Attachments"]) == 0:
        # volumes["Attachments"] is dic
        unused_volumes.append(volume)

message = "##### List of unused volumes ##### \n"

for volume in unused_volumes:
    print(volume)
    message = message + volume["VolumeId"] + "\n"
    print("----------"*5)

response = sns_client.publish(
    TopicArn = "arn:aws:sns:ap-southeast-1:028668155772:eventbridge-demo",
    Message = message,
    Subject = "list unused volume"
)