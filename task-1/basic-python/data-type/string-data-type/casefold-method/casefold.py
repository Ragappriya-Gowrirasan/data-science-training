# method converst all characters of the string into lowercase letters and returns a new string
text = 'LEvel'
text1 = text.casefold()
print(text1)

#example 1
print('enter your pet name: ')
text2 = input()
text3 = text2.capitalize()
print(text3)
print('are you sure. is this your pet name?? ')
text4 = input()
print('your pet name is ', text3.casefold())
