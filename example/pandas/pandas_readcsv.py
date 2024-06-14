import os
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'data.csv')
df_csv = pd.read_csv(csv_file_path)

print(df_csv)