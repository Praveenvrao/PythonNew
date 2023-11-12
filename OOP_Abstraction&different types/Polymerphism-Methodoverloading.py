
#Method overloading
class Calculation:
    def add(self,a,b):
        print(f"Add of 2 numbers is {a+b}")

C1 = Calculation()
C1.add(3,4)

#method overloading with default args
class Calculation:
    def add(self,a,b,c=0,d=0):
        print(f"Add of 2 numbers is {a+b}")
        print(f"Add of 4 numbers is {a+b+c+d}")

C1 = Calculation()
C1.add(3,4,5,6)

#Method overloading with * args
class Calculation:
    def add(self,*args):
        total = 0
        for x in args:
            total = total+x
        print(total)

C1 = Calculation()
C1.add(2,3,4,5,6,7)
