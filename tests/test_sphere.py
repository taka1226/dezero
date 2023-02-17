import sys
sys.path.append('../')

import unittest
import numpy as np
from dezero import Variable
from dezero.utils import numerical_diff


class SquareTest(unittest.TestCase):
    def test(self):
        self.assertTrue(1==1)
