# Bahrain (COVID-19) statistics

This is a json interface for the [summary of cases table](https://www.moh.gov.bh/COVID19) in Bahrain Ministry of Health website.

## [Live Demo](https://cvapi.awal.pw/)

You can just call the above link and it will return the data as a josn object.

### Returned data
| key | Description |
| ------ | ------ |
| total_check | Total Tested |
| negative_cases | Tested Negative |
| existing_cases | Active Cases |
| arrived_cases_icrp |International COVID-19 Repatriation Programme (ICRP)|
| stable_existing_cases | Stable cases  |
| critical_existing_cases |Critical cases |
| arrived_stable_existing_cases_icrp |ICRP Stable cases |
| arrived_critical_existing_cases_icrp | ICRP Critical cases |
| arrivals_from_abroad | Arrivals from abroad (Not ICRP) |
| contacts_of_arrivals_from_abroad | Contacts of arrivals from abroad |
| local_cases | Local cases (Community) |
| recovered_cases | Discharged |
| deaths | Deaths |
|request_timestamp | Unix time to know when the data fetched.|


## Quick integration
```
curl --location --request GET 'https://cvapi.awal.pw/'
```
More example available in the example folder.

### Errors
the following errors might happen:
- if there is no data cache and the server can not fetch data from Bahrain MOH website it will return 
```
{"erorr": "connection error"}
```
- if the there is a cached data and the server can not fetch data from Bahrain MOH website, cache data will be returned.

## The code
The server code created with `python3` using `BeautifulSoup` to parse the HTML table from [Ministry of Health website](https://www.moh.gov.bh/COVID19)

following library are required to run the code locally:
- [pip install requests](https://pypi.org/project/requests/)
- [pip install beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pip install html5lib](https://pypi.org/project/html5lib/)

Files:
- data_source.py: will load the data and return dictionary will all the keys
- server.py: will run a local server at `http://localhost:8181` 

Note:
- The data is being cached in `cvbh.json` so it will only request new data every 5 minutes.
- The function `get_data` can take a (True|False) value to enable data cache.

To run the server locally just run 
```bash
python3 server.py
```

# Extra

- More information about [Coronavirus (COVID-19)](https://www.flattenthecurve.com/)
- Bahrain Coronavirus COVID-19 Updates [coronabh.com](https://coronabh.com/)
- Volunteer in the Campaign to Combat Coronavirus (COVID-19)[volunteer.gov.bh](http://volunteer.gov.bh)

