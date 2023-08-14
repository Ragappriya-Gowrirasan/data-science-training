#pop method removes the item at the specified index.
number = [2,4,6,8,0]
remove_element =number.pop()
print(remove_element) # 0
print(number) #[2, 4, 6, 8]

#example 1
animals = ['cat','dog','elephant','pig','monkey']
animals.pop(2)
print(animals) #['cat', 'dog', 'pig', 'monkey']


#example 2
subject = ['maths','science','music','ict','english']
remove = subject.pop()
print(remove) #enlish
print(subject) #['maths', 'science', 'music', 'ict']


#example 3
name =['nisha','risha','kavi','nila','kavitha']
remove = name.pop(2)
print(remove) #kavi
print(name) #['nisha', 'risha', 'nila', 'kavitha']
 
#example 4
letters =['t','y','s','k','r','h']
return_value = letters.pop(-3)
print(return_value) # k
print(letters) #['t', 'y', 's', 'r', 'h']

#example 5
languges =['python','java','ruby','c','c++']
print(languges.pop()) # c++

#exmaple
fruit = ['mango','papaya','pineapple','apple','orange']
print(fruit.pop(-1)) #orange
print(fruit) #['mango', 'papaya', 'pineapple', 'apple']


