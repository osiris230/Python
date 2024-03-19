class Point:
    def __init__(self, x, y):
        self.x =  x
        self.y = y 

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

p1 = Point