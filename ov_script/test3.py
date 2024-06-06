def process_site(url, org_id, site_id, detail=False):
    # Dummy function to mimic getting devices by site
    def get_devices_by_site(url, org_id, site_id):
        # Example data structure returned by this function
        return {
            'data': [
                {'serialNumber': 'ABC123', 'status': 'ONLINE'},
                {'serialNumber': 'DEF456', 'status': 'OFFLINE'},
                {'serialNumber': 'GHI789', 'status': 'ONLINE'},
                {'serialNumber': 'JKL012', 'status': 'UNKNOWN'},
            ]
        }
    
    # Get devices from the site
    site_devices = get_devices_by_site(url, org_id, site_id)
    
    # Check if 'data' key exists
    if 'data' not in site_devices:
        print("Error: No data found in site_devices")
        return None
    
    site_devices_data = site_devices['data']
    
    # Check if there are no devices
    if not site_devices_data:
        return None
    
    # Dictionary to hold the result
    result = {}
    
    # Set to keep track of unique device statuses
    device_states = set()
    
    # Process each device
    for device in site_devices_data:
        status = device.get('status', 'UNKNOWN')
        device_states.add(status)
        
        if status not in result:
            result[status] = []
        
        result[status].append(device['serialNumber'])
    
    # Prepare the log
    log = "Site ID {}: Device Summary".format(site_id)
    for state in device_states:
        count = len(result[state])
        log += "\n  {}: {} device(s)".format(state, count)
        if detail:
            log += " - Serial Numbers: {}".format(", ".join(result[state]))
    
    # Print the log
    print(log)
    
    return result

# Example usage
url = "http://example.com/api"
org_id = 1
site_id = 101
process_site(url, org_id, site_id, detail=True)
