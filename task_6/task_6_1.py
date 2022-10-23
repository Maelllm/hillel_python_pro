class frange:

    def __init__(self, *args):
        if len(args) == 1:
            self.start, self.stop, self.step = 0, args[0], 1
        elif len(args) == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif len(args) >= 3:
            self.start, self.stop, self.step = args[0], args[1], args[2]

    def __iter__(self):
        return self

    def __next__(self):
        if self.step <= 0:
            if self.start <= self.stop:
                raise StopIteration('Done.')
        else:
            if self.start >= self.stop:
                raise StopIteration('Done.')
        first_element = self.start
        result = self.start + self.step
        self.start = result
        if first_element == result - self.step:
            return first_element
        else:
            return result - self.step


if __name__ == '__main__':
    for i in frange(1, 100, 3.5):
        print(i)
