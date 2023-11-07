class Circle:
    def __init__(self):
        self.π = 3.14
        self.radius = 4

    def c_radius(self):
        Area = self.π*self.radius**2
        print(f'Area of circle is {Area}')
    def c_circumference(self):
        Circumference = 2*self.π*self.radius
        print(f'Circumference of the circle is {Circumference}')

C1 = Circle()
C1.c_radius()
C1.c_circumference()

class CircleEx:
    pi = 3.14
    def __init__(self,radius,length,width):
        self.r = radius
        self.l = length
        self.w = width

    def c_radius(self):
        Area = self.pi*self.r**2
        print(f'Area of circle is {Area}')
    def c_circumference(self):
        Circumference = 2*self.pi*self.r
        print(f'Circumference of the circle is {Circumference}')
    def rectangle_area(self):
        Area_rect = self.l * self.w
        print(f'Area of rectangle is {Area_rect}')

C2 = CircleEx(4,10,2)
C2.c_radius()
C2.c_circumference()
C2.rectangle_area()

C3 = CircleEx(5,2,2)
C3.c_radius()
C3.c_circumference()
C3.rectangle_area()

C4 = CircleEx(5,10,20)
C4.c_radius()
C4.c_circumference()
C4.rectangle_area()

