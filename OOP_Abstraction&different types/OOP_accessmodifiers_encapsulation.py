class Student:
    def __init__(self,name,rollno,age):
        self.Name = name
        self._RollNo = rollno
        self.__Age = age

    def display(self):
        print(f'My name is {self.Name} and roll number is {self._RollNo}')
    def get_Age(self):
        print(f'My age is {self.__Age}')
    def set_age(self):
        self.__Age = 100
        print(f'My age is {self.__Age}')
    def _protecteddisplay(self):
        print(f'My rollno is {self._RollNo}')
    def __displayprivatedata(self):
        print(f'My age is {self.__Age}')
    def dispalydata(self):
        self.__displayprivatedata()

class Branch(Student):
    def __init__(self,name,rollno,age,branch):
        self.Branch = branch
        Student.__init__(self,name,rollno,age)

s1 = Student('RAHUL',244,36)
print(s1.Name)
#s1._Student__displayprivatedata()
s1._Rollno = 22222
print(s1._Rollno)
s2 = Branch('ROHIT',222,44,'IT')
print(s2._RollNo)
s2.display()
s1._protecteddisplay()
s1._Student__displayprivatedata()
s2._Student__displayprivatedata()
s1.get_Age()
s1.dispalydata()
s1.set_age()

