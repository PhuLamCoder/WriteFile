from function import *
list = createlist()
writetofile('test.txt', list)
sumline('test.txt')
sumline = sumline('test.txt')
print(sumline)