#method returns true if a string ends with the specified suffix. it not it return false
text = 'PYTHON IS FUN'
print(text.endswith('fun'))

#example 1 
print('type last text lowercase: ')
text1 = input()
text2 = text1.endswith(text1.casefold())
print(text2)

