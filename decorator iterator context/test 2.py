class ListIterator:
    def __init__(self, *args):
        self.args = args
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
            for i in self.args:
                for j in i:
                    return j


x = ListIterator([1, 3, 7], (3, 5, 6 ))

for i in x:
    print(next(x))