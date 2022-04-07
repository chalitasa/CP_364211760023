# Assignment_4.1
f = open("A4Q1.txt", 'a')
i = int(input("Enter number: "))
count = 0
while count < i:
    if i % 5 == 0:
        count = count + 5
    f.write(str(count)+'\n')
f.close()

# Assignment_4.2
f = open("A4Q2.txt", 'a')
a = []
while True:
    x = int(input())
    if x == 1:
        break
    a.append(x)
f.write(str(a)+'\n')
f.close()