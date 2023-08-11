#use the del statemnet to remove one or more items a list
# del_list_name(index_value)
letters = ['a','b','c','d','e','f','g']
del letters[3] 
print(letters) #['a', 'b', 'c', 'e', 'f', 'g']
del letters[-2]
print(letters) #['a', 'b', 'c', 'e', 'g']
del letters[0:3]
print(letters) #['e', 'g'] *****f******
del letters[-1:-5]
print(letters) #['e', 'g'] *****f******


