from elasticsearch import ElasticSearch
es = ElasticSearch("http://localhost:9200/")
res = es.get(index="order_item_local", doc_type='items', id=1)
print res['_source']
