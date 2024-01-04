import boto3
AWS_REGION = 'ap-south-1'
ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)
for volume in ec2_resource.volumes.filter(
    VolumeIds=[
        'vol-0453eb5c7b0d0350c',
    ],
    ):
    print(f'Volume {volume.id} ({volume.size} GiB) -> {volume.state}')
