import boto3
AWS_REGION = "ap-south-1"
ec2_client = boto3.client('ec2', region_name = AWS_REGION)
new_volume = ec2_client.create_volume(
    AvailabilityZone=f'{AWS_REGION}b',
    Size=10,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'hands-ond-cloud-ebs-boto3'
                }
            ]
        }
    ]
)
print(f'Create volume ID: {new_volume["VolumeId"]}')