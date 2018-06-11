import numpy as np
from math import pi, cos, sin


def dft(x):
    # x_len = len(x)
    # n = x_len // 2 + 1
    n = len(x)
    re = np.zeros(n)
    im = np.zeros(n)
    for i in range(0, n):
        for j in range(0, n):
            angle = 2 * pi * i * j / n
            re[i] += x[j] * cos(angle)
            im[i] += -x[j] * sin(angle)
    return re, im

def i_dft(re, im):
    n = len(re)
    x_len = (n - 1) * 2
    for i in range(0, n):
        re[i] = re[i] / (x_len / 2)
        im[i] = -im[i] / (x_len / 2)
    re[0] = re[0] / 2
    re[n - 1] = re[n - 1] / 2
    x = np.zeros(x_len)
    for j in range(0, n):
        for i in range(0, x_len):
            x[i] += re[j] * cos(2 * pi * i * j / n)
            x[i] += im[j] * sin(2 * pi * i * j / n)
    return x