#1. Claculator

print("Choice: \n 1.Addition \n 2.Substraction \n 3.Multiplication")
x = int(input("Enter the choice:"))
num1 = int(input("Enter the first digit:"))
num2 = int(input("Enter the second number:"))
if x is 1:
    print(num1+num2)
elif x is 2:
    print(num1-num2)
elif x is 3:
    print(num1*num2)
else:
    print("Invalid")