import unittest

from com.sbk.dspbase.signals.sinus import Sinus

class TestSinus(unittest.TestCase):

    def setUp(self):
        pass

    def test_build_sinus_wave(self):
        s = Sinus.build_sin_waves(3,3,4,5)