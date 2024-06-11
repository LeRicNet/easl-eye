import json
import pandas as pd
import requests

def get_viewer_tracking_info():
	"""collect the viewer tracking information from EASL analytics
	"""
	
	# Send a GET request to the API endpoint
	response = requests.get('http://amc-tensor1.ucdenver.pvt/eyetracking')

	# Parse the response as JSON
	data = response.json()

	# Print the data
	df = pd.json_normalize(data)
	return df


def load_eyetracking_data(fname):
	df = pd.read_csv(fname, header=None)
	df.columns = ['right_x', 'right_y', 'left_x', 'left_y', 'timestamp_hardware', 'timestamp_system']
	return df