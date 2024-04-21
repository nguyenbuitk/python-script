import os

folder_path = "diary/"
for filename in os.listdir(folder_path):
    # Check if item is a file
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        # Open the file and read its content
        with open(file_path, "r") as file:
            print(f"File: {filename}")
            print(file.read())
            print("=" * 50)