# Generated by Django 2.2.10 on 2020-03-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='active',
            field=models.BigIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='cases',
            field=models.BigIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='casesPerOneMillion',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='country_code',
            field=models.CharField(blank=True, default=None, max_length=16),
        ),
        migrations.AlterField(
            model_name='location',
            name='country_codeInfo',
            field=models.CharField(blank=True, default=None, max_length=16),
        ),
        migrations.AlterField(
            model_name='location',
            name='country_id',
            field=models.BigIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='critical',
            field=models.BigIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='deaths',
            field=models.BigIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='deathsPerOneMillion',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=12),
        ),
        migrations.AlterField(
            model_name='location',
            name='loadedDate',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=12),
        ),
        migrations.AlterField(
            model_name='location',
            name='recovered',
            field=models.BigIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='source',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='todayCases',
            field=models.BigIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='totalDeaths',
            field=models.BigIntegerField(blank=True, default=None),
        ),
    ]
