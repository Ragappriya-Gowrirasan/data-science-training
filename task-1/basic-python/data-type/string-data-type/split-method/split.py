# method splits a string at the specified separator and returns a list of substrings
name = 'my mom name is piruntha'
print(name.split()) # ['my', 'mom', 'name', 'is', 'piruntha']

text = 'dreamspace academy'
print(text.split(',')) # ['dreamspace academy']

# example 1
text1 = "i'm from mullaitivu"
text2 = text1.split()
print(text2) # ["i'm", 'from', 'mullaitivu']

#example 2
string1 = "i'm priya"
str1 = string1.split(' ')
str2 = len(string1)
print(str2)
print(str1)

#example 3
print('enter your name: ')
names = input()
print('your name is: ',names) 
lenth =len(names) # your name is:  harish
print(lenth) # 6




