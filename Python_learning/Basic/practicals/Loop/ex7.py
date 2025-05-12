num = int(input("Enter the limit of numbers you want to find the sum"))
sum_even = 0
sum_odd = 0
for i in range(1,num+1):
    if i%2==0:
        sum_even = sum_even+i
    else:
        sum_odd = sum_odd+i
print("Sum of even number",sum_even)
print("Sum of odd numbers",sum_odd)
