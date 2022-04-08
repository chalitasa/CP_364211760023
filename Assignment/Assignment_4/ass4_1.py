i = int(input("Enter number: "))
count = 5
while count <= i:
    if i % 5 == 0:
        print(f'The result is 4: ', count)
        count = count+5