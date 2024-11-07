import random

mynumber = random.randint(1,101)

def guess_my_number():
    yournumber = 0
    while yournumber != mynumber:
        yournumber = int(input("whats your number?"))
        if yournumber > mynumber:
            print("too high, try again")

        elif yournumber < mynumber:
            print("too low, try again")
    print("congerats you guessed right!")
    restart()

def restart():
    an = input("play again? y/n")
    if an.lower() == "y":
        guess_my_number

    elif an.lower() == "n":
        print("ok")
        restart()
    
    else:
        print("try again, y/n")
        restart()

guess_my_number()