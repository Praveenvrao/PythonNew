#some of digits 1st way

'''digit = 12345
mod1 = digit%10
digit = 1234
mod2 = digit%10
digit = 123
mod3 = digit%10
digit = 12
mod4 = digit%10
digit = 1
mod5 = digit%10

print(mod5+mod4+mod3+mod2+mod1)'''

#2nd way

num = int(input("Enter a digit\n"))
sum = 0
while num !=0:
    digit = num % 10
    sum = sum + digit
    num = int(num/10)
print(sum)