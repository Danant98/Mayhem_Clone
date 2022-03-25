"""
Making class vector to make it easier to work with vector objects
"""
# Importing libraries
import numpy as np
# Object class vector
class vector:
    """
    Class vector
    """
    def __init__(self, x, y):
       self.x = x
       self.y = y

    def __add__(self, other):
        """
        Add two vectors
        """
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __sub__(self, other):
        """
        Subtract two vectors
        """
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self
    
    def __mul__(self, c):
        """
        Multiplication between vector and constant c
        """
        self.x = self.x*c
        self.y = self.y*c
        return self

    def __truediv__(self, c):
        """
        Dividing by constant c
        """
        self.x = self.x/c
        self.y = self.y/c
        return self

    def magnitude(self):
        """
        Returning the magnitude of the vector
        """
        mag = np.sqrt(self.x*self.x + self.y*self.y)
        return mag
    
    def Normalize(self):
        """
        Normalize vector
        """
        vec_mag = self.magnitude()
        if not vec_mag == 0:
            return (vector(self.x/vec_mag, self.y/vec_mag))
        else:
            return (vector(1, 1))
    
    def Direction(self):
        """
        Direction of the vector in radians
        """
        angle = np.arctan2(self.x, self.y)
        return angle
    
    def __repr__(self):
        return ("Vector ({},{})".format(self.x, self.y))

def Distance(vec1, vec2):
    """
    Distance between two vectors
    """
    d = np.sqrt((vec2.x - vec1.x)*(vec2.x - vec1.x) + (vec2.y - vec1.y)*(vec2.y - vec1.y))
    return d
