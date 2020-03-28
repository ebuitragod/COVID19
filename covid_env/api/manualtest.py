from api.models import Location
from api.serializers import LocationSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
location=Location(source='test1', country_id=1, country='testcountry1')
location.save();
location=Location(source='test2', country_id=2, country='testcountry2')
location.save();
locationSerialize=LocationSerializer(location);
locationSerialize.data