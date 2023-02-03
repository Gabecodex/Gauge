# Local Database
import plotly.express as px
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
result = es.search(index="data", body={"query": {"match_all": {}}})
value = result['hits']['hits'][0]['_source']['value']

fig = px.funnel(
    values=[value, 100-value],
    title='Gauge',
    labels=['Value', 'Remaining']
)
fig.show()