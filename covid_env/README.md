# Covid Data Collector API

This web application exposes two REST apis. One will collect all measure data from different data source. The other one would return the available data from database.

# Project Setup

In order to run the application locally,
  - The application dependencies should be installed
  - Database schema migerations should have been run.

```$
$pip install -r requirements.txt
$python manage.py migrate
```

### Application Run

To run the web application, the following needs to be executed. The application would run in port `8000` in localhost

```$
$python manage.py runserver
```

#### Information

On calling the `load` API, the application would fetch the data and store it data store. When the `all` API would return all data records found in the data store.
To extend this application to get from more data source, in `api.views.py` a new `load and transform` has to be added and that has to be called from the `load` APIs view method.

### APIs

After starting the application, the document for APIs would be available at `http://localhost:8000/` as swagger.

The following are the two APIs.
a. Loading Data from Source 
`http://localhost:8000/load`

b. Getting Counts for All countries from All data sources
`http://localhost:8000/all`

Sample API Response

```
[
  {
    "source": "tracker-api.jhu",
    "country_id": null,
    "country": "Afghanistan",
    "country_code": "AF",
    "country_codeInfo": null,
    "state": "",
    "region": "",
    "latitude": "33.000000",
    "longitude": "65.000000",
    "cases": 110,
    "todayCases": null,
    "deaths": 4,
    "totalDeaths": null,
    "recovered": 0,
    "active": null,
    "critical": null,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "loadedDate": "2020-03-28T00:00:00Z",
    "created_at": "2020-03-28T16:35:04.758699Z"
  },
  {
    "source": "novaldata-api.data",
    "country_id": null,
    "country": "Liechtenstein",
    "country_code": "LIE",
    "country_codeInfo": null,
    "state": "",
    "region": "",
    "latitude": "47.166700",
    "longitude": "9.533300",
    "cases": 56,
    "todayCases": 0,
    "deaths": 0,
    "totalDeaths": 0,
    "recovered": 0,
    "active": 56,
    "critical": 0,
    "casesPerOneMillion": "1469.00",
    "deathsPerOneMillion": "0.00",
    "loadedDate": "2020-03-28T00:00:00Z",
    "created_at": "2020-03-28T16:35:07.025033Z"
  }
]
```