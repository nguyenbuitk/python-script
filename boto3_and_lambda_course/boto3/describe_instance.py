import boto3
client = boto3.client('ec2', region_name = 'ap-south-1')
resp = client.describe_instances(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": ['dev-ovng-poc-*', 'dev-ovng-poc2-*']
        }
    ]
)

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        # Find the 'Name' tag
        instance_name = ""
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break
        if instance_name == "":
            instance_name = "No Name Tag"

        # Print instance details
        print("instanceName: {}, instanceId: {}, state: {}".format(
            instance_name,
            instance['InstanceId'],
            instance['State']['Name']
        ))