a1=['dog' , 'monkey' , 'cat' , 'camel' , 'donkey'] # list animales
print(a1) # ['dog' , 'monkey' , 'cat' , 'camel' , 'donkey'] 
print(a1[1]) # monkey
a1[2] = 10 
print(a1) # ['dog', 'monkey', 10, 'camel', 'donkey']

# negative indexing in python

print(a1[-2]) # camel
a1[-2] = 8
print(a1) # [dog , monkey , 10 , 8 ,donkey]


#slicing of a list

x = ['mango' , 'banana' , 'pineapple' , 'apple' , 'papaya']
print(x) # ['mango' , 'banana' , 'pineapple' , 'apple' , 'papaya']
print(x[1:4]) # ['banana' , 'pineapple' , 'apple']
print(x[-1:-3]) # []
print(x[1:3]) # ['babana' , 'pineapple']
print(x[-1]) #papaya
print(x[-1:2]) # []
print(x[3:-1]) #['apple']
print(x[-2:-4]) #[]

x[1:4] == x[1:3]
print(x) # ['mango', 'banana', 'pineapple', 'apple', 'papaya']


letter = ['a','b','c','d','e','f','g','h']
print(letter[2:6]) #['c', 'd', 'e', 'f']
print(letter[3:]) #['d', 'e', 'f', 'g', 'h']
print(letter[-2:]) #['g', 'h']
















