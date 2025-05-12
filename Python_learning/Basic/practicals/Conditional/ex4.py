#Enter the age of 3 people by user and determine the oldest among them
age1 = int(input("Enter the person 1 age:"))
age2 = int(input("Enter the person 2 age:"))
age3 = int(input("Enter the person 3 age:"))
if age1>age2 and age1>age3:
    print("FIrst person is the oldest")
elif age2>age1 and age2>age3:
    print("Second person is the oldest")
elif age1==age2 and age2==age3:
    print("THey are all same age")
else:
    print("Third person is oldest")
