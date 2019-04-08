import math

class Circle(object):
    """A class to store information about a circle"""
    
    def __init__(self, radius, diameter=1):
        """Return a Circle object whose *radius* is radius"""
        self.radius = radius
        self.diameter = self.radius * 2

    @classmethod
    def from_diameter(self, diameter, radius=1):
        """Alternate constructor with diameter passed in"""
        self.radius = diameter / 2
        self.diameter = diameter
        return self

    @property
    def diameter(self):
        """Return the diameter of the Circle"""
        print("called getter")
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter of the Circle and update the
        radius to be half of the set diameter"""
        print("called setter")
        self.radius = diameter / 2
        self._diameter = diameter
        self._area = math.pi * (self.radius * self.radius)

    def area(self):
        """Calulates and returns the area of the Circle"""
        return (math.pi * (self.radius * self.radius))