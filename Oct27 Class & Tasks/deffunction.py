#Scoping of data

num = 20

def multiplyby_10(n):
    n = n*10
    num = n
    print("The value inside the function",num)
    return

multiplyby_10(num)
print("The value of num outside of the function", num)

#Same program example
num = 20

def multiplyby_10(n):
    n = n*10
    b = n
    print("The value inside the function",b)
    return

multiplyby_10(num)
print("The value of num outside of the function", num)


#List is mutable so we can change

list1 = [1,2,3,4]

def list_multiply_2(n):
    n[0] *= 2
    n[1] *= 2
    n[2] *= 2
    n[3] *= 3

print(list1)
list_multiply_2(list1)
#multlist = list_multiply_2(list1)
print(list1)

#tuple is immutable so we can't change

tuple1 = (1,2,3,4)

def list_multiply_2(n):
    tuple1[0] *= 2
    tuple1[1] *= 2
    tuple1[2] *= 2
    tuple1[3] *= 3

print(tuple1)
list_multiply_2(tuple1)
#multlist = list_multiply_2(list1)
print(tuple1)
