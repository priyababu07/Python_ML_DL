list = [1,1,2,2,3,3,56,7,8,7]
list2=[]
for i in list:
    
    if i not in list2:
        list2.append(i)
print(list2)