#✅ Grade Calculator:
#Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

Score = int(input('Enter your score\n'))

if Score>= 90 and Score<=100:
    print('Your grade is A')
elif Score>=80 and Score<=89:
    print('Your grade is B')
elif Score>=70 and Score<=79:
    print('Your grade is C')
elif Score>=60 and Score<=69:
    print('Your grade is D')
elif Score>=0 and Score<=59:
    print('Your grade is F')
else:
    print('Entered invalid score')
#-------------------------------------------------------------

#✅ Leap Year Checker:
#Create a program that determines whether a given year is a leap year.A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.

year =int(input('Enter the year\n'))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

#------------------------------------------------------

#✅ Triangle Classifier:
#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

side1 = float(input('Enter length of side1\n '))
side2 = float(input('Enter length of side2\n '))
side3 = float(input('Enter length of side3\n '))

if side1 == side2 == side3:
    print("It's equilateral")
elif side1 != side2 != side3:
    print("It's a Scalene")
else:
    print("It's a isosceles")
