import csv

# Data structured as a list of dictionaries
data = [
    {
        "MSP id": "64ec5084ecec4252c3de11fb",
        "MSP name": "OVNG-PT-TMA Thailand's MSP",
        "Org id": "650163f8a38d2f2d8d011531",
        "Org name": "Backup_Restore",
        "Site id": "650163f8a38d2f78f3011535",
        "Site name": "Unnamed site",
        "WaitingForFirstContact": 1
    },
    {
        "MSP id": "64ec5084ecec4252c3de11fb",
        "MSP name": "OVNG-PT-TMA Thailand's MSP",
        "Org id": "64ec5084ecec42502cde11fc",
        "Org name": "OVNG-PT-TMA",
        "Site id": "64ec5084ecec4279d7de11fd",
        "Site name": "Unnamed site",
        "WaitingForFirstContact": 2
    },
    {
        "MSP id": "64ec5084ecec4252c3de11fb",
        "MSP name": "OVNG-PT-TMA Thailand's MSP",
        "Org id": "64ec5084ecec42502cde11fc",
        "Org name": "OVNG-PT-TMA",
        "Site id": "65b1e3b57a03a0ec03f85f56",
        "Site name": "ANH",
        "WaitingForFirstContact": 3
    }
]

# Specify the CSV file name
csv_file = 'msp_data.csv'

# Get the headers from the keys of the first dictionary
headers = data[0].keys()

# Write data to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print(f"Data successfully written to {csv_file}")

