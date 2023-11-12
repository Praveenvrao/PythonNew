class Universtiy:
    def __init__(self):
        self.university_name = 'JNTUH'
    def ShowDetails(self):
        print(f'Name of the university is {self.university_name}')
class Course(Universtiy):
    def __init__(self):
        Universtiy.__init__(self)
        self.Course_name = 'ENGINEERING'
    def ShowDetails(self):
        super().ShowDetails()
        print(f'Name of my course is {self.Course_name}')
class Branch(Universtiy):
    def __init__(self):
        self.Branch_name = 'EEE'
        Universtiy.__init__(self)
    def ShowDetails(self):
        super().ShowDetails()
        print(f'My Branch is {self.Branch_name}')

class Student(Course,Branch):
    def __init__(self):
        self.Student_name = 'PRAVEEN'
        Course.__init__(self)
        Branch.__init__(self)

    def ShowDetails(self):
        print(f'My Name is {self.Student_name} and my Branch is {self.Branch_name}')
        super().ShowDetails()

class Faculty(Branch):
    def __init__(self,Faculty_sub):
        self.Faculty_name = 'Rakesh'
        self.Faculty_sub = Faculty_sub
        Branch.__init__(self)
    def ShowDetails(self):
        print(f'I Teach {self.Faculty_sub} subject')
        super().ShowDetails()

Obj1Student = Student()
print(Obj1Student.Student_name)
print(Obj1Student.Branch_name)
print(Obj1Student.Course_name)
Obj1Student.ShowDetails()

Obj1Fac = Faculty('Machines')
Obj1Fac.ShowDetails()

