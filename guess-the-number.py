import random

number=random.randint(1,100)
guess=0

def user_guess():
    guess=int(input("Enter your guess:"))
    return guess

print("Welcome. I'm thinking of a number between 1 and 100, can you guess it ?")
guess=user_guess()
while guess!=number:
    if guess>number:
        print("Too high !")
        guess=user_guess()
    else:
        print("Too low !")
        guess=user_guess()

print("Congrats, you win ! :)")