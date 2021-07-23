def createlist() :
    from random import randrange
    arr = []
    for i in range (10) :
        col = []
        for j in range(10) :
            col.append(str(randrange(0,101)))
        arr.append(col)
    return arr
def writetofile(link, list) :
    with open(link, 'w+', encoding = 'utf-8') as file :
        for row in list :
            file.writelines(';'.join(row))
            file.write('\n')
def sumline(link) :
    with open(link, 'r+', encoding = 'utf-8') as file :
        arr = []
        for i in file:
            sum = 0
            i = i.split(';')
            for j in range(len(i)) :
                sum += int(i[j])
            arr.append(sum)
    return arr





