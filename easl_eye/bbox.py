import numpy as np

def get_center(box):
    """
    Function to find the center point of a bounding box.
    
    Parameters:
    box (list): A list of four integers representing the bounding box (x1, y1, x2, y2).
    
    Returns:
    tuple: A tuple representing the center point (x, y) of the bounding box.
    """
    x = np.mean([box[0], box[2]])
    y = np.mean([box[1], box[3]])
    return int(x), int(y)

def _expand_x(arr_resized, center_point, direction, buffer):
    """
    Helper function to expand the bounding box in the x-direction.
    
    Parameters:
    arr_resized (numpy.ndarray): The resized array representing the image.
    center_point (tuple): The center point of the bounding box.
    direction (str): The direction of expansion ('positive' or 'negative').
    buffer (float): The buffer for expansion as a fraction of the image width.
    
    Returns:
    int: The new boundary in the x-direction.
    """
    buffer = int(arr_resized.shape[1] * buffer)
    center_point = center_point[0]
    
    if direction == 'positive':
        max_value = 900
        for i in range(arr_resized.shape[1] - center_point):
            max_value = arr_resized[center_point, center_point + i]
            if max_value > 0:
                max_value = center_point + i + buffer
                break
        return max_value
    elif direction == 'negative':
        min_value = 0
        for i in range(center_point):
            min_value = arr_resized[center_point, center_point - i]
            if min_value > 0:
                min_value = center_point - i - buffer
                break
        return min_value

def _expand_y(arr_resized, center_point, direction, buffer):
    """
    Helper function to expand the bounding box in the y-direction.
    
    Parameters:
    arr_resized (numpy.ndarray): The resized array representing the image.
    center_point (tuple): The center point of the bounding box.
    direction (str): The direction of expansion ('positive' or 'negative').
    buffer (float): The buffer for expansion as a fraction of the image height.
    
    Returns:
    int: The new boundary in the y-direction.
    """
    buffer = int(arr_resized.shape[0] * buffer)
    center_point = center_point[1]
    
    if direction == 'positive':
        max_value = 900
        for j in range(arr_resized.shape[0] - center_point):
            _value = arr_resized[center_point + j,center_point]
            if _value > 0:
                max_value = center_point + j + buffer
                break
        return max_value
    elif direction == 'negative':
        min_value = 0
        for j in range(center_point):
            _value = arr_resized[center_point - j,center_point]
            if _value > 0:
                min_value = center_point - j - buffer
                break
        return min_value

def basic_expand(arr_resized, center_point, buffer):
    """
    Function to expand a bounding box from a center point.
    
    Parameters:
    arr_resized (numpy.ndarray): The resized array representing the image.
    center_point (tuple): The center point of the bounding box.
    buffer (float): The buffer for expansion as a fraction of the image dimensions.
    
    Returns:
    list: A list of four integers representing the expanded bounding box (x1, y1, x2, y2).
    """
    x1 = _expand_x(arr_resized=arr_resized, center_point=center_point, direction='negative', buffer=buffer)
    x2 = _expand_x(arr_resized=arr_resized, center_point=center_point, direction='positive', buffer=buffer)
    y1 = _expand_y(arr_resized=arr_resized, center_point=center_point, direction='negative', buffer=buffer)
    y2 = _expand_y(arr_resized=arr_resized, center_point=center_point, direction='positive', buffer=buffer)
    return [x1, y1, x2, y2]
