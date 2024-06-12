import matplotlib.pyplot as plt
import pandas as pd

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