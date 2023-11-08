#Inheriting Attributes

class Mother:
    def __init__(self,address):
        self.name = 'Mom'
        self.address = address

class Father:
    def __init__(self,Vehicle,Address):
        self.name = 'Father'
        self.Address = Address
        self.Vehicle = Vehicle

class Child(Father,Mother):
    def __init__(self,name,address,Vehicle,Address):
        self.myname = name
        Father.__init__(self,Vehicle,Address)
        Mother.__init__(self,address)
    pass

ObjC1 = Child('Praveen','WGL','Honda','HYD')
print(ObjC1.myname)
print(ObjC1.name)
print(ObjC1.Address)
print(ObjC1.address)
print(ObjC1.Vehicle)

#Inheriting Methods
class India:
    def practice(self):
        print('Practicing for cricket match')
    def Home_ground(self):
        print('Playing home match')
class Australia:
    def practice(self):
        print('Practicing for cricket match')
    def away_ground(self):
        print('Playing away match')

class Final(India, Australia):
    pass

Objcricket1 = Final()
Objcricket1.practice()
Australia.practice(Objcricket1) #If we have duplicate methods calling it
Objcricket1.Home_ground()
Objcricket1.away_ground()

#Inheriting both Attributes and methods

class India:
    def __init__(self,ind_jersey_color):
        self.Team1 = 'IND'
        self.ind_num_players = 11
        self.ind_jersey_clr = ind_jersey_color
    def practice(self):
        print('Ind Practicing for cricket match')
    def Home_ground(self):
        print('Playing home match')
class Australia:
    def __init__(self,Aus_jersey_color):
        self.Team2 = 'AUS'
        self.Aus_num_players = 11
        self.Aus_jersey_clr = Aus_jersey_color

    def practice(self):
        print('Aus Practicing for cricket match')
    def away_ground(self):
        print('Playing away match')

class Final(India, Australia):
    Match = 'Grand Final match'
    def __init__(self,ind_jersey_color,Aus_jersey_color,final_ground):
        India.__init__(self,ind_jersey_color)
        Australia.__init__(self,Aus_jersey_color)
        self.total_no_players = 22
        self.Final_ground = final_ground

    def practice(self):
        print(f'practice match done earlier between {self.Team1} and {self.Team2}')
    def tourney_final(self):
        print(f'Playing the tournament {self.Match} in {self.Final_ground} between {self.Team1} and {self.Team2}')

Objfinal = Final('BLUE','YELLOW','HYDERABAD')

Australia.practice(Objfinal)
India.practice(Objfinal)
Objfinal.practice()
Objfinal.tourney_final()









