# method return a shallow copy of the list
import copy
list = [4,6,9,2,4]
list1 = list.copy()
print(list1)

#example 1
list2 = ['cat','dog','cartoon','dear']
list3 = list2.copy()
print(list3) # ['cat', 'dog', 'cartoon', 'dear']

#example
letters = []
letters.append('l')
letters.append('r')
letters.append('n')
print(letters) # ['l', 'r', 'n']
new_letters = letters.copy()
new_letters.reverse()
print(new_letters) # ['n', 'r', 'l']

