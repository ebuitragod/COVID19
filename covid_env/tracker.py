import flask 
import configparser
import requests
from flask import jsonify 


config = configparser.ConfigParser()
config.read('config.txt')

host=config['tracker']['host']
list=config['tracker']['listsources']
getrecent=config['tracker']['getrecent']



app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/', methods=['GET'])
def home():
	resp = requests.get(host+list)
	if resp.status_code != 200:
		raise ApiError('Cannot list sources: {}'.format(resp.status_code))


	responseValue=[]

	for source in resp.json()["sources"]:
		val='{}{}?source={}'.format(host,getrecent,source);
		resourceresp = requests.get(val)

		if resourceresp.status_code != 200:
			raise ApiError('Cannot fetch resource:{} detail: {}'.format(source,resourceresp.status_code))

		responsedata=resourceresp.json();
		recentdata={};
		recentdata['source'] = source;
		recentdata['latest'] = responsedata['latest'];
		recentdata['locations'] = responsedata['locations'];

		responseValue.append(recentdata);

		print('Source : summary:{} {}'.format(responsedata['latest'], responsedata['locations']));

	return jsonify(responseValue)

app.run()
