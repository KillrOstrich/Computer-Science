def start():   # function to start
    st = input("congrats! you have been given the opertunity to become a super soldier. do you accept? >") #y or n Q for first split

    if st.lower() == "yes":
        procide() # the continue path

    elif st.lower() == "no":
        walk_away() # the first ending

    else: # solve errors
        print("awnser yes or no, try again.")
        start() 

def walk_away(): # first ending where you walk away
    print("you say no and walk away.")
    print("status: Chicken") #status of your ending
    start_over() #function to start over

def start_over():
    an = input("would you like to startover? >")

    if an.lower() == "yes":
        start()

    elif an.lower() == "no":
        print("ok")
        start_over()
    
    else:
        print("yes or no, try again")
        start_over()

def procide(): #continues the story
    print("you have consented to become a super soldier")
    an = input("Do you have a peanut allergy? >")

    if an.lower() == "yes":
        print("Okay, just a heads up you may die.")
        Death_by_nut()
   
    elif an.lower() == "no":
        print("Good, there could have been complacations.")
        surgery()
    
    else:
        print("Bruh, y/n simple")
        procide()

def Death_by_nut():
    print("everything went fine... until it didn't!")
    print("you died 1 of 5")
    print("status: Death by Nut")
    start_over()

def surgery():
    print("the procidure went perfectly.")
    print("you are now given options on your weapon.")
    wea = input("Sword, Minigun, or Sniper rifle.")

    if wea.lower() == "sword":
        print("This will end well")
        sword()

    elif wea.lower() == "minigun":
        print("Awwwww yeeeeeaaaaah!")
        minigun()

    elif wea.lower() == "sniper rifle":
        print("Really. you have enhanced speed and strength, and you choose to shoot people from far away?")
        print("you are now practiclly unkillable and you become a sniper!?")
        sniper()
    
    else:
        U_sure()

def sword():
    print("you fight your first mission, it goes well.")
    print("the next even better.")
    print("After a dozen missions you betry the military.")
    print("you start fighting everyone until your the only one left standing")
    print("Status: Menice to society")
    start_over()

def minigun():
    print("")

def U_sure():
    an = input("Are you sure you want to do this?")

    if an.lower() == "yes":
        print("Alright Fists it is then.")
        fists()
    
    elif an.lower() == "no":
        print("ok")
        surgery()
    
    else:
        print("yes or no")
        U_sure()

start()