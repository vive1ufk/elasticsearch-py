from elasticsearch import Elasticsearch
from elasticsearch.helpers import reindex

es = Elasticsearch("http://spff-esmaster-apollo-0001.nm.flipkart.com:9200")
reindex(es, "order_item_v1", "order_item_v2")
