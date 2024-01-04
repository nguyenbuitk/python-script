import boto3
import logging
import json
import datetime 


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AWS_REGION = 'ap-south-1'
def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 
  

class EC2Manager:
    def get_instance_by_description(self, ec2_client, env, description):
        try:
            result = ec2_client.describe_instances(
                Filters=[
                    {'Name': 'tag:Description', 'Values': [description]},
                    {'Name': 'tag:Name', 'Values': ['{}-ovng-*'.format(env)]}
                ]
            )

            # Print result
            print("API call result: ")
            print(json.dumps(result, indent=4, default=serialize_datetime))


        except Exception as e:
            logger.error("\n    Invalid description! Error: {}".format(e))
            return None

        if len(result["Reservations"]) < 1:
            logger.error("\n    Description %s not found" % description)
            return None

        instance = result["Reservations"][0]["Instances"][0]
        return instance
    
def main():
    ec2_client = boto3.client('ec2', region_name = AWS_REGION)
    ec2_manager = EC2Manager()

    env = 'dev'
    description = 'POC hung_bnn'

    instance = ec2_manager.get_instance_by_description(ec2_client, env, description)

    if instance:
        logger.info(f"Instance found: {instance['InstanceId']}")
    else:
        logger.info("No instance found with give description")

if __name__ == "__main__":
    main()
