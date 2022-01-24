#WAP to state a class Triangle with 3 sides as parameters in a, b and c.
#2 functions one for calculating perimeter and other for area.
import math
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        return (self.a+self.b+self.c)
    def area(self):
        s=self.perimeter()/(float)(2.0)
        return (math.sqrt((s)*(s-self.a)*(s-self.b)*(s-self.c)))
    def __str__(self):
        return ("The perimeter of the given triangle is {}m and area is {}sq.metres".format(self.perimeter(),self.area()))

a=int(input("Enter a side:"))
b=int(input("Enter a side:"))
c=int(input("Enter a side:"))
t=Triangle(a,b,c)
print(t)
