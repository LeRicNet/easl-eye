from cateyes import (classify_nslr_hmm, classify_remodnav, classify_velocity)
from cateyes.utils import (pixel_to_degree, sfreq_to_times) # to preprocess eye-tracking data
from cateyes.classification import mad_velocity_thresh
import pandas as pd
import numpy as np

def format_data(data, screen_size: float, screen_res: tuple, viewing_dist: int):
	
	# format the numeric data to remove parentheses and convert to float
	str_fmt = lambda v: v.replace('(', '').replace(')', '')
	
	for var in ['right_x', 'right_y', 'left_x', 'left_y']:
		data[var] = data[var].apply(str_fmt)
		
	# convert the values to pixels and degrees
	for var in ['right_x', 'left_x']:
		data['{}_px'.format(var)] = data[var].apply(lambda x: float(x) * screen_res[0])
		degree = pixel_to_degree(
			x=data['{}_px'.format(var)].values, 
			viewing_dist=viewing_dist,
			screen_size=screen_size[0],
			screen_res=screen_res[0])
		data['{}_deg'.format(var)] = np.squeeze(degree)
	
	for var in ['right_y', 'left_y']:
		data['{}_px'.format(var)] = data[var].apply(lambda x: float(x) * screen_res[1])
		degree = pixel_to_degree(
			x=data['{}_px'.format(var)].values, 
			viewing_dist=viewing_dist,
			screen_size=screen_size[1],
			screen_res=screen_res[1])
		data['{}_deg'.format(var)] = np.squeeze(degree)
		
	return data


def classify(data, eye: str, roi_x: list=None, roi_y: list=None):	
	
	# Time needs to be formatted for the cateyes algorithm
	timestamp = data['timestamp_hardware'].values
	elapsed_time = sfreq_to_times(data['{}_x_deg'.format(eye)].values, sfreq=250, start_time=timestamp[0])
	

	
	segment_id, segment_class = classify_velocity(
		x=data['{}_x_deg'.format(eye)].values,
		y=data['{}_y_deg'.format(eye)].values,
		time=elapsed_time,
		threshold=mad_velocity_thresh(
			x=data['{}_x_deg'.format(eye)].values,
			y=data['{}_y_deg'.format(eye)].values,
			time=elapsed_time
		)
	)
	
	data['segment_id'] = segment_id
	data['segment_class'] = segment_class
	data['{}_x'.format(eye)] = data['{}_x'.format(eye)].apply(float).values
	data['{}_y'.format(eye)] = data['{}_x'.format(eye)].apply(float).values
	
	if roi_x is not None:
		data['in_roi_filter_x'] = data['{}_x'.format(eye)].apply(
			lambda value: min(roi_x) <= float(value) <= max(roi_x)
		)
		data['{}_roi_filter_scaled_x'.format(eye)] = data['{}_x'.format(eye)].apply(
			lambda x: scale_gaze_data(x, _min=min(roi_x), _max=max(roi_x))
		)
		
	if roi_y is not None:
		data['in_roi_filter_y'] = data['{}_y'.format(eye)].apply(
			lambda value: min(roi_y) <= float(value) <= max(roi_y)
		)
		data['{}_roi_filter_scaled_y'.format(eye)] = data['{}_y'.format(eye)].apply(
			lambda y: scale_gaze_data(y, _min=min(roi_y), _max=max(roi_y))
		)
		
	return data
	
	
def scale_gaze_data(x, _min, _max, dim_size=900):
    return ((float(x) - _min) / (_max - _min)) * dim_size
