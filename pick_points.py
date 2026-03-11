# import
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def rgb2gray(rgb):
    """
    Convert an RGB image to grayscale using:
    gray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    """
    return 0.2989 * rgb[..., 0] + 0.5870 * rgb[..., 1] + 0.1140 * rgb[..., 2]

def pick_points(image_path, num_points=0, title="Select points (press Enter when done)"):
    """
    Display the image and allow the user to pick points.
    
    Parameters:
      - image_path: Path to the image file.
      - num_points: Number of points to pick. Set to 0 for unlimited (stop with Enter).
      - title: Title for the selection window.
      
    Returns:
      - pts: A numpy array of selected (x, y) points.
    """
    # Load the image
    image = np.array(Image.open(image_path))
    
    # Convert to grayscale for display if it's RGB
    if image.ndim == 3:
        image_disp = rgb2gray(image)
    else:
        image_disp = image

    plt.figure(figsize=(8, 6))
    plt.imshow(image_disp, cmap='gray')
    plt.title(title)
    
    # If num_points is 0, user can pick unlimited points until they press Enter.
    pts = plt.ginput(n=num_points, timeout=0)
    plt.close()
    
    pts = np.array(pts)
    return pts

# Example usage:
img_file = "hallway3.jpg"
# Change the image file path as needed (e.g., "hallway1.jpg")
selected_points = pick_points(img_file, num_points=0, title="Select corresponding points on: "+img_file)
print("Selected Points:")
print(selected_points)

# Optionally, display the image with markers on the selected points.
img = np.array(Image.open(img_file))
if img.ndim == 3:
    img_disp = rgb2gray(img)
else:
    img_disp = img

plt.figure(figsize=(8,6))
plt.imshow(img_disp, cmap='gray')
plt.title("Selected Points")
for pt in selected_points:
    # Draw a red square at each selected point.
    rect = plt.Rectangle((pt[0]-3, pt[1]-3), 6, 6, edgecolor='red', facecolor='none', linewidth=2)
    plt.gca().add_patch(rect)
plt.show()
