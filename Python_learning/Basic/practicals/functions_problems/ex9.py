def prime_or_not(number=13):
    flag = 0
    for i in range(2,50+1):
        if number%i ==0 and i!=number:
            flag = 1
            break

    if flag==1:
        print("It not prime")
    else:
        print("It is prime")

prime_or_not(11)