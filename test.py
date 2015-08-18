from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
res = es.get(index="order_item_local_v1", doc_type='items', id=1)
#es.indices.create(index='my-index', ignore=400)
#es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": "123"})
#res = es.get(index="my-index", doc_type="test-type", id=42)['_source']
print res
