list = [5, 6, 7]
fact = 1
fact1 = 1
per_list = []

for i in list:
    fact = 1
    fact1 = 1
    for j in range(1, i + 1):  
        fact = fact * j
    for k in range(1, i - len(list) + 1):  
        fact1 = fact1 * k
    permut = fact // fact1  
    per_list.append(permut)

print(per_list)

