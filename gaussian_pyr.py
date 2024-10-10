import numpy as np
import cv2
from scipy.ndimage import gaussian_filter

def gaussian_pyr(img, num_octaves=4, num_scales=5, sigma=1.6):
    octaves = []
    k = np.sqrt(2)
    for i in range(num_octaves):
        octave = [img]
        for j in range(1, num_scales):
            blur = gaussian_filter(octave[-1], sigma * (k ** j))
            octave.append(blur)
        octaves.append(octave)
        img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    return octaves