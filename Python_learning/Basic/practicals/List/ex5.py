#Count Strings with same start and end
list = ['abc','xyz','aba','1221']
count=0
for x in list:
    if len(x)>=2 and x[0]==x[len(x)-1]:
        count = count+1
print(count)
       
        