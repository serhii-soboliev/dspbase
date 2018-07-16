import numpy as np


def blackman_kernel(filter_length=5, alpha=0.16):
    t = np.arange(filter_length)
    a0 = (1 - alpha) / 2
    a1 = 1 / 2
    a2 = alpha / 2
    f = a0 - a1 * np.cos(2 * np.pi * t / (filter_length - 1)) + a2 * np.cos(4 * np.pi * t / (filter_length - 1))
    return f
