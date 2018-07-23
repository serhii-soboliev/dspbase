from numpy import linspace, zeros, sin, pi


class Sinus:

    @staticmethod
    def build_sin_waves(sample_rate, signal_length, *args):
        if len(args) % 2 != 0:
            raise ValueError("Parameters sequence length isn't even")
        sample_num = signal_length*sample_rate
        t = linspace(start=0, stop=signal_length, num=sample_num)
        s = zeros(sample_num)
        for i in range(0, len(args), 2):
            amplitude = args[i]
            frequency = args[i + 1]
            s += amplitude*sin(2*pi*frequency*t)
        return s

