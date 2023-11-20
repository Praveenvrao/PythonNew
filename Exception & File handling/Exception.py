#Exception

try:
    a = int(input('Enter a number'))
    b = int(input('Enter b number'))
    c = a/b
    print(c)
except Exception as z:
    print(f'You entered wrong number {z}')


