# method reverses the element of the list
#list_name.reverse()
numbers = [2,3,8,7,5,9,2]
numbers.sort()
print(numbers) # [2, 2, 3, 5, 7, 8, 9]
numbers.reverse()
print(numbers) # [9, 8, 7, 5, 3, 2, 2]

#exmaple 1
names = []
names.append('priya')
print(names)
list1 = ['harish', 'thuva', 'kaayal']
list2 = ['raam' ,'kavi','siya']
list1.extend(list2)
names.extend(list1)
print(names)
names.reverse()
print(names)

#exmaple 2
system = ['macOs','lunix','windows']
for r in reversed(system):
    print(r)


