'''class Rahul:
    def __init__(self):
        self.Lan = 'Telugu'
        self.Sports = 'Rugbi'
    def Speaks(self):
        print(f'Rahul speaks {self.Lan}')
    def Sports(self):
        print(f'Rahul plays {self.Sports}')

class Surya:
    def __init__(self):
        self.Lan = 'Hindhi'
        self.Sports = 'Sport'
    def Speaks(self):
        print(f'Surya speaks {self.Lan}')
    def Sports(self):
        print(f'Surya plays {self.Sports}')


def display(x):
    x.Speaks()
    x.Sports()
    print('Printed display function')

R = Rahul()  #Arguments with objects not callable in ducktyping
display(R)'''


#Duck typing without attributes

class Rahul:
    def Speaks(self):
        print(f'Rahul speaks Telugu')
    def Sports(self):
        print(f'Rahul plays Cricket')

class Surya:
    def Speaks(self):
        print(f'Surya speaks Hindhi')
    def Sports(self):
        print(f'Surya plays Rugbi')

class Check:
    def display(self,x):
        x.Speaks()
        x.Sports()
        print('Printed display function')

R1 = Rahul()
#display(R1)
#S1 = Surya()
#display(S1)
C1 = Check()
C1.display(R1)