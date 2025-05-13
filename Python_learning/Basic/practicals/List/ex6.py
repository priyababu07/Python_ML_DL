sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


for i in range(len(sample_list)):
    for j in range(0, len(sample_list)-i-1):
        if sample_list[j][1] > sample_list[j+1][1]:
            sample_list[j], sample_list[j+1] = sample_list[j+1], sample_list[j]

print("Sorted list:", sample_list)
