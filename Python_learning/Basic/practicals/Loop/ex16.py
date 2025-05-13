#First pattern
for i in range(1,5):
    for j in range(1,5+1):
      print("*",end="")
    print("\n")
#SEcond pattern
for m in range(1,5):
    for k in range(m):
       print("*",end="")
    print("\n")
# #Third pattern
k = 0

for i in range(1, 5+1):
    for space in range(1, (5-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

  # five
for i in range(1, 6):
    print(str(i) * (2 * i - 1))
#six
for i in range(1, 6):
    
    for j in range(i, 0, -1):
        print(j, end="")
  
    for j in range(2, i + 1):
        print(j, end="")
    print()


