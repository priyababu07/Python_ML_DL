def perfect_number(number=6):
    sum=0
    for i in range(1,(number//2)+1):
        if number%i ==0:
            sum = sum+i
    if sum == number:
        print("It is perfect number")
    else:
        print("Not a perfect number")

perfect_number(7)
