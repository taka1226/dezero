import numpy as np
from dezero import Variable
from dezero.utils import get_dot_graph
from dezero.utils import plot_dot_graph
from dezero.utils import numerical_diff
import dezero.functions as F
import math
import matplotlib.pyplot as plt


def sphere(x, y):
    z = x ** 2 + y ** 2
    return z

def matyas(x, y):
    z = 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y
    return z

def goldstein(x, y):
    z = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * \
        (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    return z

def my_sin(x, threshold=0.0001):
    y = 0
    for i in range(100000):
        c = (-1) ** i / math.factorial(2 * i + 1)
        t = c * x ** (2 * i + 1)
        y = y + t
        if abs(t.data) < threshold:
            break
    return y



def main():
    x = Variable(np.array([[1.0, 2.0], [2.0, 3.0]]))
    f = F.tanh
    y = f(x)
    y.backward(create_graph=True)
    gx = x.grad
    expected = numerical_diff(f, x)

    print(gx)
    print(expected)

if __name__ == "__main__":
    main()
