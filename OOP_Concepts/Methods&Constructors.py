class Instructor:
    Salary = 100000
    def __init__(self,ins_name,ins_Address):
        self.name = ins_name
        self.Address = ins_Address
        self.followers = 0
    def fun1(self, Stream):
        print(f'Hi My name is {self.name} and my stream is {Stream} and my Salary is {self.Salary}')
    def update_salary(self):
        self.Salary = 200000
        print(f'Updated salary is {self.Salary}')
    def fun2(self):
        if self.Address == 'Wgl':
            print(f'Instructor is from {self.Address}')
        else:
            print(f'Instructor is not from Wgl instructor from {self.Address}')

Instructor_1 = Instructor('Raj','Wgl')
Instructor_1.fun1('IT')
Instructor_1.fun2()
Instructor_1.update_salary()

Instructor_2 = Instructor('RAM','Hyd')
Instructor_2.fun1('CSE')
Instructor_2.fun2()