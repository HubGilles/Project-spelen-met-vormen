import numpy as np
import matplotlib.pyplot as plt

tolerance = 200

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
    plt.imshow(image)
    plt.show()

def red(image):
    image_R = image.copy()
    image_R[:,:,[1,2]] = 0
    return image_R

def green(image):
    image_G = image.copy()
    image_G[:,:,[0,2]] = 0
    return image_G

def blue(image):
    image_B = image.copy()
    image_B[:,:,[0,1]] = 0
    return image_B

def counterclockwise(image):
    image_counterclockwise = np.rot90(image)
    return image_counterclockwise

def clockwise(image):
    image_clockwise = np.rot90(image, k=-1)
    return image_clockwise

def flip_y(image):
    image_y = np.flip(image, 1)
    return image_y

def flip_x(image):
    image_x = np.flip(image, 0)
    return image_x

def repeat(image, repeats):
    return np.tile(image, (1, repeats, 1)) 

def glue(*arrays):
    concatenated_array = np.concatenate(arrays, axis=1)
    return concatenated_array

def reorder(image, dimension):
    image_reorder = np.concatenate((np.split(image, dimension, axis=1)), axis = 0)
    return image_reorder

def organize(*arrays,dimension):
     concatenated_array = np.concatenate(arrays, axis=1)
     image_reorder = np.concatenate((np.split(concatenated_array, dimension, axis=1)), axis = 0)
     return image_reorder   

def kwadrant(image, kwadrant=1):
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
    This is comment to explain this functin and variables
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