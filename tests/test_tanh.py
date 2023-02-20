# import sys
# sys.path.append('../')

import unittest
import numpy as np
from dezero import Variable
import dezero.functions as F
from dezero.utils import numerical_diff


class TanhTest(unittest.TestCase):
    def test(self):
        x = Variable(np.array([1.0, 2.0]))
        f = F.tanh
        y = f(x)
        y.backward(create_graph=True)
        gx = x.grad
        expected = numerical_diff(f, x)
        flg = np.allclose(x.grad.data, expected)
        self.assertTrue(flg)
