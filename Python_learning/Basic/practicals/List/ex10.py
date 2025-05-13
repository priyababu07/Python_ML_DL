n = int(input("Enter the length "))
list1=[]
for i in range(0,3+1):
    k = input("Enter the element for the list")
    list1.append(k)
for x in list1:
    if len(x)>=n:
        print("They are longer words",x)
    else:
        print("Sorry")