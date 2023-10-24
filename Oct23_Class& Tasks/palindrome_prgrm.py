#Palindrome program

'''given_str = input("Enter input string for palindrome check \n")
def palindrome(input_str):
    Reverse_str = ""
    for char in input_str:
        Reverse_str = char + Reverse_str
    return Reverse_str

result = palindrome(given_str)
if given_str == result:
    print("Polindrome")
else:
    print("Not a polindrome")'''

#Same program
'''def palindrome(input):
    rvr_str =""
    for c in input:
        rvr_str = c + rvr_str
    return rvr_str

print(palindrome('Namak'))'''

#2nd way for polindrome
input_str = input("Enter input string for palindrome check \n")
def palindrome(input_str):
    if input_str == input_str[::-1]:
        print("It's a palindrome")
    else:
        print("Not a palindrome")

palindrome(input_str)






