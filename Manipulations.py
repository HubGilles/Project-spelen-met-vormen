import numpy as np
import matplotlib.pyplot as plt

# Sensitivity for color change
tolerance = 200

# Dictionary containing color names and their RGB values
colorpalet = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
}

def show(image):
    """
    Display the image using matplotlib.
    Args:
    - image: The image to display.
    """
    plt.imshow(image)
    plt.show()

def red(image):
    """
    Convert all non-red pixels in the image to black.
    Args:
    - image: The input image.
    Returns:
    - image_R: The modified image with only red pixels.
    """
    image_R = image.copy()
    image_R[:,:,[1,2]] = 0
    return image_R

def green(image):
    """
    Convert all non-green pixels in the image to black.
    Args:
    - image: The input image.
    Returns:
    - image_G: The modified image with only green pixels.
    """
    image_G = image.copy()
    image_G[:,:,[0,2]] = 0
    return image_G

def blue(image):
    """
    Convert all non-green pixels in the image to black.
    Args:
    - image: The input image.
    Returns:
    - image_G: The modified image with only green pixels.
    """
    image_B = image.copy()
    image_B[:,:,[0,1]] = 0
    return image_B

def counterclockwise(image):
    """
    Rotate the image counterclockwise by 90 degrees.
    Args:
    - image: The input image.
    Returns:
    - image_counterclockwise: The rotated image.
    """
    image_counterclockwise = np.rot90(image)
    return image_counterclockwise

def clockwise(image):
    """
    Rotate the image clockwise by 90 degrees.
    Args:
    - image: The input image.
    Returns:
    - image_clockwise: The rotated image.
    """
    image_clockwise = np.rot90(image, k=-1)
    return image_clockwise

def flip_y(image):
    """
    Flip the image vertically.
    Args:
    - image: The input image.
    Returns:
    - image_y: The vertically flipped image.
    """
    image_y = np.flip(image, 1)
    return image_y

def flip_x(image):
    """
    Flip the image horizontally.
    Args:
    - image: The input image.
    Returns:
    - image_x: The horizontally flipped image.
    """
    image_x = np.flip(image, 0)
    return image_x

def repeat(image, repeats):
    """
    Repeat the image horizontally.
    Args:
    - image: The input image.
    - repeats: Number of times to repeat the image horizontally.
    Returns:
    - repeated_image: The repeated image.
    """
    return np.tile(image, (1, repeats, 1)) 

def glue(*arrays):
    """
    Concatenate multiple arrays horizontally.
    Args:
    - arrays: A variable number of arrays to be concatenated.
    Returns:
    - concatenated_array: The concatenated array.
    """
    concatenated_array = np.concatenate(arrays, axis=1)
    return concatenated_array

def reorder(image, dimension):
    """
    Reorder the image by splitting it into multiple segments along the specified dimension and concatenating them vertically.
    Args:
    - image: The input image.
    - dimension: The number of segments to split the image into horizontally.
    Returns:
    - image_reorder: The reordered image.
    """
    image_reorder = np.concatenate((np.split(image, dimension, axis=1)), axis = 0)
    return image_reorder

def organize(*arrays,dimension):
    """
    Organize multiple arrays by concatenating them horizontally and then splitting them into segments along the specified dimension and concatenating them vertically.
    Args:
    - arrays: A variable number of arrays to be organized.
    - dimension: The number of segments to split the concatenated arrays into horizontally.
    Returns:
    - image_reorder: The organized image.
    """
     concatenated_array = np.concatenate(arrays, axis=1)
     image_reorder = np.concatenate((np.split(concatenated_array, dimension, axis=1)), axis = 0)
     return image_reorder   

def kwadrant(image, kwadrant=1):
    """
    Extract a quadrant from the image based on the specified quadrant number.
    Args:
    - image: The input image.
    - kwadrant: The quadrant number (1, 2, 3, or 4).
    Returns:
    - part: The extracted quadrant of the image.
    """
    image = np.repeat(np.repeat(image, 2, axis = 1), 2, axis=0)
    if kwadrant == 1:
            part = image[0:image.shape[0]//2, 0:image.shape[1]//2]
    elif kwadrant == 2:
            part = image[0:image.shape[0]//2, image.shape[1]//2:image.shape[1]]
    elif kwadrant == 3:
            part = image[image.shape[0]//2:image.shape[0], image.shape[1]//2:image.shape[1]]
    elif kwadrant == 4:
            part = image[image.shape[0]//2:image.shape[0], 0:image.shape[1]//2]
    else:
        print("The number is not an integer or not between 1 and 4.")
    return part

def color(image, color, face = "back"):
    """
    Modify the image by changing pixels that match the background color to the specified color.
    Args:
    - image: The input image.
    - color: The color to apply to the modified pixels.
    - face: Specifies whether to sample the background color from the "back" or "front" of the image.
    Returns:
    - image_modified: The modified image with the specified color applied to the background pixels.
    """
    color = colorpalet[color]
    if face == "back":
        sample = (5,5)
    elif face == "front":
        y = image.shape[0]//2
        x = image.shape[1]//2
        sample = (y, x)

    background_pixel = image[sample].astype(np.int16)
    min_color = np.clip(background_pixel - tolerance, 0, 255)  
    max_color = np.clip(background_pixel + tolerance, 0, 255)
 
    mask = np.all((min_color <= image) & (image <= max_color), axis=-1)
    image_modified = image.copy()
    image_modified[mask] = color

    return image_modified

def resize(image):
    """
    Resize the image to make it square by adding blank or colored space around it, if necessary.
    Args:
    - image: The input image.
    Returns:
    - image_sized: The resized image with blank space added to make it square.
    """
    shape = image.shape
    form = (shape[0]-shape[1])
    if form > 0:
        gap = form//2
        fill_1 = np.tile(image[:,1,:],(gap, 1, 1))
        fill_2 = np.tile(image[:,1,:],(gap+form%2, 1, 1))
        image_sized = np.hstack([fill_1, image, fill_2])
    elif form < 0:
        gap = abs(form)//2
        fill_1 = np.tile(image[0, :, :], (gap, 1, 1)) 
        fill_2 = np.tile(image[0, :, :], (gap+form%2, 1, 1)) 
        image_sized = np.vstack([fill_1, image, fill_2, ])
    else:
        print("No resize executed")
        return image
    return image_sized

def zoom(image, x_zoom=1.3, y_zoom=1.3, x_center=50, y_center=50):
    """
    Zoom in or out on the image around the specified center coordinates.
    Args:
    - image: The input image.
    - x_zoom: The zoom factor along the x-axis.
    - y_zoom: The zoom factor along the y-axis.
    - x_center: The x-coordinate of the zoom center (percentage of image width).
    - y_center: The y-coordinate of the zoom center (percentage of image height).
    Returns:
    - image_zoomed: The zoomed image.
    """
    view = np.tile(image, (3,3,1))
    view_width = int(view.shape[1] * x_zoom)
    view_height = int(view.shape[0] * y_zoom)
    view_zoomed = np.zeros((view_height, view_width, 3),dtype=np.uint8)

    for x_view in range(view_width):
        for y_view in range(view_height):
            x = int(x_view//x_zoom)
            y = int(y_view//y_zoom)
            view_zoomed[y_view,x_view] = view[y,x]

    x_center = int((image.shape[1] * x_zoom * (1 + x_center/100)))
    y_center = int((image.shape[0] * y_zoom * (1 + y_center/100)))
    image_width = image.shape[1]
    image_height = image.shape[0]

    image_zoomed = view_zoomed[y_center - image_height//2 : y_center + image_height//2 + image_height%2, x_center - image_width//2 : x_center + image_width//2 + image_width%2]

    return image_zoomed