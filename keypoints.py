import numpy as np
import cv2
from scipy.ndimage import gaussian_filter
from scipy.ndimage import maximum_filter, minimum_filter

def keypoints(dog_pyr, threshold=0.03):
    keypoints = []
    for octave in dog_pyr:
        for i in range(1, len(octave) - 1):
            prev_img, cur_img, next_img = octave[i - 1], octave[i], octave[i + 1]
            for x in range(1, cur_img.shape[0] - 1):
                for y in range(1, cur_img.shape[1] - 1):
                    patch = np.stack([
                        prev_img[x-1:x+2, y-1:y+2],
                        cur_img[x-1:x+2, y-1:y+2],
                        next_img[x-1:x+2, y-1:y+2]
                    ])
                    
                    pixel = cur_img[x, y]
                    
                    is_max = (np.max(patch) == pixel)
                    is_min = (np.min(patch) == pixel)
                    
                    if (is_max or is_min) and abs(pixel) > threshold:
                        keypoints.append((x, y, i))
    
    return keypoints