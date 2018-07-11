import unittest

import numpy as np

from com.sbk.dspbase.dft import fft


class TestFFT(unittest.TestCase):

    def setUp(self):
        pass

    def test_fft_1(self):
        x = np.random.random(1024)
        self.assertTrue(np.allclose(fft(x), np.fft.fft(x)))