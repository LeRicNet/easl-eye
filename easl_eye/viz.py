# %% environment and functions
import numpy as np
import matplotlib.pyplot as plt
import os
join = os.path.join

from skimage import io, transform

import pandas as pd
import cv2
import easl_eye as eye

def raw_gaze_plot(data):
	df = pd.DataFrame({
		'X': data['right_x'].apply(float),
		'Y': data['right_y'].apply(float),
	})

	# Create a scatter plot
	plt.scatter(df['X'], df['Y'])

	# Set the labels for the x and y axes
	plt.xlabel('X')
	plt.ylabel('Y')

	# Set the title for the plot
	plt.title('recorded gaze positions')

	# Display the plot
	return plt.show()


def session_video(aligned_data, instance_map, dims: tuple=(900, 900), return_array=True, overlay_eyetracking=False):
	# Assume we have a list of 2D numpy arrays
	images = [eye.get_pixel_array(aligned_data.current_uid[i], instance_map) for i in range(len(aligned_data.current_uid))]
	if return_array:
		images = [cv2.resize(image, dims) for image in images]
		return images
	else:
		# Define the codec using VideoWriter_fourcc() and create a VideoWriter object
		fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
		video = cv2.VideoWriter('/home/jovyan/output.mp4', fourcc, 250, dims, isColor=False)

		## Write the frames
		for i, image in enumerate(images):
			image = cv2.resize(image, dims)
			if aligned_data.in_roi_filter_x[i]:
				video.write(image)
				
		# Finally release the video
		video.release()

# visualization functions
# source: https://github.com/facebookresearch/segment-anything/blob/main/notebooks/predictor_example.ipynb
# change color to avoid red and green
def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([251/255, 252/255, 30/255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)

def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='blue', facecolor=(0,0,0,0), lw=2))

