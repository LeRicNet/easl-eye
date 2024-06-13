import pandas as pd
from datetime import datetime

def align_tracking_data(image_tracking, eye_tracking):
	image_tracking['ui_timestamp_date'] = image_tracking['ui_timestamp'].apply(lambda s: s.split('T')[0])
	image_tracking['ui_timestamp_time'] = image_tracking['ui_timestamp'].apply(lambda s: s.split('T')[1])

	image_tracking = image_tracking.loc[image_tracking['ui_timestamp_date'] == '2024-05-14']

	def convert2us(date):
		# Convert the date string to a datetime object
		date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

		# Convert the datetime object to microseconds
		microseconds = date.timestamp() * 1e4
		return microseconds
	
	image_tracking['ui_timestamp_us'] = image_tracking['ui_timestamp'].apply(convert2us)

	image_tracking['adjusted_timestamp'] = image_tracking['ui_timestamp_us'].apply(
		lambda t: t - (max(image_tracking.ui_timestamp_us) - max(eye_tracking.timestamp_system)))

	image_tracking['adjusted_timestamp'] = pd.to_datetime(image_tracking['adjusted_timestamp'], unit='ms')
	image_tracking.set_index('adjusted_timestamp', inplace=True)

	eye_tracking['timestamp_system'] = pd.to_datetime(eye_tracking['timestamp_system'], unit='ms')
	eye_tracking.set_index('timestamp_system', inplace=True)

	aligned_dataset = eye_tracking.join(image_tracking, how='outer').fillna(method='ffill')
	return aligned_dataset