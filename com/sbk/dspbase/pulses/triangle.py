import math
import numpy as np


def triangle_pulse(signal_length=512,  peak_height=32, peak_angle_radian=math.pi/4, shift=0):
    t = np.zeros(signal_length)
    b = peak_height * np.arctan(peak_angle_radian)
    up_ramp_start = np.int64(shift)
    up_ramp_end = np.int64(shift + b)
    t[up_ramp_start:up_ramp_end] = np.linspace(start=0, stop=peak_height, num=b)
    down_ramp_start = np.int64(shift + b)
    down_ramp_end = np.int64(shift + 2*b)
    t[down_ramp_start:down_ramp_end] = np.linspace(start=peak_height, stop=0, num=down_ramp_end-down_ramp_start)
    return t

