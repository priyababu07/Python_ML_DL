#Used to store multiple items
#Collections of unordered balance are ordered
#They are unchangeable
#No indexing
#Duplicates are not allowed
thisset = {"priya","megha","aneena","priya"}#no duplication allowed
print(thisset)

#length
print(len(thisset))
#Can have data of any type of data
#WE use type to find which type of dataset we use
print(type(thisset))

#we have constructor
thisset2 = set((1,2,3,4))
print(thisset2)

#Looping
for i in thisset2:
    print(i)
if 1 in thisset2:
    print("true")
#Adding element
thisset.add("Mango")
print(thisset)
#Update the set - join
mylist = [1,2,3]
thisset.update(mylist)
print(thisset)
thisset.remove("priya")
#pop method removes the last element - it is unordered we cannot predict which we will delete
#.clear() to clear all
# del to delete all theset
for x in thisset:
    print(x)
#combine two set
set1={1,2,3,4}
set2={4,5,6,7,8}
thisset3 = set1.union(set2)
print(thisset3)

#common elements to print intersection_update()
z = set1.intersection_update(set2)
print(z)
print(set1.intersection(set2))
