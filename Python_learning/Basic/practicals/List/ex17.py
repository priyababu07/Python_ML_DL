list = [3,5,7,13,4]
count =0
for i in list:
    for j in range(2,int(i**0.5) + 1):
       if i != j and i%j!= 0:
           count =count+1
if count==len(list):
    print("True")
else:
    print("False")
           