num1 = int(input("The first number"))
num2 = int(input("The second number"))

while num2!=0:
    temp= num1%num2
    num1=num2
    num2=temp

print(num1)
