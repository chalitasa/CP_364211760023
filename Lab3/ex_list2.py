# list comprehension

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(mylist, len(mylist))

# เลือกข้อมูลจาก mylist
# โดยเลือกเฉพาะข้อมูลที่มากกว่าหรือเท่ากับ 50
newlist = [x for x in mylist if x >= 50]
print(newlist)

# เลือกข้อมูลจาก mylist
# โดยเลือกเฉพาะข้อมูลที่มากกว่าหรือเท่ากับ 50 และ น้อยกว่า 80
newlist = [x for x in mylist if x >= 50 and x < 80]
print(newlist)

# จากข้อมูลใน mylist ให้ทำการเปลี่ยนข้อมูล
# ที่มีค่ามากกว่า 50  เป็น 50 ทั้งหมด
print(mylist)
newlist = [x if x < 50 else 50 for x in mylist]
print(newlist)

# reverse data in list
mylist.reverse()
print(mylist)

# sort list
#low to high
mylist.sort()
print(f'Sort Low to High: {mylist}')
# high to low
mylist.sort(reverse=True)
print(f'Sort High to Low {mylist}')

# join list
x = [10,20,30]
y = ['a','b','c']

z = x+y
print(z)

x.extend(y)
print(x)