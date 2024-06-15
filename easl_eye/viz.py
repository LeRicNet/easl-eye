import matplotlib.pyplot as plt
import pandas as pd
import cv2
import numpy as np
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
		video = cv2.VideoWriter('output.mp4', fourcc, 55.0, dims, isColor=False)

		## Write the frames
		for i, image in enumerate(images):
			image = cv2.resize(image, dims)
			
			if overlay_eyetracking:
			
				if aligned_data.in_roi_filter_x[i]:

					# Create a scatter plot
					fig, ax = plt.subplots()
					ax.scatter(3, 1, 2, 'red')
					# ax.scatter(*zip(*points))
					plt.axis('off')

					# Convert the plot to a cv2 image
					fig.canvas.draw()
					plot_img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
					plot_img = plot_img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
					plot_img = cv2.cvtColor(plot_img,cv2.COLOR_RGB2BGR)

					# Overlay the scatter plot on the image
					overlay_image = cv2.addWeighted(image, 0.7, plot_img, 0.3, 0)

					video.write(overlay_image)

					# Close the plot to free up memory
					plt.close(fig)

				else:
					video.write(image)
			else:
				video.write(image)
				
		# Finally release the video
		video.release()