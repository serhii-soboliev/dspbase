from numpy import zeros, sin, pi, arange


class Sinus:

    @staticmethod
    def build_sin_waves(sample_rate, *args):
        if len(args) % 2 != 0:
            raise ValueError("Parameters sequence length isn't even")

        t = arange(0,1,1.0/sample_rate)
        s = zeros(sample_rate)
        for i in range(0, len(args), 2):
            amplitude = args[i]
            frequency = args[i + 1]
            s += amplitude*sin(2*pi*frequency*t)
        return s

