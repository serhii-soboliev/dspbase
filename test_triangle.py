import unittest

from com.sbk.dspbase.triangle import triangle_pulse


class TrianglePulseTestCase(unittest.TestCase):

    def test_default_pulse_with_shift_64(self):
        s = 128
        ph = 60
        x = triangle_pulse(shift=s, peak_height=ph)
        self.assertEqual(x[166], 60)
        self.assertAlmostEqual(x[165], 58.421052631)
        self.assertEqual(x[167], 60)
        self.assertAlmostEqual(x[168], 58.461538461538)


if __name__ == '__main__':
    unittest.main()
