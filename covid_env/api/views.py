#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import requests
from django.conf import settings
import datetime


from .serializers import LocationSerializer
from .models import Location
# views here.

@api_view(['GET', 'POST'])
def LocationList(request):
	"""
	List all Locations
	"""

	locations = Location.objects.all().order_by('source')
	serializer_class = LocationSerializer(locations)
	return JsonResponse(serializer_class.data, safe=False)
	#return JsonResponse(serializer_class.data, safe=False)


@api_view(['GET'])
def LocationLoad(request):
	"""
	This would help to fetch all data and store it
	"""
	host=settings.TRACKERHOST
	listapipath=settings.TRACKERLISTAPI
	getrecentapipath=settings.TRACKERGETLOCATIONAPI
	resp = requests.get(host+listapipath)
	if resp.status_code != 200:
		raise ApiError('Cannot list sources: {}'.format(resp.status_code))

	responseValue=[]

	for source in resp.json()["sources"]:
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
			Location.objects.update_or_create(source = 'tracker-api.{}'.format(source),
			country_code =locationFound['country_code'],
			country = locationFound['country'],
			state = locationFound['province'],
			region = locationFound['county'] if hasattr(locationFound, 'county') else '',
			latitude = float(countryInfo['latitude']) if countryInfo['latitude'] else 0,
			longitude= float(countryInfo['longitude']) if countryInfo['longitude'] else 0,
			loadedDate = datetime.date.today(),
			defaults = {    
				'cases' : int(caseInfo['confirmed']) if caseInfo['confirmed'] else 0,
				'deaths' : int(caseInfo['deaths']) if caseInfo['deaths'] else 0,
				'recovered' : int(caseInfo['recovered']) if caseInfo['recovered'] else 0,
				'created_at' : createdVal
			}
			)

		responseValue.append(recentdata);

		print('Source : summary:{} {}'.format(responsedata['latest'], responsedata['locations']));

	return JsonResponse(responseValue, safe=False)
