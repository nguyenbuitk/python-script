'''
Scheduling EC2 instance, start at 9AM and stop at 6PM
Condition: Instance with tag key="type" and value="scheduled"
Condition: Mon - Fri

Steps: 
    1. IAM of lambda for Cloudwatch logs and EC2 full permission
    2. Write lambda function
    3. Add trigger of lambda function
'''

# Define your AWS credentials and region
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION_NAME'

# Define the EC2 client
# ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)


import boto3
ec2 = boto3.client('ec2', region_name = 'ap-southeast-1')
instances = ec2.describe_instances(
    Filter=[
         {
             "Name": "tag:Type",
             "Values": "Scheduled"
         }
    ]
)



ec2.stop_instances(InstanceIds=instances)