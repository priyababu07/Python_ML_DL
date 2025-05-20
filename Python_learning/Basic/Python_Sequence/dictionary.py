# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#Store value in a key value pair
#Associative array

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":2020,
  "colorr":["red","white"]
}
print(thisdict)

#Accessing element
print(thisdict["brand"])
print(thisdict["year"])
x = thisdict.get("model")
print(x)
#if we want to get keys
y = thisdict.keys()
print(y)
#only values use .value

#item return as a tuuple
k = thisdict.items()
print(k)
#Key exist look
if "model" in thisdict:
    print("yes")

# no duplication allowed
#len find the no. of items in dictionary
print(len(thisdict))#no duplicate

#datatypes- can have any types of data

print(type(thisdict))
#They are mutatble
thisdict["model"]="bmw"
print(thisdict)
# #also use updatet
# thisdict.update("year":1999)
thisdict["name"]="yutu"
print(thisdict)
#remove we use pop del
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)#last item removel
# del thisdict complete data delete
#thisdict.clear() clears all value
for x in thisdict:#gets the key
    print(x)
for x in thisdict.values():#gets the values
    print(x)
for x,y in thisdict.items():
    print(x,y)
#copy
mydict = thisdict.copy()
print(mydict)
#nested dictionary
myfamily = {"child1":{
    "name":"priya",
    "age": 1,
    "stream":"ai"
}}