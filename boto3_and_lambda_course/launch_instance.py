import boto3
client = boto3.client('ec2', region_name='ap-south-1')
resp = client.run_instances(ImageId='ami-03f4878755434977f',
                            InstanceType='t2.micro',
                            MinCount=1,
                            MaxCount=1)

for instance in resp['Instances']:
    print(instance['InstanceId'])