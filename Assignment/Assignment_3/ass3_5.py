def getPTD():
    sumPID = [int(x) for x in input(f'Enter PID : ').split()]
    return sumPID

def getFortune(*var):
    resultlist = []
    for x in var:
        if x % 2 == 0:
            resultlist.append('Your fortune is good')
        else:
            resultlist.append('Your fortune is very good')
    return resultlist

PID = getPTD()
print(f'The data from user: {sum(PID)}')
print(f'The prediction result is: {getFortune(sum(PID))}')