import requests
import functools

COVID_API_URL = 'https://covid-api.com/api/reports'

def get_remote_data(list):
  
  for item in list:
    iso = item.iso
    date = item.date
    
    print("Querying API to gather COVID data for " + iso + " on " + str(date) + "\n")
    
    query = {'iso':iso, 'date':date}
    response = requests.get(COVID_API_URL, params=query)

    if (response.status_code == 200):
      _process_data(item, response.json()['data'])
    else:
      print("No response for record with ISO:" + iso + " and Date:" + str(date) + "\n")

def _process_data(country, data):
  if len(data) > 0:
    confirmed = 0
    deaths = 0
    recovered = 0
    for item in data:
      confirmed += item['confirmed']
      deaths += item['deaths']
      recovered += item['recovered']
    
    country.set_data(confirmed=confirmed, deaths=deaths, recovered=recovered)
  else:
    print ("No data for record with ISO:" + country.iso + " and Date:" + str(country.date) + "\n")
