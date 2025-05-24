# def Sum_all_numbers(*numbers):
#     return sum(numbers)
# print(Sum_all_numbers(1,2,3))

def Sum_all_list(mylist):
    sum = 0
    for i in mylist:
        sum = sum+i
    return sum
    
print(Sum_all_list([1,2,3,4]))
