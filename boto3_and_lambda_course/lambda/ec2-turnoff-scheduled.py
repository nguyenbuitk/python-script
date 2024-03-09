import boto3

ec2_client = boto3.client('ec2', region_name = "ap-southeast-1")

instances = ec2_client.describe_instances(
    Filters=[
        {
            "Name": "tag:Type",
            "Values": ['Scheduled']
        }
    ]
)

instanceID = []
for instance in instances['Reservations']: 
    instanceID.append(instance['Instances'][0]['InstanceId'])

ec2_client.stop_instances(
    InstanceIds = instanceID
)