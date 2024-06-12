import json
import pandas as pd
import requests

def get_viewer_tracking_info(url):
	"""collect the viewer tracking information from EASL analytics
	
	This is the instance in the series that is being viewed at a specific time.
	"""
	
	# Send a GET request to the API endpoint
	response = requests.get(url)

	# Parse the response as JSON
	data = response.json()

	# Print the data
	df = pd.json_normalize(data)
	return df


def load_eyetracking_data(fname):
	df = pd.read_csv(fname, header=None)
	df.columns = ['right_x', 'right_y', 'left_x', 'left_y', 'timestamp_hardware', 'timestamp_system']
	return df