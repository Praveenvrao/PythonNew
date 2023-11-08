#Multilevel inheritance

class Grandparent:
    def __init__(self,gp_name,gp_address):
        self.gpname = gp_name
        self.gpaddress = gp_address
    def eat1(self):
        print(f'Grandparent {self.gpname} can eat ')

class Parent(Grandparent):
    def __init__(self,p_name,p_address):
        self.pname = p_name
        self.paddress = p_address
    def eat2(self,p2_name):
        print(f'Both Parents {self.pname} {p2_name} can eat ')
    def Parent_work(self):
        print(f'Parents can work for their property')

class Son(Parent):
    def __init__(self,S_name,S_address,gp_name,gp_address,p_name,p_address):
        Grandparent.__init__(self, gp_name, gp_address)
        Parent.__init__(self,p_name,p_address)
        self.sname = S_name
        self.saddress = S_address
    def eat3(self):
        print('Sons can eat')
    def Parent_work(self):
        print("Sons can work for their Parents and grand parents property")


Obj1son = Son('PRAVEEN','HYD','RAMARAO','MLG','RRAO','HNK')
print(Obj1son.saddress)
print(Obj1son.gpname)
print(Obj1son.paddress)
Obj1son.eat1()
Obj1son.eat2('LRAO')
Obj1son.Parent_work()
Parent.Parent_work(Obj1son)

