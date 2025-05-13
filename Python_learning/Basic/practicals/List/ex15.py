import random
list = ["REd","Green","White","Black","Pink","Yellow"]

list2=[]
for i in range(0,len(list)):
    number = random.randint(0,len(list)-1)
    list2.append(list[number])
    
print(list2)
