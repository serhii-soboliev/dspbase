import math

import numpy as np


def gaussian_pulse(signal_length=20, mean=0, deviation=1):
    steps_count = 10
    t1 = np.linspace(start=mean - signal_length / 2,
                     stop=mean + signal_length / 2,
                     num=steps_count * signal_length)
    a = 1 / (deviation * ((2 * math.pi) ** 1/2))
    b = ((t1 - mean) ** 2) / (2 * deviation)
    t2 = a * np.exp(-b)
    return t1, t2
