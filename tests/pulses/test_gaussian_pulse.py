import unittest

from com.sbk.dspbase.pulses.gaussian import gaussian_pulse


class GaussianPulseTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_default_gaussian_pulse(self):
        t1, t2 = gaussian_pulse()
        self.assertEqual(t2.size, 200, "incorrect default gaussian pulse size")
        self.assertAlmostEqual(t2[99], 0.31790824)
        self.assertAlmostEqual(t2[100], 0.31790824)
        self.assertAlmostEqual(t2[101], 0.314713293)

