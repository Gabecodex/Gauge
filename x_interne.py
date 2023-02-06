import plotly.graph_objects as go
import pandas as pd

df = pd.read_json('Data.json')

print( df.info(verbose= True) )
print(df)


df['value'] = df['value'].astype(float)


fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = df.value[3],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed"}))

fig.show()

