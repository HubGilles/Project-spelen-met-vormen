# Project 2: Spelen met vormen (Gilles Servais)

Welcome to the Project "Spelen met vormen". This project is designed to modify and create new images. Functions are provided to do some modifications on the images and combine them into new images. 

## Installation

### Installing the Environment

1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/HubGilles/Project-spelen-met-vormen
2. Navigate to the project directory:
    ```sh
    cd project-name
3. Create a new conda environment from the provided YAML file:
    ```sh
    conda env create -f Project2.yml
4. Activate the newly created conda environment:
    ```sh
    conda activate .Project2
### Running the Project
After activating the conda environment, you can run the project using the following steps:

1. Navigate to the project directory:

    ```sh
    cd /path/to/your/project
2. Run the main script or execute specific Python files:
    ```sh
    python main.py
It demonstrates different image manipulation techniques using the imported functions from "Manipulation.py", such as flipping, rotating, resizing, and coloring quadrants of the image.
The processed images are displayed using the "show" function, which utilizes Matplotlib to visualize the images.


## Features

Resize images to specific dimensions.
Rotate images clockwise or counterclockwise by a given angle.
Flip images horizontally or vertically.
Change the color of images using a predefined color palette.
Combine multiple images into a single image.
Zoom into an image around a specified center point.

## Functions Explanations

### show(image)
Display the given image using Matplotlib.

* **'image':** NumPy array representing the image.

### red(image)
Convert the image to a red scale by setting green and blue channels to zero.

* **'image:'** NumPy array representing the image.

### green(image)
Convert the image to a green scale by setting red and blue channels to zero.

* **'image:'** NumPy array representing the image.

### blue(image)

Convert the image to a blue scale by setting red and green channels to zero.

* **'image:'** NumPy array representing the image.

### counterclockwise(image)
Rotate the image counterclockwise by 90 degrees.

* **'image:'** NumPy array representing the image.

### clockwise(image)
Rotate the image clockwise by 90 degrees.

* **'image:'** NumPy array representing the image.

### flip_y(image)
Flip the image vertically.

* **'image:'** NumPy array representing the image.

### flip_x(image)
Flip the image horizontally.

* **'image:'** NumPy array representing the image.

### repeat(image, repeats)
Repeat the image horizontally a specified number of times.

* **'image:'** NumPy array representing the image.

* **'repeats':** Number of times to repeat the image horizontally.

### glue(*arrays)
Concatenate multiple images horizontally.

* **'*arrays'**: List of NumPy arrays representing the images to concatenate.

### reorder(image, dimension)
Reorder the image by splitting it into multiple parts and concatenating them vertically.

* **'image:'** NumPy array representing the image.

* **'dimension'**: Number of parts to split the image into.

### organize(*arrays, dimension)
Organize multiple images by concatenating them horizontally and then reordering them vertically.

* **'*arrays'**: List of NumPy arrays representing the images to organize.
* **'dimension'**: Number of parts to split the concatenated image into.

### kwadrant(image, kwadrant)
Extract a specific quadrant of the image.

* **'image:'** NumPy array representing the image.
* **'kwadrant'**: Quadrant number (1 to 4) to extract.

### color(image, color, face="back")
Change the color of the image to a specified color.

* **'image:'** NumPy array representing the image.
* **'color'**: Name of the color to change the image to.
face: Face of the image to change the color ("back" or "front"). (default back).

### resize(image)
Resize the image to a square shape by adding filler pixels.

* **'image'**: NumPy array representing the image.

### zoom(image, x_zoom=1.3, y_zoom=1.3, x_center=50, y_center=50)
Zoom into the image around a specified center point.

* **'image'**: NumPy array representing the image.
* **'x_zoom'**: Zoom factor for the x-axis (default is 1.3).
* **'y_zoom'**: Zoom factor for the y-axis (default is 1.3).
* **'x_center'**: X-coordinate (in procent of total width) of the left side (default is 50).
* **'y_center'**: Y-coordinate (in procent of total heigth) of the top side (default is 50).