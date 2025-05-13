my_list = ['apple', 'banana', 'cherry', 'date']
item = 'cherry'

for i in range(len(my_list)):
    if my_list[i] == item:
        print("Index of", item, "is:", i)
        break
