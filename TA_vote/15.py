print("Welcome to Nightmare at Lock in\n")
friend_1 = input("Before we start choose a name for your first friend\n")
friend_2 = input("And now one for you second friend\n")
print("Alright, let the nightmare being\n")
print("  \n")

def Enter():           #enter school for lock in
    global friend_1
    global friend_2
    print("As you enter the school you spot your friends " + friend_1 + " and  " + friend_2 + " as you enter\n")
    print("You are all excited because you are all attending your school year lock in where all the students stay overnight in the school\n")
    print("The school has set up activites to do and you are deciding where to go first, " + friend_1 + " wants to go see a movie in the gym but " + friend_2 + " want to play games in the seience room\n")
    Act = input(" Do you want to go the gym to watch a movie ( Movie ) or go to the science room to play game ( Game )\n")
    Act = Act.lower()
    if Act == "movie":
        Gym()

    elif Act == "game":
        SciRoom()

    else:
        print(" Hint: try typing the word in the parenthesess\n")
        Enter()

def Gym():                #Go to gym with f1
    print("You decide to go watch a movie with " + friend_1 + ".\n")
    print("As the movie goes on, " + friend_1 + " tap you on your shoulder, they hears something coming for the supply room\n")
    Inv = input(" Do you go investigate (Go) or let " + friend_1 + " go by themself(Stay)\n")
    Inv = Inv.lower()
    if Inv == "go":
        Investigate()
    
    elif Inv == "stay":
        WatchMov()
    
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        Gym()

def SciRoom():               #go to science room with f2
    print("You decide to go play games with " + friend_2 + ".\n")
    print("While playing game, the power goes out\n")
    print(" A group of kids volunteer to go down and fix the power\n")
    Power = input(" Do you go help fix the power (Fix) or let them do it (Stay)\n")
    Power = Power.lower()
    if Power == "fix":
        Fix_Power()
    
    elif Power == "stay":
        Stay_Wait()
    
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        SciRoom()


def  Investigate():         #go investigate with f1
    print("You decide to go investigate with " + friend_1 + ".\n")
    print()
    print("while investigating the noise, you find a hole in the wall where the sound is loudest\n")
    print(friend_1 +  " crawls into it after a bit you hear them scream\n")
    FolF1 = input(" Do you follow " + friend_1 + " into the hole (Follow) or do you go find help (Help)\n")
    FolF1 = FolF1.lower()
    if FolF1 == "follow":
        End1()
    
    elif FolF1 == "help":
        Find_F2()
    
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        Investigate()

def  WatchMov():       #let friend investigate with f1
    print("You stay and watch the movie as your friend goes\n")
    print("After the movie, you realise that " + friend_1 + " never returned.\n")
    print("You go to the supply closet only to find that it’s locked\n")
    FindF1 = input(" Do you look for " + friend_1 + " (Find) or do you go see " + friend_2 + " (Leave)\n")
    FindF1 = FindF1.lower()
    if FindF1 == "find":
        FinF1()
    
    elif FindF1 == "leave":
        SciRoom()
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        WatchMov

def Fix_Power():            #go fix power
    print("You and the group fIx the power and start to head back\n")
    print("You see " + friend_1 + " as you're walking back, they doese’t say anything but gesture for you to follow them\n")
    Go_F1 = input("Do you go with " + friend_1 + ",(Yes) or (No)\n")
    Go_F1 = Go_F1.lower()
    if Go_F1 == "yes":
        print("While you walk, " + friend_1 + " knocks you over the head with a hard object and you fall to the ground, as you fade out of consciousness, you see " + friend_1 + " smile.\n")
        End4()
   
    elif Go_F1 == "no":
        print("You walk back to the sceince room and tell " + friend_2 + " the event of you trip, you decide to go and see " + friend_1 + " with " + friend_2 + "\n")
        SciRoom()
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        Fix_Power()

def End4():        #End 1: die to "f1"
    print("Ending 1: Fall to the hands for a Friend\n")
    print("to be concluded...\n")

def Stay_Wait():      # leave to go see f1 with f2
    print("As you wait, " + friend_2 + " recommend that the two of you go see " + friend_1 + " in the gym\n")
    find_F1()

def find_F1():       #go to gym with f2
    print("Once you make it to the gym you realize, it’s emty except for a faint red light coming from the supply closet\n")
    print("You and " + friend_2 + " enter the supply closet only to find that the light is coming from a hole in the wall, you can hear something coming from the hole\n")
    print( friend_2 + " enter the hole and gestures for you to follow\n")
    FolF2 = input(" Do you follow " + friend_2 + " (yes) or (no)\n")
    FolF2 = FolF2.lower()
    if FolF2 == "yes":
        End3()
    
    elif FolF2 == "no":
        print("Something inside you tell you not to go but you know you can’t leave your friend\n")
        End3()
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        find_F1()

def End3():               #End 3: go into hole with f2
    print("Ending 3: You Enter the hole with " + friend_2)
    print("to be concluded...\n")

def End1():                #End 5 : go into hole with f1
    print("Ending 5: You Enter the hole with " + friend_1)
    print("to be concluded...\n")

def  Find_F2():           #go find f2 to help find f1
    print("You decide to go find " + friend_2 + " for help\n")
    print("As you head to the sceince, the power goes out.\n")
    Power2 = input(" Do you go help fix the power (Fix) or keep heading to the science room (SciRoom)\n")
    Power2 = Power2.lower()
    if Power2 == "fix":
        fix_power()
    
    elif Power2 == "sciroom":
        End2()
    
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        Find_F2

def FinF1():    # try and find f1
    print("You look for a way into the supply closet, you notice the keypad and you remember that you and F1 set a jail break code for the pad so that we could get in secretly\n")
    Enter_Code()

def  Enter_Code():         # enter code to get into supply room
    code = input("Input the Code, Hint: The year you favorite game; fortnite came out\n")
    code = str(code)
    if code == "2017":
        print("<ACCESS GRANTED>\n")
        enter_supply_room()

    else:
        print("<ACCESS DENIED>, try again\n")
        Enter_Code()
        


def End2():       # get captured by the darkness
    print("As you continue to the scince you start to notice thing moving in the dark\n")
    print("Your about to hit the scince room but suddenly something grabs your leg and you hit the ground.\n")
    print("You try to look behind you to see what grab your leg you realise that you can’t moving\n")
    print("You can feel darkness creep over you but you can’t do a thing and eventuly...\n")
    print("Ending 2:Ṫ̶͖̣̩̖̏́̈́h̶͙͇̰̦̄͗̀̃̋̆̎ȩ̴̛̺̣̹͈̇ ̴̩͎͇̮̦̝̽̈́̅͋̃͋̊͝D̸̛͖͚͉̥̣̯́̑̌̃͜ͅą̸̠͉̿r̴̡̪̻̩͝k̴͎̓͌͂̔͆͛͠͝n̸͇̳͇̦̗̭̂͝ͅē̵̢̢̜̺͇̒̅́͝ͅs̶̱̅̈́͆́̆͠͝ś̸̡̭̙̭̖̺̙̼̌̇͂̆̓̄\n")


def fix_power():       #go fix the power alone
    print("You decide to fix the power, as you make your way to the power room, you meet a group for the science room with the same motive so you deside to join them\n")
    Fix_Power()

def enter_supply_room():           # enter supply room
    print("The code works, you make your way into the supply closet and look for " + friend_1 + ", while look you find a hole in a wall, you can hear someone voice from inside the hole\n")
    FolF2 = input(" Do you enter, (yes) or (no)\n")
    FolF2 = FolF2.lower()
    if FolF2 == "yes":
        End5()
    
    elif FolF2 == "no":
        print("Something inside you tell you not to go but you know you can’t leave your friend\n")
        End5()
    else:
        print(" Hint: try typing the word in the parenthesess\n")
        enter_supply_room()


def End5():           # End 4 : enter hole alone
    print("Ending 4:You Enter the hole, Alone\n")
    print("to be concluded...\n")

Enter()