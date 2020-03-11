#!/usr/bin/env python3
import datetime
import pytz
import requests
import json
from bs4 import BeautifulSoup


def get_data(enable_cache):
	#read local cache file
	if enable_cache ==True:
		local_file=open("cvbh.json","r")
		local_data=local_file.read()
		#confirm the file is not empty
		if(len(local_data)>5):
			data=json.loads(local_data)
			now=int(datetime.datetime.now(tz=pytz.utc).timestamp() * 1000)
			#if less than 5min. request update cache, else return cache
			if now-data["request_timestamp"] <(5*60*1000):
				local_file.close()
				print("Return cache")
				return data
	print("Return new data")
	r = requests.get('https://www.moh.gov.bh/COVID19')
	html=r.text
	# html=open("demo.html","r").read();
	#parse html
	soup=BeautifulSoup(html, "html5lib")
	#get statistics table
	table=soup.findAll("table")[0]
	#get total check 
	data=dict()
	data["total_check"]=table.findAll("tr")[0].findAll("span")[0].text
	data["negative_cases"]=table.findAll("td")[0].findAll("span")[0].text
	data["existing_cases"]=table.findAll("td")[1].findAll("span")[0].text
	data["arrived_cases_icrp"]=table.findAll("td")[2].findAll("span")[0].text
	data["stable_existing_cases"]=table.findAll("td")[5].findAll("span")[0].text
	data["critical_existing_cases"]=table.findAll("td")[6].findAll("span")[0].text
	data["arrived_stable_existing_cases_icrp"]=table.findAll("td")[7].findAll("span")[0].text
	data["arrived_critical_existing_cases_icrp"]=table.findAll("td")[6].findAll("span")[0].text
	data["arrivals_from_abroad"]=table.findAll("td")[9].findAll("span")[0].text
	data["contacts_of_arrivals_from_abroad"]=table.findAll("td")[10].findAll("span")[0].text
	data["local_cases"]=table.findAll("td")[11].findAll("span")[0].text
	data["recovered_cases"]=table.findAll("tr")[7].findAll("td")[0].findAll("span")[0].text
	#get current UTC timestamp
	#https://stackoverflow.com/a/52146362
	data["request_timestamp"]=int(datetime.datetime.now(tz=pytz.utc).timestamp() * 1000)
	#save as cache
	file=open("cvbh.json","w")
	file.write( json.dumps(data) )
	file.close()
	return data


