import random

number = random.randint(1,1000)
print("This is a game to guess random number between 1 to 1000 are you ready \n You only have 3 chances")
for i in range(1,4):
    guess = int(input("Enter the number"))
    if(guess==number):
        print("Great , You won the game")
    elif(guess>number):
        print("Too high,try again")
    else:
        print("Too Low, try again")