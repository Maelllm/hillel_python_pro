class Circle:
    X = 10
    Y = 20
    RADIUS = 5

    @classmethod
    def contains(cls, obj):
        return (obj[0] - cls.X) ** 2 + (obj[1] - cls.Y) ** 2 <= cls.RADIUS ** 2


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return (self.x, self.y)

#For displaying results
a = Point(3, 5)
b = Point(10, 22)

print(Circle.contains(a()))
print(Circle.contains(b()))
