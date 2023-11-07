class Instructor:
    def __init__(self, ins_Name, ins_Address, ins_Stream):
        self.Name = ins_Name
        self.Address = ins_Address
        self.Stream = ins_Stream
        self.Salary = 100000

Instructor_1 = Instructor('Ram','Wgl','CSE')
Instructor_2 = Instructor('Raj','HNK','IT')
Instructor_3 = Instructor('Pavan','Hyd','ECE')

print(Instructor_1.Address)
print(Instructor_3.Salary)
print(Instructor_2.Name)
print(Instructor_3.Stream)

