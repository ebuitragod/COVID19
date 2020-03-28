# Generated by Django 2.2.10 on 2020-03-28 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('country_id', models.BigIntegerField()),
                ('country', models.CharField(max_length=200)),
                ('country_code', models.CharField(max_length=16)),
                ('country_codeInfo', models.CharField(max_length=16)),
                ('state', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=12)),
                ('cases', models.BigIntegerField()),
                ('todayCases', models.BigIntegerField()),
                ('deaths', models.BigIntegerField()),
                ('totalDeaths', models.BigIntegerField()),
                ('recovered', models.BigIntegerField()),
                ('active', models.BigIntegerField()),
                ('critical', models.BigIntegerField()),
                ('casesPerOneMillion', models.DecimalField(decimal_places=2, max_digits=6)),
                ('deathsPerOneMillion', models.DecimalField(decimal_places=2, max_digits=6)),
                ('loadedDate', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]