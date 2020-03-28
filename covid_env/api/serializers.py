#api.serializers.py

from rest_framework import serializers

from .models import Location

class LocationSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		return Location.objects.create(**validated_data)
		
	class Meta:
		model = Location
		fields = ('source', 'country_id', 'country', 'country_code', 'country_codeInfo', 'state', 'region', 'latitude', 'longitude', 'cases', 'todayCases', 'deaths', 'totalDeaths', 'recovered', 'active', 'critical', 'casesPerOneMillion', 'deathsPerOneMillion', 'loadedDate', 'created_at')
