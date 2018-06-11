import numpy as np
from math import pi, cos, sin


def dft(x):
    n = len(x)
    dft_len = n // 2
    re = np.zeros(dft_len)
    im = np.zeros(dft_len)
    for i in range(0, dft_len):
        for j in range(0, n):
            angle = 2 * pi * i * j / n
            re[i] += x[j] * cos(angle)
            im[i] -= x[j] * sin(angle)
    return re, im


def i_dft(re, im):
    dft_len = len(re)
    n = dft_len * 2 + 1
    for i in range(0, dft_len):
        re[i] = re[i] / (n / 2)
        im[i] = -im[i] / (n / 2)
    re[0] = re[0] / 2
    re[-1] = re[-1] / 2
    x = np.zeros(n)
    for j in range(0, dft_len):
        for i in range(0, n):
            angle = 2 * pi * i * j / n
            x[i] += re[j] * cos(angle)
            x[i] += im[j] * sin(angle)
    return x