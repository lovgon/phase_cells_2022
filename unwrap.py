import os
import cv2
from skimage import exposure
import numpy as np
from skimage.restoration import unwrap_phase
import matplotlib.pyplot as plt

for filename in os.listdir('6_20211022173732_Acquisition-20063790-0_phase/'):
    # Load an image as a floating-point grayscale
    image = cv2.imread(os.path.join('6_20211022173732_Acquisition-20063790-0_phase/', filename))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(filename)

    # Scale the image to [0, 4*pi]
    image_rescale = exposure.rescale_intensity(image_gray, out_range=(0, 4 * np.pi))

    # Create a phase-wrapped image in the interval [-pi, pi)
    image_wrapped = np.angle(np.exp(1j * image_rescale))

    # Perform phase unwrapping
    image_unwrapped = unwrap_phase(image_wrapped)

    plt.imshow(image_unwrapped, cmap='gray')
    plt.savefig('6_20211022173732_Acquisition-20063790-0_phase_unwrapped/' + filename,
                bbox_inches='tight',
                facecolor='black',
                dpi=340)
