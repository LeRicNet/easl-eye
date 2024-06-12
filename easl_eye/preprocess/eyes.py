from cateyes import (classify_nslr_hmm, classify_remodnav, classify_velocity)
from cateyes.utils import (pixel_to_degree, sfreq_to_times) # to preprocess eye-tracking data
import pandas as pd

def format_data(data, screen_size: float, screen_res: tuple, viewing_dist: int):
	
	# format the numeric data to remove parentheses and convert to float
	str_fmt = lambda v: v.replace('(', '').replace(')', '')
	
	for var in ['right_x', 'right_y', 'left_x', 'left_y']:
		data[var] = data[var].apply(str_fmt)
		
	# convert the values to pixels and degrees
	for var in ['right_x', 'left_x']:
		data['{}_px'.format(var)] = data[var].apply(lambda x: float(x) * screen_res[0])
		data['{}_deg'.format(var)] = pixel_to_degree(
			x=data['{}_px'.format(var)].values, 
			viewing_dist=viewing_dist,
			screen_size=screen_size[0],
			screen_res=screen_res[0])
	
	for var in ['right_y', 'left_y']:
		data['{}_px'.format(var)] = data[var].apply(lambda x: float(x) * screen_res[1])
		data['{}_deg'.format(var)] = pixel_to_degree(
			x=data['{}_px'.format(var)].values, 
			viewing_dist=viewing_dist,
			screen_size=screen_size[1],
			screen_res=screen_res[1])
		
	return data


def classify(data, eye: str, roi_x: list=None):	
	
	# Time needs to be formatted for the cateyes algorithm
	timestamp = data['timestamp_hardware'].values
	
	# Define the frequency of the hardware clock in Hz
	# This value depends on the specific hardware and should be provided by the manufacturer
	# For example, if the hardware clock frequency is 1 GHz (1 billion cycles per second)
	hardware_clock_frequency = 250

	# Convert the hardware timestamp to seconds
	timestamp_in_seconds = timestamp / hardware_clock_frequency
	
	
	segment_id, segment_class = classify_velocity(
		x=data['{}_x_deg'.format(eye)].values,
		y=data['{}_y_deg'.format(eye)].values,
		time=sfreq_to_times(data['{}_x_deg'.format(eye)].values, sfreq=250, start_time=timestamp[0])
	)
	
	clf_res = pd.DataFrame({
		'timestamp_hardware': timestamp,
		'timestamp_in_seconds': timestamp_in_seconds,
		# 'timestamp_in_seconds': sfreq_to_times(data['{}_x_deg'.format(eye)].values, sfreq=250, start_time=timestamp[0]),
		'segment_id': segment_id,
		'segment_class': segment_class,
		'{}_x'.format(eye): data['{}_x'.format(eye)].values,
		'{}_y'.format(eye): data['{}_y'.format(eye)].values
	})
	
	if roi_x is not None:
		clf_res['in_roi_filter_x'] = data['{}_x'.format(eye)].apply(
			lambda value: min(roi_x) <= float(value) <= max(roi_x)
		)
	
	return clf_res
	
	

