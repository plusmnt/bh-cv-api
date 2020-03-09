import requests
from bs4 import BeautifulSoup

#html=open("demo.html","r").read();
def get_data():
	r = requests.get('https://www.moh.gov.bh/COVID19')
	html=r.text
	#parse html
	soup=BeautifulSoup(html, "html5lib")
	#get statistics table
	table=soup.findAll("table")[0]
	#get total check 
	data=dict()
	data["total_check"]=table.findAll("tr")[0].findAll("span")[0].text
	data["negative_cases"]=table.findAll("td")[0].findAll("span")[0].text
	data["existing_cases"]=table.findAll("td")[1].findAll("span")[0].text
	data["stable_existing_cases"]=table.findAll("td")[3].findAll("span")[0].text
	data["critical_existing_cases"]=table.findAll("td")[4].findAll("span")[0].text
	data["outside_cases"]=table.findAll("td")[5].findAll("span")[0].text
	data["cases_around_outside_cases"]=table.findAll("td")[5].findAll("span")[1].text
	data["local_cases"]=table.findAll("td")[5].findAll("span")[2].text
	data["recovered_cases"]=table.findAll("td")[6].findAll("span")[0].text
	return data


