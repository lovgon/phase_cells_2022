import skimage
from skimage import feature
from skimage import filters
from scipy.ndimage import distance_transform_edt
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

for filename in os.listdir('images/'):
    cell_image = cv2.imread(os.path.join('images/', filename))
    gray_image = cv2.cvtColor(cell_image, cv2.COLOR_BGR2GRAY)
    print(filename)
    cell_image_denoised = filters.median(gray_image, footprint=np.ones((7, 7)))
    edges = skimage.feature.canny(cell_image_denoised, sigma=1)
    dt = distance_transform_edt(~edges)
    plt.imshow(dt)
    plt.savefig('images_dt_7/' + filename, bbox_inches='tight', facecolor='black', dpi=340)
