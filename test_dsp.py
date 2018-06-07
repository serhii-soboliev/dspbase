import unittest

import numpy.testing as npt
from com.sbk.dspbase.dft import dft


class TestDFT(unittest.TestCase):

    def setUp(self):
        self.x_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.x_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_re_im_length_1(self):
        re, im = dft(self.x_1)
        self.assertEqual(re.size, 5)
        self.assertEqual(im.size, 5)

    def test_re_im_length_2(self):
        re, im = dft(self.x_2)
        self.assertEqual(re.size, 5)
        self.assertEqual(im.size, 5)
