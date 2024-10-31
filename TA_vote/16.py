print("You are a Delta Force operator in 'The Boys' universe, attempting to go on a TTD (Terrorist Take Down)")
print("mission. You and your platoon are riding into the depths of Somolia where it is the most dangerous.")
print("You are riding in a bulletproof humvee with a 50 cal on top, when your brother in arms operating the machine gun is suddenly shot in the neck and killed instantly.")
def entering_somolia():
    print("The driver of the humvee shouts out 'SOMEONE GET ON THAT 50!!!' Do you:")
    print("1. Bravely pull down your deceased commerade and get on the 50 cal where you will most likely take fire and")
    print("have limited protection")
    print("2. Cowardly sit in the humvee where your safety is guaranteed")

    choice1 = input("")

    if choice1 == "1":          # Go on the machine gun
        get_on_50()
    elif choice1 == "2":        # Stay In the truck
        stay_in_humvee()
    else:
        print("Invalid choice. Try again. :( ")
        entering_somolia()


def get_on_50():            # Go on the machine gun
    print("You rip your commerade out of the 50 cal seat and jump up there without hesitation.")
    print("You chamber the ammunition belt and start opening fire on the rooftops, covering your teammates from enemy fire.")
    print("Once you arrive in the center of the city where the suspected terrorist is located, all of his milita men protecting him are dead due to your heavy fire.")
    print("However, you do hear loud commotion inside a tall tower that could potentially house the terrorist. Do you:")
    print("1. Use your current rage and adrenalline to push and clear the tower, without a clue as to what is inside")
    print("2. Wait for backup and an overhead UAV scan to help get some intel and support about what your up against")

    choice2 = input("")

    if choice2 == "1":              # Run in the tower
        rush_in()
    elif choice2 == "2":            # Wait for more support
        wait_for_support()
    else:
        print("Invalid choice. Try again. :( ")
        get_on_50()



def stay_in_humvee():           # Stay in the truck
    print("You decide to not risk your life and stay in the humvee.")
    print("You continue to flinch at the sound of loud lead banging against the humvee walls.")
    print("You barely make it to the center of the city when all the sudden,")
    print("the driver and the rest of your platoon is killed upon exit of the humvee due to the heavy amount of milita men.")
    print("They rip you out of the humvee and are planning to inprison and torture you for American secrets. Do you:")
    print("1. Become a prisoner where you know you will be tortured worse than you can imagine")
    print("2. Quickly grab your pistol and kill yourself, ensuring american secrets remain confidential")

    choice3 = input("")

    if choice3 == "1":          # Become a prisoner
        be_prisoner()
    elif choice3 == "2":        # Kill yourself
        kill_self()
    else:
        print("Invalid choice. Try again. :( ")
        stay_in_humvee


def rush_in():          # Run in the tower
    print("After killing a ton of milita men you fell unstoppable and decide to go balls to the wall and rush in.")
    print("You run in the tower and immediately see a bunch of armed somoli soilders aiming right at you with non other than the dangerous terrorist himself right in the middle.")
    print("You quickly raise your gun and take a shot at the terrorist, while wondering why the soilders where not firing at you, and hit him right in the heart.")
    print("He doesent even flinch, while his skin isin't even peirced.")
    print("He slowly raises his hand up and a ball of electricity starts to form. It gets bigger and bigger.")
    print("He then throws it at you, and as soon as it hits you it explodes, ripping you apart instantly.")
    print("In your last moments you realize why the soilders where not interfearing, while also regretting your decision to have not waited for backup or air support.")
    print("The End. Make sure to play again and try all the endings")


def wait_for_support():         # Wait for more support
    print("You decide to take a minute and wait for some backup.")
    print("Once backup arrives, a UAV scans the tower and sees a bunch of armed and trained soilders along with one individual with a very strange reading.")
    print("The UAV also shows a hidden basement enterance where all of you guys quietly enter from.")
    print("There are noises of what sounds like comotion coming through a vent that startle you, but the vent is just big enough to fit one person. Do you:")
    print("1. Enter the vent and investigate")
    print("2. Throw a grenade into the vent to potentially kill any enemies")

    choice4 = input("")

    if choice4 == "1":          # Enter the vent yourself
        enter_vent()
    elif choice4 == "2":        # Throw a grendade into the vent
        throw_grenade()
    else:
        print("Invalid choice. Try again. :( ")
        wait_for_support()

def kill_self():            # Kill yourself
    print("You decide to make the difficult decision to protect american secrets by ending it all.")
    print("Your sacrifice does not go unheard though. Not allowing the terrorist in on the secrets allowed US forces the upper hand, eventually taking down the terrorist.")
    print("You are awarded the medal of honor and your family is given a grant of millions of dollars.")
    print("Your name and sacrafice is remembered for the next decades to come. You are an american hero.")
    print("The End. Make sure to play again and try all the endings")


def be_prisoner():          # Become a prisoner
    print("You become their prisoner where you are taken deep into the tower and into a old prison cell.")
    print("Once you are in the cell you know you dont have much time before the guards come back with torture devices.")
    print("However, you find a small hole in the wall. You reach in and pull out a small class cylander with a green liquid in it labeled 'TEMP V'.")
    print("With nothing more to lose, Do you:")
    print("1. Ingest the myserious substance")
    print("2. Try to use it against the guards when they return")

    choice5 = input("")

    if choice5 == "1":
        take_substance()            #Inject the substance into yourself
    elif choice5 == "2":
        use_as_weapon()             #Throw the substance at the guards
    else:
        print("Invalid choice. Try again. :( ")
        be_prisoner()


def enter_vent():               # Enter the vent yourself
    print("You squeeze into the tight air vent and begin crawling through closer to the noises.")
    print("You get to a vent grate and look through and standing right below you is the terrorist. Do you:")
    print("1. Call for a danger close precision and cluster airstrike on your location")
    print("2. Request help from the new miliarized superhero program")

    choice6 = input("")

    if choice6 == "1":      # Call in an airstrike
        airstrike()
    elif choice6 == "2":    # Call in Homelander
        superhero()
    else:
        print("Invalid choice. Try again. :( ")
        enter_vent()


def throw_grenade():        # Throw a grendade into the vent
    print("You absolutly lob a grenade into the vent and take cover for the explosion.")
    print("It explodes and you hear a ton of screaming")
    print("You then look down the long vent and see non other than the terrorist, heavily wounded, crawling on all fours at superhuman speed right at you")
    print("You and your team start opening fire with everything you have and it seems to slow him down, but somehow not kill him. Do you:")
    print("1. Retreat back to the humvees")
    print("2. Try to hold your ground and keep firing")

    choice7 = input("")

    if choice7 == "1":      # Retreat back to the humvee
        retreat()
    elif choice7 == "2":    # Keep firing
        hold_ground()
    else:
        print("Invalid choice. Try again. :( ")
        throw_grenade()


def take_substance():           # Inject the substance into yourself
    print("You decide to inject the mysterious substance into yourself with nothing more to lose.")
    print("The guards return to see you in the corner shaking and holding your head.")
    print("They open the cell and grab you to bring you to the torture room.")
    print("But when they try to forcibly grab you, you aren't moved.")
    print("They go to hit you with a metal pole they had in their hand and the pole bent in half.")
    print("You turn around slowly and the guards notice your glowing eyes and take a step back.")
    print("Your eyes start to hurt like a huge hedache and eventually it gets to be to much and you let loose and lazer the guards, cutting them in half instantly.")
    print("You then step out of the cell, walk upstairs, and come face to face with the terrorist and his armed soildiers.")
    print("You absolutely obliterate the soildiers with your lazer vision and it is just you and the terrorist left.")
    print("The terrorist all the sudden creates an electricity ball out of his bare hands, and you and him have an epic superpower abled fight.")
    print("You lazer vison overwhelmes him and you end up lazering his head right off his body.")
    print("You single handedly took down the entire terrorist organization, keeping the world safe.")
    print("The End. Make sure to play again and try all the endings")




def use_as_weapon():            # Throw the substance at the guards
    print("You think that the substance could be used as some sort of weapon and decide to throw it at the guards when they return.")
    print("You throw the liquid at the guard and he is startled, he panics for a second then starts to laugh.")
    print("He then grabs you and sicks a pistol at the back of your head and explains that you just wasted your only option of escape.")
    print("He explains that the mysterious liquid grants you superpowers for a temporary amount of time and that you just wasted it by throwing it at him.")
    print("He then says 'screw it, we got all the information we need' and blows your brains all over the wall. Maybe you should have not wasted your only way of escape.")
    print("The End. Make sure to play again and try all the ending")



def airstrike():        # Call in an airstrike
    print("You call in a danger close airstrike right on your position.")
    print("The second you give your coordinates, crawl as fast as you can out of there.")
    print("As you exit the tower, you hop in the humvee and drive away as the tower competely explodes and is destroyed almost instantaiously.")
    print("Anything once surviving in that tower was now turned into pink mist.")
    print("You and your platoon drive away and radio back to base that the mission was sucsessful.")
    print("You succeed and make it home where you are awarded medals for your bravery.")
    print("The End. Make sure to play again and try all the endings")


def superhero():        # Call in Homelander
    print("You see the large number of guards and are not sure about the strange reading you got from the UAV, so you call in a superheo to help.")
    print("You radio it in a hear the loud tundering noise of the sound barrier being broke.")
    print("Then all of the sudden a supe named Homelander broke through the roof and into the room with the terrorist.")
    print("Homelander a little to comfortably slaughters all of the soilders and just leaves the terrorist.")
    print("You then hear him say that he won't kill him due to the terrorist being 'one of them' and actually trys to help the terrorist.")
    print("You then radio back to base that Homelander changed sides and that you knew this would be a bad idea.")
    print("You are then told that they have a dose of a virus that kills supes, but only one. You then get the dose, do you:")
    print("1. Use the dose on the terrorist")
    print("2. Use the dose on Homelander")

    choice8 = input("")

    if choice8 == "1":          # Kill the terrorist with the virus
        kill_terrorist()            
    elif choice8 == "2":        # Kill Homelander with the virus
        kill_homelander()
    else:
        print("Invalid choice. Try again. :( ")
        superhero()



def retreat():                  # Retreat back to the humvee
    print("You realize that the terrorist is not dying so you call for your team to fall back.")
    print("The terrorist, running on all fours, kills one of your teammates in the back of the group and you procceed to dead sprint to the 50 cal on top of the humvee.")
    print("You get on top of the humvee, load the machine gun, and aim at the basement enterance.")
    print("The terrorist, more like an animal now, appears at the enterance, and right before you fire you say,")
    input("-")
    print("You then blast him with hundereds of 50 cal rounds.")
    print("The bullets are too much for him compared to the AR rounds you fired at him previously and he gets opened up with holes until there is nothing left.")
    print("After that you radio back to base that the mission was sucsessful, and you and your platoon head home to fight another day.")
    print("The End. Make sure to play again and try all the endings")




def hold_ground():          # Hold your ground and keep firing
    print("You decide that you need to put as many rounds as you can in him.")
    print("But things take a turn as the terrorist keep eating the bullets like its nothing.")
    print("He reaches the end of the vent and kills your team, and you realize that maybe you shouldn't of kept firing when he wasan't dying in the first place.")
    print("He then looks at you and jumps at you like a dog, killing you by ripping your face off.")
    print("The End. Make sure to play again and try all the endings")


def kill_terrorist():       # Kill the terrorist with the virus
    print("Since the terrorist is the mission, you fire the dose into him.")
    print("The terrorist skin starts to bubble he starts to cough up blood just as he passes out and dies.")
    print("Homelander, now angry, starts to murder your platoon and you run away.")
    print("You manage to escape have to go into hiding.")
    print("Homelander, being the most powerful superhero, manages to take over the world and forces all non supes into forced labor camps.")
    print("Maybe you should have killed the most powerful individual instead.")
    print("The End. Make sure to play again and try all the endings")


def kill_homelander():      # Kill Homelander with the virus
    print("You decide to kill the most powerful of the two and kill Homelander.")
    print("His skin bubbles as it starts to fall off, and after a minute, he is dead.")
    print("However you still have the terrorist to deal with, Do you: ")
    print("1. Continue the mission")
    print("2. Fall back to regroup due to the mission being compromised")

    choice9 = input("")

    if choice9 == "1":              # Continue the mission
        continue_mission()
    elif choice9 == "2":            # Fall back due to the mission being compromised
        fall_back()
    else:
        print("Invalid choice. Try again. :( ")
        kill_homelander()



def continue_mission():             # Continue the mission
    print("Since the soldiers where already dead and only the terrorist remains, you continue the mission.")
    print("You now need to figure out a way to kill him.")
    print("You know he is also a superhero and cant be killed by your rifles.")
    print("The terrorist is very angry and starts to running at your team.")
    print("You quickly think of two options, Do you: ")
    print("1. Set a large trap with dozens of grenades to hopefully kill him")
    print("2. Blow up the entrances trapping the terrorist in")

    choice10 = input("")

    if choice10 == "1":             # Set a grenade trap
        grenade_trap()
    elif choice10 == "2":           # Trap the terrorist inside
        trap_inside()
    else:
        print("Invalid choice. Try again. :( ")
        continue_mission()
        

def fall_back():                # Fall back due to the mission being compromised
    print("You tell your team that the mission has gone compleatly inside out and that you all need to fall back.")
    print("You retreat back to the humvees and go back to base.")
    print("You see on the TV that the terrorist base and men had been compleatly destroyed but there had been no sign of the terrorist.")
    print("The general was happy with the impact of the mission.")
    print("He theorized that the terrorist had lost everything and wouldn't have the guts to rebuild his work again just for us to take it down.")
    print("You know that the mission was successful, but you also know the terrorist was still out there in hiding, for now...")
    print("The End. Make sure to play again and try all the endings")



def grenade_trap():         # Set a grenade trap
    print("You radio back to your teammates at the enterence of the vent to set up a ton of grenades to blow him up.")
    print("You crawl out of the vent and can hear him approaching you rapidly.")
    print("You and your team take cover around the corner, and the terrorist activates the trap.")
    print("The terrorist stands there confused for a couple of seconds, then get hit by about 20 grenades.")
    print("The terrorist may have been able to withstand rifle bullets, but 20 grenades was to much and he was blown to bits.")
    print("You and your team high five eachother, knowing that, even though the it went a little off path, the mission was successful.")
    print("You radio back to base that the mission was a success, and fall back to base.")
    print("You and your team are labeled as heros for taking down two dangerous individuals.")
    print("The End. Make sure to play again and try all the endings")



def trap_inside():          # Trap the terrorist inside
    print("You dont think that you can kill him with pure firepower and brute force, so you decide to trap him inside his own basement prison for eternity.")
    print("You have your team quickly put explosives next to all the exits.")
    print("The second you exit the vent you blow up all the exits.")
    print("You hear him screaming on the other side of the wall trying to get out.")
    print("In the next hour you and your team call in a cement truck and proceed to pour it into the basement.")
    print("His screams get quieter and quieter until they are completely gone.")
    print("The terrorist is now trapped in an eternal paralisis due to the cement.")
    print("Where he can do nothing more to terrorize anyone else while hes still trapped, for now...")
    print("The End. Make sure to play again and try all the endings")


entering_somolia()              # Beginning of the story