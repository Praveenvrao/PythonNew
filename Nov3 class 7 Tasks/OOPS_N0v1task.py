#Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods

'''class Cars:
    brand_name = None
    car_color = None
    Car_model_year = None
    Car_model_version = None
    Car_Type = None
    Car_milage = None

    def Car_brand(self):
        print(f'Car brand is {self.brand_name}' )
    def Car_color(self):
        print(f"Color of the car is {self.car_color}")
    def Car_version_year(self, Car_model_year):
        print(f'Car Version and year is {self.Car_model_version} and {Car_model_year}')
    def type_car(self):
        print('Car type is ', self.Car_Type)
    def Car_condition(self):
        if self.Car_milage > 25:
            print(f'Car condition is good with {self.Car_milage} milage')
        else:
            print(f'Car condition is  not good at all with {self.Car_milage} milage')


Car1 = Cars()

Car1.brand_name = input("Enter the name of the car brand\n")
Car1.Car_Type = input("Enter the type of car\n")
Car1.car_color = input("Enter the color of car\n")
Car1.Car_model_year = input("Enter the model year of car\n")
Car1.Car_model_version = input("Enter the model version of car\n")
Car1.Car_milage = int(input("Enter the milage of car\n"))

Car1.Car_brand()
Car1.Car_color()
Car1.Car_version_year(Car_model_year=Car1.Car_model_year)
Car1.type_car()
Car1.Car_condition()

Car2 = Cars()

Car2.brand_name = input("Enter the name of the car brand\n")
Car2.Car_Type = input("Enter the type of car\n")
Car2.car_color = input("Enter the color of car\n")
Car2.Car_model_year = input("Enter the model year of car\n")
Car2.Car_model_version = input("Enter the model version of car\n")
Car2.Car_milage = int(input("Enter the milage of car\n"))

Car2.Car_brand()
Car2.Car_color()
Car2.Car_version_year(Car_model_year=Car2.Car_model_year)
Car2.type_car()
Car2.Car_condition()'''


#Create a Class Person , Two Objects by taking (name, age, address) Input from users and print details in the end.

class Person:
    name = None
    age = None
    address = None

    def Person_name(self):
        print(f'Name of the person is {self.name}')
    def Person_age(self):
        print(f'Age of the person is {self.age}')
    def Person_address(self):
        print(f'Address of the person is {self.address}')


Person1 = Person()

Person1.name = input('Enter the name\n')
Person1.age = input('Enter the age\n')
Person1.address = input('Enter the address\n')

Person1.Person_name()
Person1.Person_age()
Person1.Person_address()


Person2 = Person()

Person2.name = input('Enter the name\n')
Person2.age = input('Enter the age\n')
Person2.address = input('Enter the address\n')

Person2.Person_name()
Person2.Person_age()
Person2.Person_address()
