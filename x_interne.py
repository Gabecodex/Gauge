import plotly.express as px
import json

with open("Data.json", 'r') as f:
    data = json.load(f)


with open("json.json") as f:
    data = json.load(f)

value = data['Value']

fig = px.funnel(
    values=[value, 100-value],
    title='Gauge',
    labels=['Value', 'Remaining']
)
fig.show()
