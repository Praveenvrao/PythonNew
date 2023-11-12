#Method overriding

class Father:
    def sleeptime(self):
        print('Sleep timings are 9 PM to 6 AM')

class Son(Father):
    def sleeptime(self):  #Here we are overriding the method
        print('Sleep timings are 11 PM to 8 AM')

S1 = Son()
S1.sleeptime()

#Method overriding with Args


class Father:
    def __init__(self,Place):
        self.Sleepplace = Place
    def sleeptime(self):
        print(f'Sleep timings are 9 PM to 6 AM and will sleep in {self.Sleepplace}')

class Son(Father):
    def sleeptime(self):  #Here we are overriding the method
        print(f'Sleep timings are 11 PM to 8 AM and will sleep in {self.Sleepplace}')
        super().sleeptime()

F1 = Father('Bedroom')
F1.sleeptime()
S2 = Son('Terrace')
S2.sleeptime()

#method overriding args in methods
class Father:
    def sleeptime(self,Place):
        print(f'Sleep timings are 9 PM to 6 AM and will sleep in {Place}')

class Son(Father):
    def sleeptime(self,Place):  #Here we are overriding the method
        print(f'Sleep timings are 11 PM to 8 AM and will sleep in {Place}')
        super().sleeptime('Ground')

F1 = Father()
F1.sleeptime('Bedroom')
S2 = Son()
S2.sleeptime('Terrace')
