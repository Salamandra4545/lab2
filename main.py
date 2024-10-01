from math import sqrt

class Triangle:

  def __init__(self, catet1, catet2):
    self.catet1 = catet1
    self.catet2 = catet2
    
  def __str__(self):
    return f"{self.catet1} {self.catet2}"

  def calc_hypotenuse(self):
    return sqrt(self.catet1**2 + self.catet2**2)


triangle = Triangle(3, 4)
print(triangle.calc_hypotenuse())

