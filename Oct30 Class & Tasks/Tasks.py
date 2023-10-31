#Program 1:
#Find the maximum and minimum elements in a tuple.

my_tuple = (15, 8, 25, 36, 42, 10)
maximum = max(my_tuple)
minimum = min(my_tuple)
print(maximum)
print(minimum)

#Program 2:
#Find the intersection and union of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
intersection = set1.intersection(set2)
print(intersection)
union = set1.union(set2)
print(union)

#Program 3:
#Remove duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
set = set(my_list)
print(set)

#Program 4:
#Remove a key-value pair from the dictionary.

dict = {'a':2, 'b':3, 'c':5}
dict1 = dict.pop('a')
print(dict1)
print(dict)

#Program 5:
#Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data
'''{
"bookingid": 2384,
"booking": {
"firstname": "PRAMOD",
"lastname": "Dutta",
"totalprice": 432,
"depositpaid": False,
"bookingdates": {
"checkin": "2022-01-01",
"checkout": "2022-01-01"
},
"additionalneeds": "Lunch"
}
}'''

ticketdetails = {
"bookingid": 2384,
"booking": {
"firstname": "PRAMOD",
"lastname": "Dutta",
"totalprice": 432,
"depositpaid": False,
"bookingdates": {
"checkin": "2022-01-01",
"checkout": "2022-01-01"
},
"additionalneeds": "Lunch"
}
}

print(ticketdetails)
print("Booking id is", ticketdetails.get('bookingid'))
print("checkin details is ", ticketdetails['booking']['bookingdates']['checkin'])
print("checkout details is ", ticketdetails['booking']['bookingdates']['checkout'])

