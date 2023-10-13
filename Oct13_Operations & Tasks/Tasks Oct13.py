# TASK1
# 1.Explain the difference between the = operator and the == operator in Python.
# "=" is assignment operator which is used to assign values/variables,, "==" is comparison operator which is used to compare variables/values

# 2.What does the ** operator do in Python, and how is it used?
# The ** operator is used for exponentiation also known as "Power" operator

# 3.What does the ^ operator do in Python, and in what context is it commonly used?
# "^" is the bitwise XOR (exclusive OR) operator. It performs a bitwise XOR operation on the binary representations of two numbers.
# It will take binary values and execute XOR operation, Below is the example

x = 7 # 0111
y = 9 # 1001
print(x^y)

----------------------------------------------------------------------------

# TASK2
# 1.Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
r = int(input("Enter the radius of circle \n"))
π = 3.14
area = π*(r**2)
print(area)

# 2.Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))

if a>b:
    print("a is greater than b")
elif a<b:
    print("a is lessthan b")
else:
    print('a is equal to b')

# 3. Use the ternary operator to find the maximum of three numbers entered by the user.
j = float(input('Enter the 1st number\n'))
k = float(input('Enter the 2nd number\n'))
l = float(input('Enter the 3rd number\n'))

max_value = j if (j>k and j>l) else (k if (k>l) else l)
print(max_value)

#4.Develop a Python script that calculates the square and cube of a given number

s = float(input("Enter the number \n"))
print(f'Square of {s} is {s**2}')
print(f'Cube of {s} is {s**3}')



