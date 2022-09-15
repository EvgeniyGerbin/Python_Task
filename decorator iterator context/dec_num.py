import math


class Dec_Sin:

    def __init__(self, func):
        self.func = func

    def __call__(self, x, *args, **kwargs):
        return math.sin(self.func(x))

@Dec_Sin
def sqr(a):
    return a**2

print(sqr(5))
print(math.sin(25))

