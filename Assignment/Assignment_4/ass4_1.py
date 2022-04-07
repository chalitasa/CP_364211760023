i = int(input("Enter number: "))
count = 0
while count < i:
    if i % 5 == 0:
        print(f'The result is : ', count)
        count = count+5