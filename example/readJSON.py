import json
from pprint import pprint

def readJSON(file_path):
    """_summary_

    Args:
        file_path (_type_): _description_
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("Data read from JSON file:")
        pprint(data)
        return data
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    json_data = readJSON('data.json')

if __name__ == "__main__":
    main()