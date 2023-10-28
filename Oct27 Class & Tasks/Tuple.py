#Converting tuple into list and list into tuple

t1 = (34,55,55,2,8)
List = list(t1)
print(List)
print(tuple(List))

#Merging of tuples
t1 = (34,55,55,2,8)
t2 = (3,4,5,6,7)
Mixtuple = t1 + t2
Addtuples =(t1,t2)
print(Mixtuple)
print(Addtuples)
print(Mixtuple[3])
print(Addtuples[0][2])

#Search in tuple
t1 = (34,55,55,2,8)
print(34 in t1)
print('Name' in t1)