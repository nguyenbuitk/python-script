import boto3
AWS_REGION = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = AWS_REGION)
volume = ec2_resource.Volume('vol-0453eb5c7b0d0350c')
if volume.state == "available":
    volume.delete()
    print(f'Volume successfully deleted')
else:
    print(f"Can't delete volume attached to EC2 instance")