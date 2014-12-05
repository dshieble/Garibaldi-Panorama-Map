#!/usr/bin/python

import  json

with open('../static/data/data_by_location.json','w') as infile:
	with open('../static/data/data_by_book.json.json','w') as out_file:
		old_json_data = json.load(infile)
		json_data = {'rows':[]}
		for r in old_json_data['rows']:
			for book in r["properties"]["books"]:
				d = book
				d["location"] = {}
				d["location"]["geometry"] = r["geometry"]
				d["location"]["name"] = r["properties"]["name"]
				d["location"]["type"] = r["properties"]["type"]
				d["location"]["scenes"] = r["properties"]["scenes"]
				json_data["rows"].append(d)


