'''def multipleoflist(a):
    return a[0]*2,a[1]*2,a[3]*2,a[2]*2,a[4]*2,a[5]*2

list = [1,2,3,4,5,6,7]
result = multipleoflist(list)
print(result)

def adding(a,b):
    return a+b
addresult = adding(4,5)
print(addresult)'''

#filetrs
list1 = [1,2,3,4,5,6,7,8,12,9,11]

evenlist = list(filter(lambda n:n%2 ==0,list1))
eventuple = tuple(filter(lambda n:n%2 ==0,list1))
evenset = set(filter(lambda n:n%2 ==0,list1))

print(evenlist)
print(eventuple)
print(evenset)

#map
list2 = [2,3,4,5]

addbytwo_list = list(map(lambda a:a+2,list2))
addbytwo_tuple = tuple(map(lambda a:a+2,list2))
addbytwo_set = set(map(lambda a:a+2,list2))

print(addbytwo_list)
print(addbytwo_tuple)
print(addbytwo_set)

#reduce

from functools import reduce
tuple1 = (1,2,3,4,5)

substractingtuple = reduce(lambda a,d:a-d,tuple1)
substractingtuple1 = reduce(lambda a,d:d-a,tuple1)
addingtuple = reduce(lambda a,b:a+b,tuple1)
multiplytuple = reduce(lambda a,b:a*b,tuple1)

print(substractingtuple)
print(substractingtuple1)
print(addingtuple)
print(multiplytuple)



