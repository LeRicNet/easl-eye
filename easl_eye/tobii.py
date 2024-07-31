import tobii_research as tr

def gaze_data_callback(gaze_data):
    # Get the left and right eye gaze point on the screen
    left_eye_point = gaze_data['left_gaze_point_on_display_area']
    right_eye_point = gaze_data['right_gaze_point_on_display_area']

    # Print gaze points
    print("Left eye gaze point: ", left_eye_point)
    print("Right eye gaze point: ", right_eye_point)

# Find all connected eye trackers
found_eyetrackers = tr.find_all_eyetrackers()

# Get the first eye tracker
my_eyetracker = found_eyetrackers[0]

# Subscribe to the gaze data stream
my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)