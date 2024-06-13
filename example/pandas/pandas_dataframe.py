import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 24, 34],
    'City': ['New York', 'LA', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

print(df)