#Remove Specific Elements from list
list = ["REd","Green","White","Black","Pink","Yellow"]
# list.insert(1,"Green")
print("You have 3 options:")
for i in range(0,3):
    num = int(input("Enter the index you want to remove"))
    list.pop(num)


print(list)

