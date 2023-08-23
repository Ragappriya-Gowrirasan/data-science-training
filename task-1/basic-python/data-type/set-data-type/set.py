#the set is use to maths
a = {1,3,2,5}
print(type(a)) # <class 'set'>

# empty set
b = set()
print(type(b))

# remove set
# set value remove way
c= set()
c.add(2)
c.add(5)
c.add(9)
c.add(8)
print(c)
c.remove(9)
print(c)

#pop 
# first element remove
c.pop()
print(c)

#clear
c.clear()
print(c)

# extra set add 
c.add(1)
print(c)

# copy
e = {1,6,4,9,0}
e.add(5)
print(e)
f = e.copy()
print(f)

#update
num = {2,3,4,1}
num1 = {5,6,8,9,7,0}
num.update(num1)
print(num)

# deifference
# a - b
a1 = {1,2,3,4,5,6,7}
a2 = {2,5,0,8,7}
a3 = a1.difference(a2)
print(a3)
a4 = a2.difference(a1)
print(a4)

#union 
#set a1 and set a2 unic value print
# a / b
a5 = a1.union(a2)
print(a5)

#intersection 
# a & b
a = {1,2,3,4,5}
b = {4,5,6,7,3,4,3}
a.intersection(b)
print('intersection: ',a)

