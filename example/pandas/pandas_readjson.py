import os
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_directory, 'data.json')

df_json = pd.read_json(json_file_path)
print(df_json)