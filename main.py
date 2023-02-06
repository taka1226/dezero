class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()

# ２乗
class Square(Function):
    def forward(self, x):
        return x ** 2

# exp
class Exp(Function):
    def forward(self, x):
        return np.exp(x)


import numpy as np

x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(y))
print(y.data)
