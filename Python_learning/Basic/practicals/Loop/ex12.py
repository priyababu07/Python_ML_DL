number = input("Enter the number")
length = len(number)
total =0
for i in number:
    total= total+int(i)**length
    

if total==int(number):
    print("It is armstrong")
else:
    print("Not an armstrong")