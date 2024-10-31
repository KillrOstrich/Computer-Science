import random
print("Welcome to <insert creative title>!")
print("\nWe start off in the fictional hellscape known by the name of New Jersey.")
print("Your only job is to escape.")

money = 16.49
ski_mask = False
apples = 0
savings_money = 8276.98
cargo_plane = False
def end_1():
    print("You fail to even wake up, and have no hope of leaving New Jersey.")  #New Jersey truly is an awful place
    print("ending 1")
    exit()

def end_2():
    print("You forgot about the 9 bottles of lighter fluid you left in the oven, a rookie mistake.")
    print("Ending 2")
    exit()

def end_3():
    print("You die of old age while the teller goes on and on about credit score and interest.")
    print("Ending 3")
    exit()

def end_4():
    print("You fail to rob the bank, and get arrested.")
    print("Ending 4")
    exit()

def end_5():
    print("You fail to escape.")
    print("Ending 5")
    exit()

def end_6():
    print("You become the Rat King.")
    print("Secret ending")
    exit()

def end_7():
    print("You leave New Jersey, and enter New York.")      #I don't know how much better New York is
    print("True ending")
    exit()

def end_8():
    print("You go home and take a nap.")
    print("Ending 8")
    exit()

def end_9():
    print("you live a happy life in guam")
    print("Ending 9")
    exit()

def end_10():
    print("You join the aliens and live out the rest of your life in space")
    print("Ending 10")
    exit()

def start():
    print("ACT 1\nYou awake to your alarm clock going off. do you:")
    print("1. try to get out of bed (10 or higher)")
    print("2. hit snooze and go back to sleep")

    choice = int(input("> "))
    if choice == 1:
        a = random.randint(1,20)        #Rolls d20
        print(a)
        if a >= 10:                     #Checks if it rolled greater than or equal to 10
            kitchen()
        else:
            end_1()
    elif choice == 2:
        end_1()
    else:
        print("Invalid answer, try again")
        start()

def kitchen():
    print("After successfully getting out of bed, you go to the kitchen. do you:")
    print("1. Make breakfast (8 or higher)")
    print("2. Leave the kitchen without eating breakfast")

    choice = int(input("> "))
    if choice == 1:
        b = random.randint(1,20)
        print(b)
        if b >= 8:
            garage()
        else:
            end_2()
    elif choice == 2:
        print("You go to the garage without eating")
        garage()
    else:
        print("Invalid answer, try again")
        kitchen()

def garage():
    global choice1
    print("You are in the garage. Pick a vehicle.")
    print("1. 1987 Buick Grand National")
    print("2. 2017 Cadillac Escalade V")
    print("3. 1997 Toyoto Corolla")
    print("4. A mule you have hitched to the wall")

    choice1 = int(input("> "))
    if choice1 < 4:
        street()
    elif choice1 == 4:
        print("That wouldn't have been my choice, but you still continue")
        street()
    else:
        print("Invalid answer, try again")
        garage()

mule_steroids = False

def street():
    global choice1
    print("You can now make your way to one of three destinations:")
    print("1. The store (You have $"+str(money)+")" )
    print("2. The bank")
    print("3. The Lincoln Tunnel (The tunnel that leads out of New Jersey)")
    print("4. The Jets game")                 #both the Jets and Giants are in New Jersey, despite having New York in the name
    print("5. The Giants game")
    print("6. Some guy selling a cargo plane on Facebook Marketplace")
    print("7. Airport")

    choice = int(input("> "))
    if choice == 1:
        if choice1 == 4:                                            #Only shows up if you have the mule
            print("It takes hours to get there due to the mule.")
        store()
    elif choice == 2:
        if choice1 == 4:
            print("It takes hours to get there due to the mule.")
        bank()
    elif choice == 3:
        chance1 = random.randint(1,10)
        if chance1 <= 5:
            mugged()
        else:
            gas_station()
    elif choice == 4:
        jets()
    elif choice == 5:
        giants()
    elif choice == 6:
        plane()
    elif choice == 7:
        airport()
    else:
        print("Invalid answer, try again")
        street()

def store():
    global choice1
    global money
    print("You are at the store. you can buy:")
    print("1. a ski mask ($5.00)")
    print("2. 6 dozen apples ($32.49)")
    print("3. Leave")
    if choice1 == 4:                            #Checks if you have the mule
        print("4. mule steroids ($0.78)")
    
    choice = int(input("> "))
    
    if choice == 1:
        global ski_mask
        if ski_mask == True:
            print("You already have one of these")
            store()
        
        elif money >= 5:                        #Checks if you have enough money before taking it
            print("You buy the ski mask.")
            money = money - 5.00
            ski_mask = True
            print("You now have $"+str(money))
            store()
        else:
            print("You don't have enough money")
        store()
        
    elif choice == 2:
        global apples
        if money >= 32.49:
            print("you buy 6 dozen apples")
            money = money-32.49
            apples += 72
            print("you are now at $"+str(money))
            store()
        else:
            print("you don't have enough money")
        store()
    elif choice == 3:
        street()
        
    elif choice == 4:
        global mule_steroids
        if money >= 0.78:
            print("Your mule is now much faster")
            money = money - 0.78
            print("you are now at $"+str(money))
            choice1 = 2                             #Dialouge unique to the mule choice doesn't show up
            store()

        else:
            print("You don't have enough money")
            store()
    else:
        print("Invalid answer, try again")
        store()

def bank():
    global savings_money
    global money
    print("you are at the bank you can:")
    print("1. take out a loan")
    print("2. rob the bank (10 or higher)")
    print("3. withdraw money ("+str(savings_money)+" in account)")
    print("4. leave")

    choice = int(input("> "))

    if choice == 1:
        end_3()
    elif choice == 2:
        if ski_mask == True:
            a = random.randint(1,20)
            print(a)
            if a >= 6:
                c = random.randint(100,25000)
                print("successfully robbed the bank for $"+str(c)+"!")
                street()
                money += c
            elif a < 6:
                end_4()
        else:
            b = random.randint(1,20)
            print(b)
            if b >= 10:
                d = random.randint(100,25000)
                print("Successfully robbed the bank for $"+str(d)+"!")
                money = money + d
                street()
            else:
                end_4()
    elif choice == 3:
        cash = int(input("How much money do you want to withdraw\n> "))
        if cash <= savings_money:
            money = money + cash
            savings_money = savings_money - cash
            print("Withdrew $"+cash)
            
        else:
            print("not enough money in account.")
        bank()
    elif choice == 4:
        street()
    else:
        print("Inavalid answer, try again")
        bank()

def mugged():
    global money
    print("When you stop at a gas station, you get cornered and one of them asks for all your money")
    print("1. give them all your money")
    print("2. attempt to escape (6 or higher)")

    choice = int(input("> "))

    if choice == 1:
        print("you give them all of your money")
        global money
        money = 0
        lincoln_tunnel()
    elif choice == 2:
        a = random.randint(1,20)
        print(a)
        if a >= 6:
            print("You successfully escape")
            lincoln_tunnel()
        else:
            end_5()
    else:
        print("Invalid answer, try again")
        mugged()

def gas_station():
    a = random.randint(1,10)
    print(a)
    if a >= 5:
        print("When you stop at a gas station, you are knocked unconscious, and wake up in a sewer surrounded by rats")
        print("1. Start talking to the rats")
        print("2. Leave the sewer and continue to the lincoln tunnel")

        choice = int(input("> "))

        if choice == 1:
            end_6()
        elif choice == 2:
            lincoln_tunnel()
    else:
        lincoln_tunnel()

def lincoln_tunnel():
    print("The final showdown; do you:")
    print("1. Leave New Jersey")
    print("2. Go home")

    choice = int(input("> "))

    if choice == 1:
        end_7()
    elif choice == 2:
        end_8()         #The worst ending
    else:
        print("Invalid answer, try again")

def jets():
    print("you go to watch a Jets game, do you:")
    print("1. stay and watch them lose")
    print("2. leave")

    choice = int(input("> "))
    
    if choice == 1:
        print("They lose")
        street()
    elif choice == 2:
        street()
    else:
        print("invalid answer, try again")
        jets()

def giants():
    print("You go to a Giants game, do you:")
    print("1. watch them lose")
    print("2. leave")

    choice = int(input("> "))

    if choice == 1:
        print("They lose")
        street()
    elif choice == 2:
        street()
    else:
        print("Invalid answer, try again")
        giants()

def plane():
    print("You go see the guy selling the cargo plane")
    print("1. buy the plane for $1200")
    print("2. Leave")

    choice = int(input("> "))
    global money
    global cargo_plane

    if choice == 1:
        if money >= 1200:
            money = money - 1200
            
            cargo_plane = True
            street()
        else:
            print("Not enough money")
            street()
    elif choice == 2:
        street()
    else:
        print("Invalid answer, try again")
        plane()

def airport():
    global money
    print("You go to the airport, do you:")
    print("1. buy a ticket to guam ($2407)")
    print("2. Steal a plane (16 or higher)")
    print("3. Leave")

    choice = int(input("> "))

    if choice == 1:
        if money >= 2407:
            money = money - 2407
            fly()
        else:
            print("you dont have enough money")
            airport()
    elif choice == 2:
        a = random.randint(1,20)
        print(a)
        if a >= 16:
            print("You fly to Guam with your new plane")
            fly()
        else:
            end_5()
    elif choice==3:
        street()
    else:
        print("Invalid answer, try again")
    
def fly():
    print("You're in Guam, do you:")
    print("1. Go back")
    print("2. go to different tourist destinations")

    choice = int(input("> "))

    if choice == 1:
        print("you go back home")
        airport()
    elif choice == 2:
        time_machine()
    else:
        print("Invalid answer, try again")
    
def time_machine():
    print("while on a tour, you see a concrete box with lights coming out of a window on the side, do you:")
    print("1. Ignore it and continue")
    print("2. Attempt to break in (4 or higher)")

    choice = int(input("> "))

    if choice == 1:
        guam_2()
    elif choice == 2:
        a = random.randint(1,20)
        print(a)
        if a >= 4:
            box()
        else:
            print("you look at the box, but give up eventually")
            guam_3()
    else:
        print("Invalid answer, try again")
        time_machine()
    
def guam_2():
    print("you continue with the tour guide, and get back to the airport, do you")
    print("1. go home")
    print("2. stay in guam")

    choice = int(input("> "))

    if choice == 1:
        airport()
    elif choice == 2:
        end_9()
    else:
        print("Invalid answer, try again")
        guam_2()
    
def box():
    print("You enter the box and find a machine that you could stand in, do you:")
    print("1. step in")
    print("2. leave the box")

    choice = int(input("> "))

    if choice == 1:
        print("You step in the machine and press the big red button to your left")
        dino()
    elif choice == 2:
        guam_3()
    else:
        print("Invalid answer, try again")
        box()
    
def guam_3():
    print("you leave the box, but can't find the tour guide, do you:")
    print("1. take a nap")
    print("2. attempt to find your way back (10 or higher)")

    choice = int(input("> "))

    if choice == 1:
        print("you are woken up by the tour guide")
        guam_3()
    elif choice == 2:
        a = random.randint(1,20)
        print(a)
        if a >= 10:
            print("you find your tour guide")
            guam_2()
        else:
            rat_king()
    else:
        print("Invalid answer, try again")

def rat_king():
    print("you fall in a hole while looking, and find some weirdo calling himself the rat king, do you:")
    print("1. Steal his crown and become the rat king")
    print("2. leave and keep looking")

    choice = int(input("> "))

    if choice == 1:
        print("You beat him senseless and then put his crown on your head.")
        end_6()
    elif choice == 2:
        print("you find the tour guide")
        guam_2()
    else:
        print("Invalid answer, try again")
        rat_king()

def dino():
    print("The door on the machine closes and after a minute of loud noises, the door opens again.")
    print("You walk out and absolutely nothing looks different")
    print("1. look for the tour guide")
    print("2. take a nap")

    choice = int(input("> "))

    if choice == 1:
        print("You find the tour guide")
        guam_2()
    elif choice == 2:
        guam_1()
    else:
        print("Invalid answer, try again")

def guam_1():
    print("You wake up inside a dark room and see very tall green figures, do you:")
    print("1. ask for them to let you go")
    print("2. accept your fate")

    choice = int(input("> "))

    if choice == 1:
        print("They agree")
        guam_2()
    elif choice == 2:
        end_10()
    else:
        print("Invalid answer, try again")
        guam_1()


    
        



start()