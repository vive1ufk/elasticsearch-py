from elasticsearch import Elasticsearch
from elasticsearch.helpers import reindex
from datetime import date, timedelta
import datetime

def getNextDate(dt):
	return dt + timedelta(1)

def getPrevDate(dt):
	return dt - timedelta(1)

def convertStrToDate(strdt):
	arrdt = strdt.split("-")
	return datetime.date(day=arrdt[2], month=arrdt[1], year=arrdt[0])

def getQueryForDate(x):
	ds = str(x)
	de = str(getNextDate(x))
	c = {}
	c['gte'] = ds + "T00:00:00.000+05:30"
	c['lt'] = de + "T00:00:00.000+05:30"
	r = {}
	r['created_at'] = c
	q = {}
	q['range'] = r
	query = {}
	query['query'] = q
	return query

es = Elasticsearch("http://spff-es-apollo-0001.stage.ch.flipkart.com:9200")

start_at = datetime.date(day=15, month=7, year=2015)
end_at = datetime.date(day=10, month=3, year=2015)

cur_at = start_at
while str(end_at) != str(cur_at):
	print "processing for date - ", str(cur_at)
	reindex(es, "order_item_v1", "order_item_v2", getQueryForDate(cur_at))
	cur_at = getPrevDate(cur_at)
