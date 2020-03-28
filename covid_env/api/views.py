#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import requests
from django.conf import settings
import datetime
from django.core import serializers


from .serializers import LocationSerializer
from .models import Location
# views here.

@api_view(['GET'])
def LocationList(request):
	"""
	List all Locations
	"""

	locations = Location.objects.all().order_by('source')
	print('Cound found: {}'.format(locations.count()))
	data = serializers.serialize("json", locations)
	return HttpResponse(data, content_type='application/json');

@api_view(['GET'])
def LocationLoad(request):
	"""
	This would help to fetch all data and store it
	"""
	responseValue = LoadTracker();
	responseValue = [] if not responseValue else responseValue;

	novalTrackerResponse = LoadNovalTracker();
	if novalTrackerResponse:
		responseValue.append(novalTrackerResponse);

	return JsonResponse(responseValue, safe=False)

def LoadNovalTracker():
	host = settings.NOVALCOVID_TRACKER_HOST
	apipath = settings.NOVALCOVID_COUNTRY_API

	responseValue = []
	loadDate = datetime.date.today()
	sourceId = 'novaldata-api.data';
	foundObjects = Location.objects.filter(source = sourceId, loadedDate = loadDate).count()

	if foundObjects > 0:
		print('NovalCovidData: Source Id :{} has been loaded already for date: {} with count:{}'.format(sourceId, loadDate, foundObjects))
		return responseValue;

	resp = requests.get(host+apipath);
	if resp.status_code != 200:
		raise ApiError('NovalCovidData: Cannot Get Response: {}'.format(resp.status_code))

	responsedata=resp.json();
	for locationFound in responsedata:
		print(locationFound);
		countryInfo = locationFound['countryInfo']
		createdVal = datetime.datetime.utcnow()

		Location.objects.update_or_create(source = sourceId,
		country_code =countryInfo['iso3'],
		country = locationFound['country'],
		state = '',
		region = '',
		latitude = float(countryInfo['lat']) if countryInfo['lat'] else 0,
		longitude= float(countryInfo['long']) if countryInfo['long'] else 0,
		loadedDate = loadDate,
		defaults = {    
			'cases' : int(locationFound['cases']) if locationFound['cases'] else 0,
			'deaths' : int(locationFound['deaths']) if locationFound['deaths'] else 0,
			'recovered' : int(locationFound['recovered']) if locationFound['recovered'] else 0,
			'todayCases': int(locationFound['todayCases']) if locationFound['todayCases'] else 0,
			'totalDeaths': int(locationFound['todayDeaths']) if locationFound['todayDeaths'] else 0,
			'active': int(locationFound['active']) if locationFound['active'] else 0,
			'critical': int(locationFound['critical']) if locationFound['critical'] else 0,
			'created_at' : createdVal
		}
		)
		responseValue.append('source:{}, country:{}, cases:{}, deaths:{}, recovered:{}, active:{}, critical:{}'.format(sourceId, 
			locationFound['country'], locationFound['cases'], locationFound['deaths'], locationFound['recovered'],
			locationFound['active'],  locationFound['critical'] ));

	return responseValue;


def LoadTracker():
	host=settings.TRACKERHOST
	listapipath=settings.TRACKERLISTAPI
	getrecentapipath=settings.TRACKERGETLOCATIONAPI
	resp = requests.get(host+listapipath)
	if resp.status_code != 200:
		raise ApiError('TrackerData: Cannot list sources: {}'.format(resp.status_code))

	responseValue=[]

	for source in resp.json()["sources"]:
		loadDate = datetime.date.today()
		sourceId = 'tracker-api.{}'.format(source);

		foundObjects = Location.objects.filter(source = sourceId, loadedDate = loadDate).count()

		if foundObjects > 0:
			print('TrackerData: Source Id :{} has been loaded already for date: {} with count:{}'.format(sourceId, loadDate, foundObjects))
			continue;

		print('TrackerData: Loading for sourceId:{} for date:{}'.format(sourceId, loadDate));

		val='{}{}?source={}'.format(host,getrecentapipath,source);
		resourceresp = requests.get(val)

		if resourceresp.status_code != 200:
			raise ApiError('Cannot fetch resource:{} detail: {}'.format(source,resourceresp.status_code))

		responsedata=resourceresp.json();
		recentdata={};
		recentdata['source'] = source;
		recentdata['latest'] = responsedata['latest'];
		recentdata['locations'] = responsedata['locations'];
		locationDataFromSource = responsedata['locations'];
		for locationFound in locationDataFromSource:
			countryInfo = locationFound['coordinates']
			caseInfo = locationFound['latest']
			createdVal = datetime.datetime.utcnow()

			Location.objects.update_or_create(source = sourceId,
			country_code =locationFound['country_code'],
			country = locationFound['country'],
			state = locationFound['province'],
			region = locationFound['county'] if hasattr(locationFound, 'county') else '',
			latitude = float(countryInfo['latitude']) if countryInfo['latitude'] else 0,
			longitude= float(countryInfo['longitude']) if countryInfo['longitude'] else 0,
			loadedDate = loadDate,
			defaults = {    
				'cases' : int(caseInfo['confirmed']) if caseInfo['confirmed'] else 0,
				'deaths' : int(caseInfo['deaths']) if caseInfo['deaths'] else 0,
				'recovered' : int(caseInfo['recovered']) if caseInfo['recovered'] else 0,
				'created_at' : createdVal
			}
			)
			responseValue.append(recentdata);

		return responseValue;