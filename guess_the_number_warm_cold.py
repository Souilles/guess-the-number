import random
guess=0
play="yes"
from guess_the_number import user_guess, play_again

while play=="yes":

        lives=7
        number=random.randint(1,100)
        print("I'm thinking of a number between 1 and 100, can you guess it ?")
        print("You've got",lives,"attempts")
        guess=user_guess()
        while guess!=number and lives>1:
            if guess>number:
                if guess<number+5:
                    print("Almost there!")
                elif guess<number+10:
                    print("Warm")
                elif guess>number+20:
                    print("Freezing cold!")
                else:
                     print("Cold")    
                lives=lives-1
                print("You've still got",lives,"attempts")
                guess=user_guess()
            
            else:
                if guess>number-5:
                    print("Almost there!")
                elif guess>number-10:
                    print("Warm")
                elif guess<number-20:
                    print("Freezing cold!")
                else:
                     print("Cold")   
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