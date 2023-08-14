# returns the index of thr specified element in the list
# list_name.index(element_name)
animales = ['cat','dog','rabbit','horse']
list = animales.index('rabbit')
print(list) # 2

#exmaple 1
vowels = ['a','e','i','o','u']
print(vowels.index('o')) # 3

#exmaple 2
vegetable = []
vegetable.append('corn') # add 
vegetable.append('mushroom') 
vegetable.append('tomato')
vegetable.append('cucumber')
print(vegetable) # ['corn', 'mushroom', 'tomato', 'cucumber']
vegetable.remove('tomato') # remove
print(vegetable) # ['corn', 'mushroom', 'cucumber']
vegetable[-1] ='carrot' # change
print(vegetable) # ['corn', 'mushroom', 'carrot']
print(vegetable.index('carrot')) # 2


# exmaple 3
#alphabets = ['a','v','g','y','i','o','l']
#list = alphabets.index('v',4)
#print(list)