#Remove Specific Elements from list
list = ["REd","Green","White","Black","Pink","Yellow"]

print("You have 3 options:")
for i in range(0,len(list)):
    if i%2==0 and i<len(list):
        list.pop(i)
    # print(list)
        
    



print(list)
