import plotly.express as px
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '<hostname>', 'port': 9200}])
result = es.search(index="data", body={"query": {"match_all": {}}})
value = result['hits']['hits'][0]['_source']['value']

### height of the first section represents the
#   input value and the height 
#   of the second section represents the remaining value. 

fig = px.funnel(
    values=[value, 100-value],
    title='Gauge',
    labels=['Value', 'Remaining']
)
fig.show()