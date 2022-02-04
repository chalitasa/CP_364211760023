# Dictionary key:value

# example
car = {'brand':'toyota','model':'vios','year':2021}

#access to data in dictionary
print(car)
print(type)
print(len)

# key
print(car['brand'],type(car['brand'])) # toyota
print(car['model'],type(car['model'])) # vios
print(car['year'],type(car['year'])) # 2021

# get()
print(car.get('brand'))
print(car.get('model'))
print(car.get('year'))

# access to keys in dictionary
x = car.keys()
print(x)
print(type(x))

# access to values in dict
x = car.values()
print(x)
print(type(x))

# items()
x = car.items()
print(x)
print(type(x))

# loop
for x in car:
    print(x)  # --> keys
for x in car:
    print(car[x]) # --> values

# use keys() with loop
for x in car.keys():
    print(x) # --> keys
# use values() with loop
for x in car.values():
    print(x)
# items() with loop
for x,y in car.items():
    print(x,y)

# in keyword
if 'color' in car:
    print('color is a key in dict.')
else:
    print('There hes no color key in dict.')

# change data in dict
print(car)
car['model'] = 'Altis'
print(car)
# update()
car.update({'year':2022})
print(car)

# add data to dict
print(car)
# add color = 'Red' to dict
car['color'] = 'Red'
print(car)
# update()
car.update({'price':'900k'})
print(car)

# remove data in dict
# pop()
if 'price' in car:
    car.pop('price')
else:
    print('Dict has no key--> "price".')
print(car)
# popitem() --> remove last item
car.popitem()
print(car)
# del keyword
del car['year']
print(car)
# del car
# print(car) # error
# clear()
car.clear()
print(car)
