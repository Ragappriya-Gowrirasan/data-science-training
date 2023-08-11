#clear method removes all items from the list
number = [2,6,5,8,9,0]
number.clear()
print(number) #[]

#example 1
#names = ['kali','nali','thusha','risha']
#names.clear('kali')
#print(names)


#example 2: own idea but not method
letters = ['r','s','t','u','v']
numbers = [1,3,5,7,9,8]
name = ['rusha','nihara','pavi','niththi']
list =[letters,numbers,name]
print(list) #[['r', 's', 't', 'u', 'v'], [1, 3, 5, 7, 9, 8], ['rusha', 'nihara', 'pavi', 'niththi']]
list.clear()
print(list) # [ ]

#example 3 
birds = ['crow', 'peacock','owl','duck','parrot']
animals = ['dog','cow', 'horse','sheep','deer']
birds.extend(animals)
print(birds) # ['crow', 'peacock', 'owl', 'duck', 'parrot', 'dog', 'cow', 'horse', 'sheep', 'deer']
birds.clear() 
print(birds) # []

#example 4
list = [{1,4,6} , (2),['1.1','priya',1.1]]
print(list)
del list[:]
print(list)



 


