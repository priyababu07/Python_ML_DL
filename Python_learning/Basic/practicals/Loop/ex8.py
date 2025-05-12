num = int(input("Enter the number"))
for i in range(1,num+1):
    if num%i ==0:
        flag = 0
    else:
        flag=1
if flag==0:
    print("Not a prime number")
else:
    print("prime number")