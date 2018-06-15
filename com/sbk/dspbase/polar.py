import numpy as np


def cart_to_polar(re, im):
    rho = np.sqrt(re ** 2 + im ** 2)
    phi = np.arctan2(im, re)
    return rho, phi
