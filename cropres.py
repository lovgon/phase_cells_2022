import os
import cv2

for filename in os.listdir('6_20211022173732_Acquisition-20063790-0_phase_unwrapped'):
    image = cv2.imread(os.path.join('6_20211022173732_Acquisition-20063790-0_phase_unwrapped', filename))
    print(filename)
    cropped = image[52:1304, 189:1852]
    width = 1624
    height = 1224
    dim = (width, height)
    resized = cv2.resize(cropped, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite('6_20211022173732_Acquisition-20063790-0_phase_unwrapped_crop_res/' + filename, resized)
