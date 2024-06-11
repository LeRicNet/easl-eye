import json
import pandas as pd
import requests

def get_viewer_tracking_info():
	# Send a GET request to the API endpoint
	response = requests.get('http://amc-tensor1.ucdenver.pvt/eyetracking')

	# Parse the response as JSON
	data = response.json()

	# Print the data
	df = pd.json_normalize(data)
	
	return df