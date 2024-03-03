import boto3
client = boto3.client('ec2', region_name = 'ap-south-1')

resp = client.terminate_instances(InstanceIds=['i-05ef5fe1130ed6cbb'])

for instance in resp['TerminatingInstances']:
    print("Instance {} is terminated".format(instance['InstanceId']))