name = {"priya":"p","harish":"h","varsha":"v"}
print(name)
print(name['priya'])


#  dictionary length
print(len(name))


# change dictionary items
name["priya"]="y" 
print(name) 

# add items to a dictionary

name["nimal"]="n"
print(name)

# remove dictionary items
del name["varsha"]
print(name)

# clear method
name.clear()
print(name)

# membership test
names = {2:"hello",5:"hi","welcome":8}
print(2 in names)

print(5 not in names)

print("welcome" in names)

print("welcome" not in names)

# list as dictionary
list1 = ["name" , "age" , "salary"]
list2 =["priya",23,1000]
print(dict(zip(list1,list2)))

# touple as dictionary
touple1 = ('priya','nimal','vaisu')
touple2 =('pri','ni','va')
print(dict(zip(touple1,touple2)))

 #type
a={}
print(type(a))

#
n = dict([('name','priya'),('age',23)])
print(n)

# nested dictionary
nested= {'name':'p','age':23 ,'fav':['mango','banana'],'language':{'forign':'english','india':'hind','srilanka':'tamil'}}
print(nested['fav'][0])
print(nested['language']['srilanka'])



