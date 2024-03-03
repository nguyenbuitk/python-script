import boto3

##########################
## Part-1 Create Images ##
##########################
source_region = 'ap-south-1'
ec2 = boto3.resource('ec2', region_name=source_region)

instances = ec2.instances.filter(InstanceIds=['i-00f6041e139226c79'])
image_ids = []

for instance in instances:
    image = instance.create_image(Name = 'Demo boto3 - {}'.format(instance.id), Description='Demo Boto ' + instance.id)
    image_ids.append(image.id)

print("Images to be copied {} ".format(image_ids))

############################################
## Part-2 Wait For Images to be available ##
############################################
# Get waiter for image_available
client = boto3.client('ec2', region_name=source_region)
waiter = client.get_waiter('image_available')

waiter.wait(Filters=[{
    'Name': 'image-id',
    'Values': image_ids
    }
])

print("Done for {} ".format(image_ids))


#########################################
## Part-3 Copy Images to otehr regions ##
#########################################
# Copy Images to the region, us-east-1
destionation_region = 'us-east-1'
client = boto3.client('ec2', region_name = destionation_region)
for image_id in image_ids:
    client.copy_image(Name='Boto3 Copy'+image_id, SourceImageId=image_id, SourceRegion='ap-south-1')
