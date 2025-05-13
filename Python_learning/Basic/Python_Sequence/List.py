# THe element of a list can be object
#they are mutable
#Allow duplicate values
#The items are ordered
#They have index value 

fruits = ["apple","cherry","banana","apple","cherry","banana"]
print(fruits)
#dupliactes can be added
print(len(fruits))#here starting value is 1
#It contain different data types
numbers = [1,2,3,4]
#type()-method-identify this is a list,tuple

print(type(numbers))

#List constructor
list2=list(("apple","cherry","banana"))
print(list2)

#Accessing list item
print(list2[1])
#negative indexing takes value from last
print(list2[-1])

#Slicing
print(list2[2:3])#here 2 is included 3 is excluded
print(list2[::2])#here in between value is took like 0 ,2,4,6,8,10 value take
print(list2[1::2])#it start 1,3,5
print(list2[2::-2])#it takes value 2,0
print(list2[3::-2])#it takes in backward manner

#Check if item exists

if "apple" in fruits:
    print("yes")
#change list item
fruits[1]="kiwi"
fruits[1:3]=["orange","Gapple"]
#Insert item
# fruits.insert()
#append-add item in the end
fruits.append("pineapple")

#extend method to join two list
numbers.extend(fruits)
print(numbers)
#Also list and tuple can be combined
#remove
#pop remove 
numbers.pop(1)
# can use del
#del can be used to completely delete 
#clear method to clear or to get the empty list

#loop through list
for i in range(len(numbers)):
    print(numbers[i])
#While loop
i=0
while i<len(numbers):
    print(numbers[i])
    i=i+1

#sort
fruits.sort()#ascending
#sort
fruits.sort(reverse=True)#descending

#reverse
#copy
mylist = numbers.copy()
print(mylist)
#Join list - +,append
