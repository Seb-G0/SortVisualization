from random import randint
class Array:
    def __init__(self, values=None, length = 25, max = 1000000):
        self.length = length
        self.max = max
        self.data = None
        self.generate()
        if values is not None:
            self.data = values
            self.length = len(values)
        else:
            self.generate()


    def generate(self):
        data = [randint(0, self.max) for _ in range(self.length)]
        self.data = data
        return data

    def getData(self):
        return self.data

    def __repr__(self):
        return str(self.data)

    def copy(self):
        return self.data[::]

    def __len__(self):
        return self.length



