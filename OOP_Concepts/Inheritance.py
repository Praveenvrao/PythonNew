#Create class and methods in it, Do a inheritance, inherit methods and attributes, Override method and attributes

class Human:
    def __init__(self, Name, Address):
        self.num_eyes = 2
        self.num_nose = 1
        self.name = Name
        self.address = Address

    def Can_see(self):
        print(f'I am {self.name} and I can see with my {self.num_eyes} eyes ')
    def Can_smell(self,food):
        print(f'I am {self.name} and I can smell any {food} with my {self.num_nose} Nose ')
    def work(self):
        print('I can work')

obj1 = Human('LUCKY','HYD')
obj1.Can_see()

#Inheritance
class Human0(Human): #inheritated class 1
    print()

h0 = Human0('Pavan','BNGLR')
h0.work()
h0.Can_see()
h0.Can_smell('ANY foooood')


class Human1(Human):  #inheritaed class 2
    def __init__(self,Org): #attributes overriding
        super().__init__('RAHIM','GTR')
        self.company = Org
        self.name = 'DAS'

    def Can_see(self,item): #method overriding
        super().Can_see()
        print(f'I am {self.name} and I can see {item} with my {self.num_eyes} eyes')
    def work(self,Stream):
        super().work()
        print(f'My name is {self.name} and I can do work in {Stream} ')

h1 = Human1('INFY')
print(h1.num_nose)
h1.Can_smell('food')
h1.Can_see('ANY ITEM')