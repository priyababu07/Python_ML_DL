def remove_duplicate(mylist):
    uni =[]
    for i in mylist:
        if i  not in  uni:
            uni.append(i)
    return uni

print(remove_duplicate([1,1,2,2,34,56,56]))

