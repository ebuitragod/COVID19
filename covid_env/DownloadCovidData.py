#DownloadCovidData.py

import requests
import datetime

url = 'http://localhost:8000/all'
headers = {'Accept': 'application/json'}

response = requests.get(url, headers=headers);


if response.status_code != 200:
			raise ApiError('Cannot fetch resource:{} detail: {}'.format(source,response.status_code))

with open('Covid19Data.json', 'wb') as outf:
	outf.write(response.content)