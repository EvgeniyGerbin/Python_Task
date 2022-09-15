a = (2, 4, 5)


def gen_1():
    yield a
    yield str(a)
    yield str(a).replace('(', '').replace(')', '')


for i in gen_1():
    print(i)

print("||||||||||||||||")


def gen_2(n):
    for i in range(1, n):
        if i % 2 == 0:
            yield i


generator = gen_2(10)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


def iterat(*args):
    for i in args:
        for j in i:
            yield j, type(i)


for i in iterat([1, 3], (1, 4), {9, 5}):
    print(i, end=', ')