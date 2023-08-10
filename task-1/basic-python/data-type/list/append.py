#add elements to a list
# add and remove element from a list
#using append() function
#list_name.append()

#example 01
number =[58,32,48,58]
print("before append in numbers: ", number)
number.append(100)
print("after: ", number)

#exmaple 02
letters =['p','q','r','n','s']
print("before append in letters: ",letters)
letters.append('a')
print("after: ",letters)

#exmaple 03: own examlpe
word = []
word.append('n')
print("add new word 1: " , word)
word.append('e')
print("add new word 2: ",word)
word.append('w')
print("add new word 3: ", word)

#exmaple 04
#random =[]
#random.append('priya',5) 
#print("numbers or names: ",random)
#append takes one argunment 

#exmaple 5
number = [2,5,8,1,0,9]
letters =['r','n','s','h']
number.append(letters)
print("different list: ",number)
#[2, 5, 8, 1, 0, 9, ['r', 'n', 's', 'h']]