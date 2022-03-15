def getNumber():
    listA = []
    for x in range(5):
        listA.append(int(input(f'Enter integer [{x+1}]: ')))
    return listA

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The lowest number is: {min(mynum)}')
print(f'The maximum number is: {max(mynum)}')