op = ['+', '-', '*', '/']
def calculator():
    a = input('Enter A : ')
    b = input('Enter B : ')
    op = input('Enter OP :')
    if op == '+':
        return 'a+b'
    elif op == '-':
        return 'a-b'
    elif op == '*':
        return 'a*b'
    else:
        return 'a/b'

cal = calculator()
print(cal)