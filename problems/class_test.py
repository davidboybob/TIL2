class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'Point:({}, {})'.format(self.x, self.y)


class Circle(Point):
    pi = 3.14
    def __init__(self, center, r):
        self.x = center.x
        self.y = center.y
        self.r = r

    def get_area(self):
        return self.pi * (self.r **2)

    def get_perimeter(self):
        return 2 * self.pi * self.r
    def get_center(self):
        return (self.x, self.y)
    def __str__(self):
        return 'Circl:({},{}), r:{}'.format(self.x, self.y, self.r)
    

p1 = Point(0, 0) 
c1 = Circle(p1, 3) 
print(c1.get_area()) 
print(c1.get_perimeter()) 
print(c1.get_center()) 
print(c1) 
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
print(c2)