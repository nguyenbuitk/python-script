import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 24, 34],
    'City': ['New York', 'LA', 'Chicago', 'Houston'],
    'Score': [85, 90, 78, 88]
}

df = pd.DataFrame(data)

# Bar Plot
fig_bar = px.bar(df, x='Name', y='Score', title='Scores by Name')
fig_bar.show()