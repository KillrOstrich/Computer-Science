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

def start_over(): #starts over
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

def Death_by_nut(): #1 death
    print("everything went fine... until it didn't!")
    print("you died 1 of 5")
    print("status: Death by Nut")
    start_over()

def surgery(): #decides your weapon
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

def sword(): #3 sword options
    print("In picking the sword you are actually given more options")
    print("There is a great sword, a pair of knives, and a katana.")
    an = input("Your choice >")

    if an.lower() == "great sword":
        print("Heavy, I like it")
        gs()
    
    elif an.lower() == "knives":
        print("ok, light and quick it is.")
        knives()
    
    elif an.lower() == "katana":
        print("weeb")
        katana()
    
    else:
        print("great sword, knives, or katana. try again")
        sword()

def gs(): #the great sword option
    print("You pick up the great sword")
    print("You notice a button on the grip, you press it.")
    print("suddenly the blade erupts in an inferno blaze!")
    fmgs()

def fmgs(): #gs mission finished
    print("So begins your first mission")
    print("kill space bugs")
    print("... wait what?")
    print("Anyway you are deployed into a jungle with normal soldiers")
    print("their is a big bug to your left, and a horde of smaller bugs to your right")
    an = input("which do you go for: the big bug, the horde, or both")

    if an.lower() == "big bug":
        big_bug()

    elif an.lower() == "horde":
        horde_bugs()

    elif an.lower() == "both":
        both_bugs()
    
    else:
        print("big bug, horde, or both. try again")
        fmgs()

def big_bug(): #win
    print("smart, big vs. big. the normal soldier will handle the horde")
    print("Its a struggle but you pull though and beat the big bug")
    print("Then you help the other soldiers kill the horde")
    print("all bugs are clear, victory")
    print("Status: Pest control")
    start_over

def horde_bugs(): #death
    print("You fight the horde, it does not go well")
    print("Your slow great sword allows you to be easily overwelmed")
    print("You somehow beat the horde, but your tired and are pretty beat up")
    print("The big bug dosent care after slaugtering the normal soldiers, and then focusing you")
    print("You both fight, but this time you loose")
    print("You died 2 of 5")
    print("Status: should have thought that though.")
    start_over()

def both_bugs(): #death
    print("You tell the normal soldier to stay back as you take the horde and big bug")
    print("you rush both and immediutly regret your decision")
    print("you call for the soldiers for help only to see them all run away")
    print("You died 3 of 5")
    print("Status: not the brightest")

def knives(): #death
    print("You take the knives and mess with them")
    print("A scientist trys telling you somthing")
    print("you turn to look at her but one of the knives slip and enbeds itself in your leg.")
    print("She's looking at a clipboard and says,")
    print("those knives are choted in nerotoxion so be-")
    print("she looks up")
    print("-careful... oh dear")
    print("you died 4 of 5")
    print("Status: self assassination")

def katana():
    print("You pick up the katana its sharp, like REALLY sharp")
    print("You make the executive decision to not toy with it")
    fmk()

def fmk():
    print("Your first mission is destorying a robot rebellion")
    print("You are deplyed with a large force of soldiers to clear the rebellion")
    print("You stand at the battle feild as robots and humans charge eachother")
    print("In the center back there is a big robot who seems to be commanding the army")
    print("in the mid line are tanks")
    print("And finally in the way back is artillery, but you super human eyes can tell they arnt set up yet however it wont be long")
    an = input("What do you target: the boss, the tanks, or the artillery?")

    if an.lower() == "boss":
        robo_boss()

    elif an.lower() == "tanks":
        robo_tanks()

    elif an.lower() == "artillery":
        robo_arty()

    else:
        print("boss, tanks, or artillery. try again")
        fmk()

def robo_boss():
    print

def robo_tanks():
    print

def robo_arty():
    print

def minigun(): #the minigun
    print("")

def sniper(): #sniper bullet options
    print("")

def fists(): #the fists garentied death
    print("")

def U_sure(): # 1st way to get fists
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

start() #starts game