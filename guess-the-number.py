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

    lives=7
    number=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100, can you guess it ?")
    print("You've got",lives,"attemptss")
    guess=user_guess()
    while guess!=number and lives>1:
        if guess>number:
            print("Too high !")
            lives=lives-1
            print("You've still got",lives,"attempts")
            guess=user_guess()
            
        else:
            print("Too low !")
            lives=lives-1
            print("You've still got",lives,"attempts")
            guess=user_guess()       
    
    if guess==number:
        print("Congrats, you win ! :)")
    else:
        print("You lost ! The number was",number)

    play=play_again()

if play=="no":
    print("Okay ! Have a nice day !")


