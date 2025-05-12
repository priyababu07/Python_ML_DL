a=33
b=200
if(b>a):
    print("Good")
else:
    print("BYe")


# elase and if combined
a=33
b=200
if(b>a):
    print("Good")
elif a==b:
    print("BYe")

    #Nested if

a=33
b=200
if(b>a):
    print("Good")
    if(b>10):
        print("yay")
elif a==b:
    print("BYe")

#Switch

print("choice \n 1.sub \n 2.mul")
x = int(input("Enter the choice"))
if x is 1:
    print(2+3)
elif x is 2:
    print(2*3)