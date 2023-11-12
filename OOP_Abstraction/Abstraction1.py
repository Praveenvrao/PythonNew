from Abstracction_class import *

class Bike(Vehicle):
    def __init__(self,n,nt,color):
        Vehicle.__init__(self,n)
        self.bike_number_tyres = nt
        self.Bike_color = color
    def start(self,Key):
        print(f'Bike Start with kick and {Key} ')
    def display(self,speed):
        print(f'The speed of the bike is {speed}')
class Scooty(Vehicle):
    def __init__(self,n,nt,color):
        Vehicle.__init__(self,n)
        self.Scooty_no_tyres = nt
        self.Scooty_color = color
    def start(self,Key):
        print(f'Scooty is self start {Key}')

class Car(Vehicle):
    def __init__(self,n,nt,color):
        Vehicle.__init__(self,n)
        self.car_no_tyres = nt
        self.car_color =color
    def start(self,Key):
        print(f'Car start with Key and Manual {Key} ')
