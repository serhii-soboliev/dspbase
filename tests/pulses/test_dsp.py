import unittest
from math import pi

import numpy as np
import numpy.testing as npt
from com.sbk.dspbase.dft import dft, i_dft


class TestDFT(unittest.TestCase):

    def setUp(self):
        self.x_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.x_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.x_3 = np.zeros(32)
        self.x_3[0] = 32

    def test_re_im_length_1(self):
        re, im = dft(self.x_1)
        self.assertEqual(re.size, 4)
        self.assertEqual(im.size, 4)

    def test_re_im_length_2(self):
        re, im = dft(self.x_2)
        self.assertEqual(re.size, 5)
        self.assertEqual(im.size, 5)

    def test_dft_equal_1(self):
        re, im = dft(self.x_3)
        expected = np.full((16,), 32)
        npt.assert_almost_equal(re, expected)

    def test_dft_i_dft_equal_1(self):
        x = self.build_sinus()

        re, im = dft(x)
        x_restored = i_dft(re, im)
        npt.assert_almost_equal(x, x_restored, decimal=2)

    def build_sinus(self, amplitude=1, freq=10, shift=0, n=64):
        sn = 10000
        st = np.arange(start=0, stop=sn, step=0.1)
        t = st[0:n - 1]
        x = np.sin(2 * pi * freq * t)
        return x
