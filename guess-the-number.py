import random
guess=0
play="yes"

def user_guess():
    guess=int(input("Enter your guess: "))
    return guess

def play_again():
    play=input("Do you want to play again ?")
    play=play.lower()
    while play not in["yes", "no"]:
        play=input("please answer with yes or no: ")
    return play

while play=="yes":

    number=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100, can you guess it ?")
    guess=user_guess()
    while guess!=number:
        if guess>number:
            print("Too high !")
            guess=user_guess()
        else:
            print("Too low !")
            guess=user_guess()

    print("Congrats, you win ! :)")

    play=play_again()

if play=="no":
    print("Okay ! Have a nice day !")


