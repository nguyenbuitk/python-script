import json
from datetime import date, datetime
import boto3
AWS_REGION = 'ap-south-1'
EC2_CLIENT = boto3.client('ec2', region_name = AWS_REGION)

def json_datetime_serilizer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

describe_response = EC2_CLIENT.describe_volumes(
    VolumeIds=[
        'vol-09d8f1a3742c3b352'
    ]
)

print('Volumes information:')
print(json.dumps(
    describe_response,
    indent=4,
    default=json_datetime_serilizer
))