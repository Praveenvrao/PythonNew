#Creating set in different ways
set1 = set()
set2 = {1,2,3,33,22,3322,33}
set3 = set('Name')
print(set1)
print(set2)
print(set3)

#Converting tuple and list into set
list1 = [34,55,55,2,8]
print(set(list1))

t1 = (3,4,5,7,7,5,4,3)
print(set(t1))

#Set - Unions, Intersection, Subset, superset

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s2.intersection(s1))
s3 = {1,2,3,4,5,6,7,8,9}
s4 = {1,2,3,4}
print(s3.issuperset(s4))
print(s4.issubset(s3))

print(s4.issuperset(s3))
print(s3.issubset(s4))

#Remove & Pop in set

sett = {1,2,3,4,5,6,7}

sett.remove(2)
print(sett)
sett.pop()
print(sett)