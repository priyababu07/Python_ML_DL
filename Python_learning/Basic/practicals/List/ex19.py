list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

diff1 = []
for i in list1:
    if i not in list2:
        diff1.append(i)

print("Elements in list1 but not in list2:", diff1)
