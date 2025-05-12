pos=0
neg=0
zero=0
for i in range(1,10):
    number = int(input("Enter the number"))
    if number>0:
        pos=pos+1
    elif number<0:
        neg=neg+1
    else:
        zero=zero+1
print("POsitive count",pos)
print("Negative count",neg)
print("Zero count",zero)
