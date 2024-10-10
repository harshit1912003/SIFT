import numpy as np
from img_gradient import img_gradient

def descriptors(keypoints, gaussian_pyr, num_cells=4, num_bins=8, window_size=16):
    descriptors = []
    cell_size = window_size // num_cells
    bin_width = 360 / num_bins  

    for x, y, octave in keypoints:
        img = gaussian_pyr[octave][0]  
        magnitude, orientation = img_gradient(img)

        descriptor = np.zeros((num_cells, num_cells, num_bins))  

        radius = window_size // 2

        for i in range(-radius, radius):
            for j in range(-radius, radius):

                if 0 <= x + i < img.shape[0] and 0 <= y + j < img.shape[1]:
                    mag = magnitude[x + i, y + j]
                    angle = orientation[x + i, y + j]

                    cell_x = (i + radius) // cell_size
                    cell_y = (j + radius) // cell_size
                    bin_idx = int(angle // bin_width) % num_bins

                    descriptor[cell_x, cell_y, bin_idx] += mag

        descriptor = descriptor.flatten()

        descriptor /= np.linalg.norm(descriptor)

        descriptor = np.clip(descriptor, 0, 0.2)

        descriptor /= np.linalg.norm(descriptor)

        descriptors.append(descriptor)

    return np.array(descriptors)