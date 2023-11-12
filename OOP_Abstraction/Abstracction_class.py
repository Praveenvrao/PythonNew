from abc import ABC,abstractmethod

class Vehicle:
    def __init__(self,n):
        self.No_tyres = n

    @abstractmethod
    def start(self,Key):
        print('Nothing, Just it is abstarct Class')
    def display(self,speed):
        print(f'Display the {speed} ')


