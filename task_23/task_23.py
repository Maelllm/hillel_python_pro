from random_word import RandomWords


class CustomMap:
    def __init__(self, dict1: dict, func1, func2):
        self.pointer = 0
        self.dict1 = dict1
        self.func1 = func1
        self.func2 = func2
        self.keys = list(dict1.keys())

    def __next__(self):
        if self.pointer == len(self.dict1):
            raise StopIteration()
        result = (self.func1(self.keys[self.pointer]), self.func2(self.dict1[self.keys[self.pointer]]))
        self.pointer += 1
        return result


custom_map = CustomMap({2: 3, 1: 2}, lambda x: x ** 3, lambda x: x ** 2)
custom_map_2 = CustomMap({"test": 2, "test_2": 3, "some_test": 4}, lambda x: x.upper(), lambda x: x ** 2 - 1)

print(next(custom_map))
print(next(custom_map))

print(next(custom_map_2))
print(next(custom_map_2))
print(next(custom_map_2))


def custom_generator(number: int) -> str:
    if number > 10_000:
        return "Max value is 10_000. Try another"
    pointer = 0
    words = RandomWords()
    unique = []
    while pointer < number:
        word = words.get_random_word()
        if word in unique:
            continue
        unique.append(word)
        pointer += 1
        yield word


a = custom_generator(50)

for i in a:
    print(i)
