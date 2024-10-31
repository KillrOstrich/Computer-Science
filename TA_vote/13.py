Man_Bond = 0   # The bond you will have with a character in the game which will influence how the game ends 

def Start_Adventure():  # Back round information to give context behind the story
    print("Your name is Bob and you have randomly come across a very suspicious looking facility with a dark mist around it")
    print("1. Turn back around being too scared to enter the scary place")
    print("2. Enter through the door which is mysteriously covered in a thick fog, so you can't see inside")

    choice_1 = input("> ")  # First choice in the story 

    if choice_1 == "1":
        Go_Home()

    elif choice_1 == "2":
        Enter_Building()
            
    else:
        Start_Adventure()

def Go_Home():
    print("You're a scaredy cat and decide not to have a totatlly fun adventure")
    print("You walk through the forest the facility still on your mind and are suddenly attacked by a shadowy figure")
    print("Your screams echo between the trees and you are never seen again")
    print("Game Over")  # First ending in the game

def Enter_Building():
    print("You enter through the door which loudly creaks and are greated with a dimly lighted front office")
    print("The doors magically slam shut behind you and won't open again")
    print("The lights shutter and in the corner of your eye you see two doors, one with danger written on it in red and the other saying safe")
    print("1. Enter though the door that says Danger on it nervous to see what you will find inside")
    print("2. Enter though the door that says Safe on it feeling confident in your choice")

    choice_2 = input("> ")  # Second choice in the story, also very important cuase it leads you to two different encounters

    if choice_2 == "1":
        Inside_Creepy_Door()

    elif choice_2 == "2":
        Inside_Safe_Door()

    else:
        Enter_Building()

def Inside_Creepy_Door():
    print("Inside the door way you see a very bright blinding light")
    print("1. walk slowly toward the light")
    print("2. run very fast at the light")
    
    choice_3 = input("> ")  # Third choice in the story 
    
    if choice_3 == "1":
        Talk_With_Man()

    elif choice_3 == "2":
        print("The person behind the blinding light shoots you out of fear")
        print("You can feel the pellets go through your body and your vision turns to black")
        print("Game Over")  # Second ending to the game

    else:
        Inside_Creepy_Door()


def Talk_With_Man():
    global Man_Bond 
    print("You see a man holding a flashlight at your face and he is also holding a shotgun")
    print("Still standing there he says, Omg I thought you were a monster, almost shot you there")
    print("What looks like to be an old man greets you and says, My name is Joe")
    print("1. Greet him back saying your name is Bob")
    print("2. Don't say anything to the stranger and look at him with an uneasy feeling in your eye")

    choice_4 = input("> ")  # Fourth choice in the story 

    if choice_4 == "1":
        Man_Bond = Man_Bond + 1   # Building bond with Man 
        Monster_Encounter()

    elif choice_4 == "2":
        Monster_Encounter()
    
    else:
        Talk_With_Man()

def Monster_Encounter():
    global Man_Bond 
    print("You have no more time to talk becuase a monster bursts through the door you just came through a moment ago")
    print("The old man tells you to run but not sure of what is the best option are frozen in place")
    print("1. You see a metal pipe on the gound and think to wack the monster with it")
    print("2. You follow the old mans direction to run")

    choice_5 = input("> ")  # Fifth choice in the story

    if choice_5 == "1":  
        Through_The_Door()

    elif choice_5 == "2":
        Man_Bond = Man_Bond + 1 # Maximized bond with Joe, he now would fully trust you
        Through_The_Door()

    else:
        Monster_Encounter()

def Through_The_Door():
    print("After either running or hitting the monster you go to the end of the hallway becuase")
    print("more monsters are crashing through the door")
    print("1. Go through the door at the end of the hallway")
    print("2. Hide in a side room")

    choice_6 = input("> ")  # Sixth Choice in story 

    if choice_6 == "1":
        Hallway_Door()

    elif choice_6 == "2":
        Side_Room()

    else:
        Through_The_Door
    
def Hallway_Door():
    print("You and Joe both go through the door at the end of the hallway")
    print("1. Lock the door with the built in lock on the door")
    print("2. Put a metal pipe through the door handle to secure it")

    choice_7 = input("> ")  # Choice seven 

    if choice_7 == "1":
        print("The monsters are able to get through the door becuase it is not secure enough")
        print("You and the man are attacked by the beasts and are never heard from again")
        print("Game Over")  # Third ending in the game

    elif choice_7 == "2":
        Exit_Sign()
    
    else:
        Hallway_Door()

def Exit_Sign():
    print("You are sure the door will hold the monsters back and now you want to find an exit to this place")
    print("There is a divided path that go in two different directions, you guys decide to split up to find an exit")
    print("1. You go left and Joe goes to the right")
    print("2. You both decide to go to the right thinking you guys are safer together")

    choice_8 = input("> ")  # Eigth choice

    if choice_8 == "1":
        Left_Pathway()

    elif choice_8 == "2":
        Right_Pathway()
    
    else:
        Exit_Sign

def Left_Pathway():
    print("As you walk through the dark corridor you hear a creepy sound a bit further down")
    print("1. Continue down the hallway")
    print("2. Walk back to the divided path and go right to meet up with Joe")

    choice_9 = input("> ")  # Ninth Choice

    if choice_9 == "1":
        Fake_Exit()

    elif choice_9 == "2":
        Right_Pathway()
    
    else:
        Left_Pathway()

def Fake_Exit():
    print("As you contiue to walk down the hallway the noise grows louder but with curoisty you continue")
    print("You see a door with an Exit sign above it at the end but you still hear the weird sound")
    print("You are sure that the noise is coming from behind the door, but it says exit on it, so its safe right")
    print("1. Go through the door anyways even though you are skeptical of it")
    print("2. Turn back and go with Joe on the other path not trusting this door")

    choice_10 = input("> ") # Tenth choice in the story

    if choice_10 == "1":
        print("Turns out there was a monster lurking behind the door trying to catch people who are unsuspecting")
        print("You are caught off guard and before you can even think the monster grabs you and drags you into the room behind the fake exit sign door")
        print("Game Over")  # Fourth Ending

    elif choice_10 == "2":
        Right_Pathway()

    else:
        Fake_Exit()

def Right_Pathway():
    print("As you both walk together down the right pathway you come across a door with an exit sign above it but chains are all over the door that need to be cut to open it")
    print("Joe tells you to watch his back while he cuts the chains")
    print("1. Watch Joes back")
    print("2. Help him cut the chain on the door")

    choice_11 = input("> ") # Eleventh Choice in the game

    if choice_11 == "1":
        Real_Exit()

    elif choice_11 == "2":
        print("As you both start to cut the chains a sneaky monster comes up behind you both knowing that neither of you know of his pressense")
        print("The monster grabs you both and you guys are never able to escape the facility")
        print("Game Over")

    else:
        Right_Pathway()

def Real_Exit():
    global Man_Bond 
    print("As Joe is able to get the last chain off the door he goes through the door")

    if Man_Bond == 2:  # Only happens if you have built a bond with Joe throughout the game
        print("Joe tells you that he has opened the door and you go out the door with him")
        print("You both escape the facility and live long fulfilling lives")
        print("Game over")  # Fifth Ending 

    elif Man_Bond < 2: # Haven't built enough bond with Joe
        print("Joe doesn't tell you that he has opened the door becuase he doesn't like you enough")
        print("He locks the door behind him and leaves you in the facility all alone")
        print("You are trapped in the facility forever and are never heard from again")
        print("Game Over")  #Sixth Ending 

def Side_Room():
    print("You see the monsters run past the door through the window")
    print("You hear the screams of the old man in the distance and think that the worst has happened to him")
    print("1. Explore more of the room you are hiding in")
    print("2. Exit the room out into the hallway thinking that it is safe")

    choice_12 = input("> ") # twelfth choice in the game

    if choice_12 == "1":
        Explore_Room()

    elif choice_12 == "2":
        Hallway()

    else:
        Side_Room()

def Explore_Room():
    print("As you walk through the dark room you hear the door open that you went though to get inside the room")
    print("A monstery figure enters the room and sniffs around trying to find you")
    print("1. Hide in a cuboard")
    print("2. Confront the monster head on")

    choice_13 = input("> ") # Thirtenth choice in the game 

    if choice_13 == "1":
        print("The cuboard was a really good hiding spot becuase the monster is never able to find you and eventually leaves")
        print("You leave the room now and eventually find Joe alive and well")
        print("It is short lived however because a monster comes after you both and you guys are forced to go through a door to escape him")
    
        Exit_Sign()

    elif choice_13 == "2":
        print("The monster lunges at you without giving you any time to try and fight back")
        print("The monster has found its prey and you are dragged deeper into the facility never heard from again")
        print("Game Over")  # Seventh Ending 

    else:
        Explore_Room()

def Hallway():
    print("Outside there is a monster standing at the end of the hallway")
    print("He is weirdly familiar to you and than you suddenly realize that it is Joe but he is now turned into a monster")
    print("1. Try and get past him to get to the door behind him")
    print("2. Turn around and go back to the front office to go inside the door that says safe on it")

    choice_14 = input("> ") # Fourteenth choice 

    if choice_14 == "1":
        print("As you try and get around him he grabs you and spits this substance on you")
        print("The substance burns your skin and suddenly you black out")
        print("When you awake you are turned into a horrific monster just like Joe and are trapped forever")
        print("Game Over")  # Eighth Ending


    elif choice_14 =="2":
        print("As you enter the office again you have a feeling that the safe door woudld've been a much better")
        print("choice than the door that you just went through")
        
        Inside_Safe_Door()

    else:
        Hallway()

Monster_Bond = 0    # Bond with the monster which will affect the ending you will get

def Inside_Safe_Door():
    global Monster_Bond
    print("As you creek open the door you see a monster at the end of a long hallway")
    print("1. You decide to approuch the monster unthreateningly with your hands up")
    print("2. Feeling scared you pick up a crowbar and start running and screaming toward the monster")

    choice_15 = input("> ") # Fifteenth Choice 

    if choice_15 == "1":
        Monster_Bond = Monster_Bond + 1 # You have built some trust with the monster
        print("Just by looking at the monster you could tell he wasn't like other ones")
        print("You could feel he meant no harm to you")
        
        Monster_Talk()

    elif choice_15 == "2":
        print("The monster scared takes a swing at you but you dodge it")
        print("You hit him back saying, die monster")
        print("The monster just lays there and does nothing so you decide to stop, he gets up")
        
        Monster_Talk()

    else:
        Inside_Safe_Door()

def Monster_Talk():
    print("You start to talk with him and learn that his name is George")
    print("George tells you that a terrible virus has came through this facility turning most people inside into mindless monsters")
    print("1. Ask him who made the virus")
    print("2. Ask him why he isn't mindless")

    choice_16 = input("> ") # Sixteenth choice in the story

    if choice_16 == "1":
        print("George tells you that an evil doctor named Ross maliciously took an exoerimental starnd of a virus and set it lose on the facility")
        
        Solution()
    
    elif choice_16 == "2":
        print("George tells you that when the outbreak first started he had a gas mask on becuase of an experiment he was conducting, the mask protected most")
        print("of his brain function but it still mutated his body")
        
        Solution()
        
    else:
        Monster_Talk()
    
def Solution():
    print("George explains however that there is an experimental gas that he was working on that should cure people's brains of the virus and bring them back to normal")
    print("He says that it is in his office but Doctor Ross, the leader of the mutants, is also trying to look for it")
    print("1. Say that we should straight to George's office to get the cure")
    print("2. Tell him that we should look for Ross so we can cut off his conection to the other monsters so he can't control them anymore")

    choice_17 = input("> ") # Seventeenth Choice in the story 

    if choice_17 == "1":
        George_Office()

    elif choice_17 == "2":
        Search_For_Ross()

    else:
        Solution()

def George_Office():
    print("When you get there George says the the cure is locked in a room but that only one of us can enter at a time")
    print("1. You offer to go inside the room")
    print("2. You tell him to go inside and retrieve the cure")

    choice_18 = input("> ") # Eighteenth Choice in the story 

    if choice_18 == "1":
        print("You go inside the room and the door behind you locks you inside")
        print("You get the canister and put it in a machine that spreads the gas across the building")
        print("The gas cures everybody including George but you are stuck inside the room forever and slowly die")
        print("Game Over")  # Ninth Ending 


    elif choice_18 == "2":
        print("George goes inside and gets the gas canister")
        print("He goes over to a machine and puts the canister inside, the gas is than released out into the facility")
        print("All the monsters are cured now and back to normal but since George is still in the room he is not cured")
        print("Game Over")  # Tenth Ending

    else:
        George_Office()

Evil_Intentions = 0 # Your willingness to do evil things 

def Search_For_Ross(): 
    print("George tells you that he is most likely in his office looking over the cameras in the facility")
    print("You guys go there and find him sitting in his chair turned around")
    print("You and George jump Ross and knock him out")
    print("1. Take a key on Ross's neck that is important")
    print("2. Leave the key on his neck for George to take")

    choice_19 = input("> ") # Ninteenth Choice

    if choice_19 == "1":        
        if Monster_Bond == 1:   # Bond with george will affect how he will react when you take the key
            global Evil_Intentions
            Evil_Intentions = Evil_Intentions + 1
            print("You find a machine key around Ross's neck and take it")

            Ross_Fate()

        elif Monster_Bond == 0: 
            print("George notice that you took the key and takes it back not trusting you with it")

            Ross_Fate()


    elif choice_19 == "2":
        print("George takes a machine key that was wrapped aroud Ross's neck and puts it in his pocket")

        Ross_Fate()

    else:
        Search_For_Ross()

def Ross_Fate():
    global Evil_Intentions
    print("1. You guys decide to leave Ross there for police to find after everybody is cured")
    print("2. You decide that Ross should be punished for what he has done to everybody")

    choice_20 = input("> ") # Tweenteith Choice 

    if choice_20 == "1":
        print("You leave him in the office and head toward Georges office")
        Final_Scene()

    elif choice_20 == "2":
        Evil_Intentions = Evil_Intentions + 1
        print("You sufficate Ross and leave his body in the office and head toward Georges office")

        Final_Scene()

def Final_Scene():
    if Evil_Intentions == 2:
        print("Once you get your hand on the canister you take the key you found on Ross and insert it in the canister")
        print("This mutates the gas and makes it so the monsters will all obey you")
        print("You release the gas on the building and become the new leader of the monsters and take over the world")
        print("Game Over") # Eleventh ending

    elif Evil_Intentions < 2:
        print("You and goerge get the canister and spread the gas all over the facility")
        print("Everyone is cured of the sickness including George and every lives happy lives")
        print("Game Over")  # Tweelth Ending 

    
Start_Adventure()