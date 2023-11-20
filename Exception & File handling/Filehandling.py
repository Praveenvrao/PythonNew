f = open('Sampletext.txt', 'r')

#print(f.read())
#print(f.readline())
#print(f.readable())
#print(f.readlines(2))

f1 = open('3rdsample','w')

#print(f1.write('This is second sample file'))
#print(f1.write('This is second line in second sample file'))
#print(f1.write('In this file writing total new words with write function'))
for data in f:
    f1.write(data)

#f2 = open('2ndsample.txt','a')

#print(f2.write('\nAdding new lines with append'))


