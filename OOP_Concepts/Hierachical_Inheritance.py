class Person:
    def __init__(self,Pname,PAge):
        self.P_name = Pname
        self.P_Age = PAge

    def Persondetails(self,location):
        print(f'My name is {self.P_name} and age is {self.P_Age} and the location is {location}')

class Student(Person):
    def __init__(self,Pname,PAge,id_number,Stream):
        Person.__init__(self,Pname,PAge)
        self.ID = id_number
        self.Branch = Stream

    def Studentdetails(self,location,year):
        Person.Persondetails(self,location)
        print(f'Student name is {self.P_name} and student stream is {self.Branch} and year is {year}')

class Teacher(Person):
    def __init__(self,Pname,PAge,Teacherid,exp):
        Person.__init__(self,Pname,PAge)
        self.Teach_id = Teacherid
        self.exp_yr = exp

    def Teacherdetails(self,location,Sub):
        Person.Persondetails(self,location)
        print(f'I teach {Sub} with {self.exp_yr} exeperience ')


Obj1St = Student('RAM',22,224,'CIVIL')
print(Obj1St.P_name)
print(Obj1St.P_Age)
print(Obj1St.Branch)
print(Obj1St.ID)
Obj1St.Persondetails('WGL')
Obj1St.Studentdetails('HNK',2018)

Obj1Teach = Teacher('PRATHAP',44,11,13)
print(Obj1Teach.Teach_id)
print(Obj1Teach.P_name)
print(Obj1Teach.P_Age)
print(Obj1Teach.exp_yr)
Obj1Teach.Persondetails('HYD')
Obj1Teach.Teacherdetails('MLG','CSE')


