import boto3
import logging
import json
import datetime 


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AWS_REGION = 'ap-south-1'

class EC2Manager:
    def create_snapshot(self, env, ec2_resource, volume_id, snapshot_name, snapshot_description, purpose):
        ec2_resource = boto3.resource('ec2')
        snapshot = ec2_resource.create_snapshot(VolumeId=volume_id, Description=snapshot_description)
        snapshot.create_tags()