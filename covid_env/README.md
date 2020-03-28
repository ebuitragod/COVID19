# Covid Data Collector API

This web application exposes two REST apis. One will collect all measure data from different data source. The other one would return the available data from database.

# Project Setup

In order to run the application locally,
  - The application dependencies should be installed
  - Database schema migerations should have been run.

```
$pip install -r requirements.txt
$python  manage.py migrate
```

### Application Run

To run the web application, the following needs to be executed. The application would run in port `8000` in localhost

```
$python  manage.py runserver
```

### APIs

After starting the application, the swagger document could be found in at `http://localhost:8000/`

The following are the two APIs.
a. Loading Data from Source 
`http://localhost:8000/load`

b. Getting Counts for All countries from All data sources
`http://localhost:8000/all`

