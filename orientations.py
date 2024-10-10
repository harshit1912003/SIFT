import numpy as np
import cv2
from img_gradient import img_gradient

def orientations(keypoints, gaussian_pyr, num_bins=36, window_size=16):

    bin_width = 360 / num_bins  
    orientations = []

    for x, y, octave in keypoints:
        img = gaussian_pyr[octave][0]  
        magnitude, orientation = img_gradient(img)  
        histogram = np.zeros(num_bins, dtype=np.float64)
        radius = window_size // 2

        gaussian_window = cv2.getGaussianKernel(window_size, window_size / 6)
        gaussian_window = gaussian_window * gaussian_window.T  

        for i in range(-radius, radius):
            for j in range(-radius, radius):

                if 0 <= x + i < img.shape[0] and 0 <= y + j < img.shape[1]:
                    angle = orientation[x + i, y + j]
                    mag = magnitude[x + i, y + j]  
                    weight = gaussian_window[i + radius, j + radius]

                    weighted_mag = mag * weight

                    if weighted_mag > 0:
                        bin_idx = int(angle // bin_width) % num_bins
                        histogram[bin_idx] += weighted_mag  

        hist_max = np.max(histogram)

        if hist_max > 0:  
            dom_bin = np.argmax(histogram)  
            dom_orientation = dom_bin * bin_width

            orientations.append((x, y, octave, dom_orientation))

    return orientations