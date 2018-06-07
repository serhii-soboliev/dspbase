import numpy as np
from math import pi, cos, sin


def dft(x):
    x_len = len(x)
    n = x_len // 2 + 1
    re = np.zeros(n)
    im = np.zeros(n)
    for i in range(0, n):
        for j in range(0, x_len):
            re[i] += x[j] * cos(2*pi*i*j/n)
            im[i] -= x[j] * sin(2 * pi * i * j / n)
    return re, im
