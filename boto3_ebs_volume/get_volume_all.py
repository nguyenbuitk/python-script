import boto3
AWS_REGION = 'ap-south-1'
# def get_volume_by_id(ec2_resource, volume_id):


def get_all_volume(ec2_resource):
    for volume in ec2_resource.volumes.all():
        print(volume)

def get_all_volume_2(ec2_resource):
    volumes = ec2_resource.Volm

def main():
    ec2_resource = boto3.resource('ec2', region_name = AWS_REGION)
    get_all_volume(ec2_resource)
    # print(volumes)

if __name__ == "__main__":
    main()