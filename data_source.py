#!/usr/bin/env python3
import datetime
import pytz
import requests
import json
from bs4 import BeautifulSoup
import os.path
from os import path


def get_local_data():
	if path.exists("cvbh.json"):
		local_file=open("cvbh.json","r")
		local_data=local_file.read()
		if(len(local_data)>5):
			data=json.loads(local_data)
			local_file.close()
			return data
	return None

def get_data(enable_cache):
	#read local cache file
	local_data=get_local_data()
	if local_data != None:
		if enable_cache ==True:
			now=int(datetime.datetime.now(tz=pytz.utc).timestamp() * 1000)
			#if less than 5min. request update cache, else return cache
			if now-local_data["request_timestamp"] <(5*60*1000):
				print("Return cache")
				return local_data

	try :
		r = requests.get('https://www.moh.gov.bh/COVID19')
		html=r.text
	except requests.Timeout:
		#return cached data
		if local_data == None:
			local_data={"error:":"timeout error"}
		return local_data
	except requests.ConnectionError:
		#return cached data
		if local_data == None:
			local_data={"erorr": "connection error"}
		return local_data

	print("Return new data")
	# html=open("demo.html","r").read();
	#parse html
	soup=BeautifulSoup(html, "html5lib")
	#get statistics table
	table=soup.findAll("table")[0]
	#get total check 
	data=dict()
	data["total_check"]=table.findAll("tr")[0].findAll("span")[0].text
	data["existing_cases"]=table.findAll("tr")[1].findAll("span")[0].text
	data["stable_existing_cases"]=table.findAll("td")[2].findAll("span")[0].text
	data["critical_existing_cases"]=table.findAll("td")[3].findAll("span")[0].text

	data["recovered_cases"]=table.findAll("td")[5].findAll("span")[0].text
	data["deaths"]=table.findAll("td")[6].findAll("span")[0].text
	
	#get current UTC timestamp
	#https://stackoverflow.com/a/52146362
	data["request_timestamp"]=int(datetime.datetime.now(tz=pytz.utc).timestamp() * 1000)
	#save as cache
	file=open("cvbh.json","w")
	file.write( json.dumps(data) )
	file.close()
	return data
