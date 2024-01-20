from random import shuffle

class Array:
    def __init__(self, values=None, length=25, max_value=25):
        self.length = length
        self.max = max_value
        self.data = None
        if values is not None:
            self.data = values
        else:
            self.generate()

    def generate(self):
        data = [i for i in range(1, self.length + 1)]
        shuffle(data)
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
