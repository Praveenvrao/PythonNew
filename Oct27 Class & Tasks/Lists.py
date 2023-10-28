L1 = [1,2,22,3,44,3,55,66,'Name','Python']
print(L1)
print(len(L1))
L1[2] = 77
print(L1)
L1.append(346)
print(L1)
print(L1.count(3))
L1.remove(1)
print(L1)
print(L1.pop(2))
print(L1)
L1.reverse()
print(L1)
#L1.sort() #sort not possible if we have mixed data types in List
L1.insert(2,99)
print(L1)
L2 = L1.copy()
L2.reverse()
print(L2)
L3 = [23.2,33,66,555,6]
L3.remove(6)
print(L3)
#L3.clear()
print(L3)


