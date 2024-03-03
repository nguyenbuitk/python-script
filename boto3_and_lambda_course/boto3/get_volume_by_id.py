# using service-resource/volume: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/index.html
# using resource/volume: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/index.html
import boto3
AWS_REGION = 'ap-south-1'

def get_volume_by_id_using_service_resource(ec2_resource, volume_ids):
    for volume in ec2_resource.volumes.filter(
        VolumeIds = volume_ids,
        ):
        print(f'Volume {volume.id} ({volume.size} GiB) -> {volume.state}')

def get_volume_by_id_using_resource(ec2_resource, volume_id):
    volume = ec2_resource.Volume(volume_id)
    print(volume)
    return volume

def main():
    ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)
    # volume_ids =['vol-0b92297eb02dfccc7', 'vol-09a5d6f5d551899eb']
    # get_volume_by_id_using_service_resource(ec2_resource, volume_id)

    volume_id = 'vol-0b92297eb02dfccc7'
    get_volume_by_id_using_resource(ec2_resource, volume_id)
    # output: 
    # ec2.Volume(id='vol-0b92297eb02dfccc7')
if __name__ == "__main__":
    main()
