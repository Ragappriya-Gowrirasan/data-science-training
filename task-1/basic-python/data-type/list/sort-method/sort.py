# method sorts the items of a list in ascending
# list_name.sort()
numbers = [1,3,5,7,9,5,4,3,2]
numbers.sort()
print(numbers)


#example 1
letters = ['r','g','r','o','t','w','s','a']
letters.append('u')
letters.append('b')
print(letters) # ['r', 'g', 'r', 'o', 't', 'w', 's', 'a', 'u', 'b']
letters.sort()
print(letters)


# example 2
vowels = ['i','e','a','u','o']
vowels.sort(reverse=False)
print(vowels) # ['a', 'e', 'i', 'o', 'u']


#example 3
vowels = ['i','e','a','u','o']
vowels.sort(reverse=True)
print(vowels) # ['u', 'o', 'i', 'e', 'a']

# example 4
number = [1,6,3,5,7,9,5,4,3,2]
sorted(number,reverse=True)
print(number) # [1, 6, 3, 5, 7, 9, 5, 4, 3, 2]

#example 5
def number(num):
    return num

random = [2,5,4,7,8,5,9,0]
random.sort(key=number)
print(random) # [0, 2, 4, 5, 5, 7, 8, 9]
