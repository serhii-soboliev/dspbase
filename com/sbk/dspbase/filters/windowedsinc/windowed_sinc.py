import numpy as np
from math import sin, pi

from com.sbk.dspbase.filters.blackman import blackman_kernel


def sinc(cut_off=0.14, kernel_length=100):
    t = np.linspace(start=-kernel_length / 2, stop=kernel_length / 2, num=kernel_length * 10)
    x = np.sin(2 * pi * cut_off * t) / t * pi
    return t, x


def blackman_windowed_sinc(cut_off=0.14, kernel_length=100):
    bk = blackman_kernel(filter_length=kernel_length * 10)
    t, x = sinc(kernel_length=kernel_length, cut_off=cut_off)
    return t, x * bk


def blackman_windowed_sinc_normalized(cut_off=0.14, kernel_length=100):
    t, x = blackman_windowed_sinc(kernel_length=kernel_length, cut_off=cut_off)
    x = x / np.sum(x)
    return t, x
