# the specified element appears in the list
#list_name.count(index)

numbers = [2, 3, 5, 2, 11, 2, 7,5,5,7,8,9,8,5,6,5,7,5,8,5,8,]
list = numbers.count(5)
print(list) # 7


#example 1
letters = ['h','h','k','a']
letter = ['a','e','r','h','k']
letters.extend(letter)
print(letters) # ['h', 'h', 'k', 'a', 'a', 'e', 'r', 'h', 'k']
letters.append('r')
letters.append('e')
print(letters) # ['h', 'h', 'k', 'a', 'a', 'e', 'r', 'h', 'k', 'r', 'e']
count = letters.count('r')
print(count)



#example 2

