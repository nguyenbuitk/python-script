responses = {  # dict
    'Reservations': [ # list
        {               # dict 
            'Instances': [  # list
                {              # dict 
                    'InstanceId': 'i-1234567890abcdef0',
                    'InstanceType': 't2.micro',
                    'LaunchTime': '2021-01-01T00:00:00.000Z',
                    'State': {
                        'Name': 'running'
                    },
                    'Tags': [
                        {'Key': 'Name', 'Value': 'MyServer'}
                    ]
                },
                {
                    'InstanceId': 'i-0abcdef1234567890',
                    'InstanceType': 't2.small',
                    'LaunchTime': '2021-01-02T00:00:00.000Z',
                    'State': {
                        'Name': 'stopped'
                    },
                    'Tags': [
                        {'Key': 'Name', 'Value': 'MyOtherServer'}
                    ]
                }
            ],
            'OwnerId': '123456789012'
        }
    ]
}

# Accessing elements
for response in responses['Reservations']: 
    for instance in response['Instances']:
        print("Instance ID: {}, state: {}".format(instance['InstanceId'],instance['State']['Name']))
