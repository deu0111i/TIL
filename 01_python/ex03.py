class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point({x}, {y})'.format(x=self.x, y=self.y)

class Circle:

    def __init__(self, center, r):
        self.center = center
        self.r = r
    
    def get_area(self):
        result = 3.14 * (self.r)**2
        return '{}'.format(result)
    def get_perimeter(self):
        return '{}'.format(self.r * 2 * 3.14)

    def get_center(self):
        return '({}, {})'.format(self.x,self.y)

    def __str__(self):
        return 'Circle:({}, {}), r:{}}'.format(self.x, self.y, self.r)

if __name__ == '__main__':
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