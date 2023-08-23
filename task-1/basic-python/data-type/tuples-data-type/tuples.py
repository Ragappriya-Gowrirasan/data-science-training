
a = (1,3,4,5,7)
print(type(a))

# len 
print(len(a))

# max
print(max(a))

#min
print(min(a))

#index
print(a.index(4))

# add 2 tuples
c = (8,5,9,0,6,3)
print(a+c)

b = a+c
print(b)

#cound
print(b.count(5))

# change to list as tuple
e = [3,6,8,0,5,4,7,2]

e = tuple(e)
print(e) # same variable change

f = tuple(e)
print(f)

# loop in for
tup1 = (2,4,7,5,6,3,4,5,2,5)
for k in tup1:
    print(k)

tup2 = ('priya')
for r in tup2 :
    print(r)

# mul
tup3c=tup2 * 3
print(tup3c)