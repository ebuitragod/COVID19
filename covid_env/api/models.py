from django.db import models

# Location.
class Location(models.Model):
	source = models.CharField(max_length=200, null=True)
	country_id = models.BigIntegerField(null=True)
	country = models.CharField(max_length=200, null=True)
	country_code = models.CharField(max_length=16, null=True)
	country_codeInfo = models.CharField(max_length=16, null=True)
	state = models.CharField(max_length=200, null=True)
	region = models.CharField(max_length=200, null=True)
	latitude = models.DecimalField(decimal_places=6,max_digits=12, null=True)
	longitude = models.DecimalField(decimal_places=6,max_digits=12, null=True)
	cases = models.BigIntegerField(null=True)
	todayCases= models.BigIntegerField(null=True)
	deaths = models.BigIntegerField(null=True)
	totalDeaths = models.BigIntegerField(null=True) 
	recovered = models.BigIntegerField(null=True)
	active = models.BigIntegerField(null=True)
	critical = models.BigIntegerField(null=True)
	casesPerOneMillion = models.DecimalField(decimal_places=2,max_digits=6, null=True)
	deathsPerOneMillion = models.DecimalField(decimal_places=2,max_digits=6, null=True)
	loadedDate = models.DateTimeField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		stateVal = ''
		countryVal = ''
		value = ''
		if self.country is not None:
			countryVal = self.country
			value = countryVal
		if self.state is not None:
			stateVal = self.state
			value = '{}-{}'.format(countryVal, stateVal)
		return value

	class Meta:
		ordering = ['created_at']