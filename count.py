import requests
from bs4 import BeautifulSoup

#html=open("demo.html","r").read();
r = requests.get('https://www.moh.gov.bh/COVID19')
html=r.text
#parse html
soup=BeautifulSoup(html, "html5lib")
#get statistics table
table=soup.findAll("table")[0]
#get total check 
total_check=table.findAll("tr")[0].findAll("span")[0].text
negative_cases=table.findAll("td")[0].findAll("span")[0].text
existing_cases=table.findAll("td")[1].findAll("span")[0].text
stable_existing_cases=table.findAll("td")[3].findAll("span")[0].text
critical_existing_cases=table.findAll("td")[4].findAll("span")[0].text
outside_cases=table.findAll("td")[5].findAll("span")[0].text
cases_around_outside_cases=table.findAll("td")[5].findAll("span")[1].text
local_cases=table.findAll("td")[5].findAll("span")[2].text
recovered_cases=table.findAll("td")[6].findAll("span")[0].text
