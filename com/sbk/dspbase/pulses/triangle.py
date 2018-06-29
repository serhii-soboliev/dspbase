import math
import numpy as np


def triangle_pulse(signal_length=512,  peak_height=32, peak_angle_radian=math.pi/4, shift=0):
    t = np.zeros(signal_length)
    b = peak_height * np.arctan(peak_angle_radian)
    t[int(shift):int(shift+b)] = np.linspace(start=0, stop=peak_height, num=b)
    ramp_start = int(shift+b)
    ramp_end = int(shift + 2*b)
    t[ramp_start:ramp_end] = np.linspace(start=peak_height, stop=0, num=ramp_end-ramp_start)
    return t

