#They are immutable and ordered
# It allows duplicate values
#The values stored in a tuple can be any type
# Indexed like list

thistuple = (1,2,3,4,1)#they can have duplicate
print(thistuple)

#len()
#tuple((1,2,3)) this is a method output in round brackets
print(len(thistuple))
ptuple = ("abc",1,True)

#type()
print(type(tuple))

#Accessing values
print(thistuple[1])
#Negative indexing
print(thistuple[-1])
#Tuple slicing
print(thistuple[2:3])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

#in keyword
if 1 in thistuple:
    print("TRue")

#Immutable
a=("apple","baba","cherry")
b = list(a)
print(b)
b[1]="kiwi"
c =tuple(b)
print(c)

#Append
#This all are done by converting it into a list bcz

#tuple join
# thistuple=+tuple
# print(thistuple)

#unpacking
#using asterisk(*)
x = ("apple", "banana", "cherry")
a, b, c = x
print(a)  # apple
print(b)  # banana
print(c)  # cherry
x = ("apple", "banana", "cherry", "kiwi", "mango")
a, *b = x
print(a)  # apple
print(b)  # ['banana', 'cherry', 'kiwi', 'mango']
