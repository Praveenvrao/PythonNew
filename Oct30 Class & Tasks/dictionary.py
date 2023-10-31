dict1 = {"Vikram":'Kamal', "LEO": 'Vijay', "Khaidhi":'Karthi', "Vikram": 'Kamal & Fahad'}

print(dict1)
print(len(dict1))
print(dict1.get('Vikram'))
print(dict1['LEO'])
dict1edit = dict1.copy()
print(dict1edit)

dict2 = dict(RRR='SSR', PUSHPA='SUKUMAR', LIGAR='PURI')
print(type(dict2))
print(dict2.keys())
print(dict2.values())
print(list(dict2.keys()))  #to get the keys in list format
print(list(dict2.values())) #to get the values in list format
keylist = list(dict2.keys())
Valueslist = list(dict2.values())
print(keylist[2])
print(Valueslist[0])
print(dict2['LIGAR'])

#Converting dict into set
dict1 = {"Vikram":'Kamal', "LEO": 'Vijay', "Khaidhi":'Karthi', "Vikram": 'Kamal & Fahad'}

print(dict1.items())
dicttoset = set(dict1.items())
print(dicttoset)

#pop item
#pop1 = dict2.pop("RRR") #pop to remove specific arg
#popitem1 = dict1.popitem()  #pop item to remove any item randamly
#print(pop1)
#print(popitem1)

#iterating key and values through for loop

for key, values in dict1.items():
    print(key, values)
    print(key)
    print(values)

dict3 = {"Vikram":'Kamal', "LEO": 'Vijay', "Khaidhi":'Karthi'}
print(dict3)
del dict3
#print(dict3)

#Ordered dict

from collections import OrderedDict
od1 = OrderedDict()
od1['a'] = 'NTR'
od1['b'] = 'RAM'
od1['c'] = 'PRABHAS'

od = list(od1)
print(od1)
print(od)

