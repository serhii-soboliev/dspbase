import unittest

from com.sbk.dspbase.pulses.gaussian import gaussian_pulse


class GaussianPulseTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_default_gaussian_pulse(self):
        t1, t2 = gaussian_pulse()
        self.assertEqual(t2.size, 201, "incorrect default gaussian pulse size")
        self.assertAlmostEqual(t2[100], 0.3183098861)
        self.assertAlmostEqual(t2[101], 0.316722309)
        self.assertAlmostEqual(t2[102], 0.3120069)

    def test_max_must_be_close_to_mean(self):
        t1, t2 = gaussian_pulse(mean=5)
        mean_index = t1.tolist().index(5)
        self.assertAlmostEqual(t2[mean_index], max(t2), msg="Gaussian function have to reach maximum at mean point")

    def test_values_outside_deviation_have_to_be_close_to_zero(self):
        t1, t2 = gaussian_pulse()
        out_of_deviation_lower_bound = t1.tolist().index(-1)
        out_of_deviation_highest_bound = t1.tolist().index(1)
        self.assertTrue((t2[0:out_of_deviation_lower_bound] > -0.01).all())
        self.assertTrue((t2[0:out_of_deviation_lower_bound] < 0.5).all())
        self.assertTrue((t2[out_of_deviation_highest_bound:-1] > -0.01).all())
        self.assertTrue((t2[out_of_deviation_highest_bound:-1] < 0.5).all())
