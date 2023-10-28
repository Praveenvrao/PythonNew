#1. Write a Python program to find the largest number in a list.
#2. Write a Python program to find the smallest number in a list.

List1 = [1,2,4,55,66,77,90,3,7]
List1.sort()
print(List1)
small = List1[0]
print(f'Smallest number in the list is {small}')
max = List1[len(List1)-1]
print(f'Max number in the list {max}')

#3. Write a Python program to sum all numbers in a list.

L1 = [1,2,3,4,5,55,6]

def sum_of_list(n):
    Sum = 0
    for i in n:
        Sum = Sum+i
    print("Sum of the list is", Sum)
sum_of_list(L1)

#4. Write a Python program to multiply all numbers in a list.

L2 = [1,2,3,4,5,6]

def Mult_of_list(n):
    Mul = 1
    for i in n:
        Mul = Mul * i
    return Mul

Result = Mult_of_list(L2)
print(f'Multiple of list numbers is {Result}')

#5. Write a Python program to count the number of strings in a list where the string length is 2 or more and the first and last character are the same.

StrList = ['RoleR','ParaP','LeL','Vikram','MGM','MadaM',]

def Count_of_str(CR):
    Count = 0
    for i in CR:
        if len(i) >= 2 and i[0] == i[-1]:
            Count = Count + 1
    return Count

print("Count of strings", Count_of_str(StrList))
