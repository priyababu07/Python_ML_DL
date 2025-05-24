def evenno_list(mylist):
    even =[]
    for i in mylist:
        if i%2==0:
            even.append(i)
    return even

print(evenno_list([1,2,3,4]))