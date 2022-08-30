class Circle:
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, obj):
        return (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= self.radius ** 2

    #For task_6*
    def __contains__(self, obj):
        return (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= self.radius ** 2


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y



#For displaying results

print(Circle(0,10,20).contains(Point(3,5)))

print(Point(42,5) in Circle(0,10,20))