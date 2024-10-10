import numpy as np

def dog_pyr(gaussian_pyr):
    dog_pyr = []
    for octave in gaussian_pyr:
        dog = [octave[i+1] - octave[i] for i in range(len(octave) - 1)]
        dog_pyr.append(dog)
    return dog_pyr