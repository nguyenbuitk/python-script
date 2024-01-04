import boto3
AWS_REGION = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)
new_volume = ec2_resource.create_volume(
    AvailabilityZone=f'{AWS_REGION}b',
    Size=10,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'hands-on-cloud-ebs-boto3'
                }
            ]
        }
    ]
)
print(f'Created volume ID: {new_volume.id}')
