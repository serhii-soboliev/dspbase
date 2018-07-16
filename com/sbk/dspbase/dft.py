import numpy as np
from math import pi, cos, sin


def dft(x, result_length=None):
    if result_length is None:
        result_length = len(x)
    else:
        result_length = max(len(x), result_length)
    r = np.zeros(result_length)
    r[:len(x)] = x
    x = r
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


def dft_complex(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def fft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 4:
        return np.fft.fft(x)
    else:
        x_even = fft(x[::2])
        x_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        odd = factor[:N // 2] * x_odd
        even_odd = x_even + odd
        return np.concatenate([even_odd,
                               x_even + factor[N // 2:] * x_odd])
