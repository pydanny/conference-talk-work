import math
class Circle(object):

    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius ** 2 *math.pi
        
    def __repr__(self):
        return '{0} as area {1}'.format(
            self.__class__.__name__, self.area()
        )
        
class Ring(Circle):

    def __init__(self, outer, inner):
        # Going up the chain. But especially with multiple inheritance, we risk not
        # properly understanding the inheritance chain
        super(Ring, self).__init__(outer)
        self.inner = inner

    def area(self):
        outer, inner = self.radius, self.inner
        return Circle(outer).area() - Circle(inner).area()
        
class Ring2(Circle):

    def __init__(self, outer, inner):
        # This is more explicit than super because super can ding you on 
        #   Multiple Inheritance.
        # Super can call things outside your inheritance chain.
        # Explicit is better than implicit
        Circle.__init__(self, outer) 
        self.inner = inner
    
    def area(self):
        outer, inner = self.radius, self.inner
        return Circle(outer).area() - Circle(inner).area()

print(Circle(10))
print(Ring(10, 5))
print(Ring2(10, 5))

# child classes are the ones determining the parent controls!

