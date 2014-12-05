#!/usr/bin/python

import  json

with open('../static/data/data_by_location.json','r') as infile:
	with open('../static/data/data_by_book.json','w') as out_file:
		old_json_data = json.load(infile)
		json_data = {'rows':[]}
		for r in old_json_data['rows']:
			for book in r["properties"]["books"]:
				d = book
				d["location"] = {}
				d["location"]["geometry"] = r["geometry"]
				d["location"]["name"] = r["properties"]["name"]
				d["location"]["type"] = r["properties"]["type"]
				if "scenes" in r["properties"]:
					d["location"]["scenes"] = r["properties"]["scenes"]
				json_data["rows"].append(d)
		#json.dump(json_data,out_file)


