import argparse

def main():
    '''
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Script to manage cloud instances.")

    # Define arguments
    parser.add_argument("-e", "--env", choices=['prod', 'preprod', 'dev'], required=True, help="Environment (prod, preprod, dev)")
    parser.add_argument("-r", "--region", choices=['ap-southeast-1', 'ap-south-1', 'us-east-1'], required=True, help="Region (ap-southeast-1, ap-south-1, us-east-1)")
    parser.add_argument("-i", "--instanceid", required=True, help="ID of the instance")

    # Parse arguments
    args = parser.parse_args()

    # Use the parsed arguments
    print(f"Environment: {args.env}")
    print(f"Region: {args.region}")
    print(f"Instance ID: {args.instanceid}")

    # Rest of the script logic goes here
    '''
    description_message = '''
    Description: Get all devices with ovManaged and assigned status
    Example: python3 %(prog)s -e dev\n
    '''
    parser = argparse.ArgumentParser(description=description_message, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-e", "--environment", help="environment: dev, prod, etc.", required=True)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', dest='data_center_region', action='store',
        choices=['ap-southeast-1', 'ap-south-1', 'ca-central-1', 'eu-central-1', 'us-east-1'],
        metavar=('data_center_region_name'), 
        help='(Optional) The data center region name')
    group.add_argument('-o', dest='ov_ids', action='append', metavar=('ov_instance'), help='(Optional) OV instance ID')

    args = parser.parse_args()
    env = args.environment

if __name__ == "__main__":
    main()