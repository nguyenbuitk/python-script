import sys
import os
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

script_file_name = str(os.path.basename(__file__)).split('.')[0].strip()
path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),"cfg","config."+env+".json")


print("Script File Name:", script_file_name)