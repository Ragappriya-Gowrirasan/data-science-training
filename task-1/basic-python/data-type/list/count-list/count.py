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
print(count) # 2


#example 2
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
count1 = random.count(('a','b'))
print(count1)


#example 2
random1 = []
random1.append({1})
list1 = [('priya'),{3,6.0},['n'],'r','name']
list2 = [{'names'},['sweet'],'m',{1},{1}]
list1.extend(list2)
random1.extend(list1)
print(random1)
count2 = random1.count({1})
print(count2)
