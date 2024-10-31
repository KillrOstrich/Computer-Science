#horror type game where you are in a haunted school filled with monsters/terror
print("you find yourself in the entrance of an abandoned school with the task of retreieving a token. The school only has the front door entrance as a in and out. It's really an easy job except something sinister lies in these walls")



def start_adventure () : #start of adventure 
    print("1. enter the entrance using the front doors") #option 1 
    print("2. turn back because there is no way youre going in there") #option 2 

    choice = input(":")

    if choice == "1" :
        enter_door()
        encounter_1()

    elif choice == "2" :
        turn_back()
        start_adventure()

    else:
        print ("invalid choice, retry")
        start_adventure()


def enter_door (): # encounter 1 
    print("you enter the doors, behind you the doors shut. there is no turning back now")

def turn_back(): #encounter 2 
    print("youre lowkey smart but also being boring. your adventure is over ") 





#choice from enter_door 
def encounter_1 ():
    print("you now look around and see 2 pathways, one on your left, one on your right. its too dark to see into the middle")
    print("1. take the left")
    print("2. take the right")

    choice = input(":")

    if choice=="1": #option 1 
        take_left()
        encounter_2v1()
        
    
    elif choice=="2": #option 2 
        take_right()
        encounter_2v2()
    else:
        print("invalid choice try again")
        encounter_1()

def take_left (): #encounter 3
    print("you slowly walk down into the left hall, as you walk you feel a presence of someone watching you from behind. suddenly, you get a pinch in the ribs")  #flow to encounter 2v1
    
def take_right (): #encounter 4
    print("you slowly walk down into the right hall, the lights flicker on and you see a shrine with swords and candles around it") #flow to encounter 2v2
    



#choice from take left 
def encounter_2v1():
    print("you feel your side and it has drops of blood coming from it. what is in this school? you keep going and see a piece of paper on the ground. Do you pick it up?  ")
    print("1. pick it up")
    print("2. don't pick it up and continue down hall")

    choice=input(":")

    if choice=="1": #option 1 
        pickup_paper()
    elif choice=="2": #option 2 
        dont_pickup()
        encounter_3v1()
    else:
        print("invalid choice try again")
        encounter_2v1()

def pickup_paper (): #encounter 5 
    print("the paper has a paper saying you will die.") #ending 0
    print("monster dressed in full black that has viscosity, a monster with a large white smile with no eyes. a 8ft beast has taken you. crushed you into little pieces. rip")

def dont_pickup (): #encounter 6
    print("you continute down the hallway until its a dead end. the classroom on the left is locked. the only way is right and thats where you go all the way down") #flow to encounter 3v1




#choice from take right 
def encounter_2v2 ():
    print("the shrine is worshipping these black creatures. must be normal. theres some water and snacks on it as offerings. might as well right")
    print("1. take the snacks and continue your task")
    print("2. continue on down the hallway")

    choice=input(":")

    if choice=="1": #option 1 
        take_snacks()
        encounter_3v2()
    elif choice =="2": #option 2 
        continue_down()
        encounter_3v3()
    else:
        print("invalid choice try again")
        encounter_2v2()

def take_snacks(): #encounter 7
    print("aw you got snacks, you continue strolling down the hallway") #flow to encounter_3v2

def continue_down(): #encounter 8 
    print("you hear loud banging closer and closer. theyre right behind you. closer closer now its behind you") #flow to encounter 3v3





#choice from dont_pickup
def encounter_3v1 ():
    print("you see a light orb at the end of the hallway and decide to go down. theres a basement. do you go down?")
    print("1. go down")
    print("2. turn around")

    choice=input(":")

    if choice =="1": #option 1 
        go_down()
        encounter_4v1()
    elif choice=="2": #option 2 
        turn_around()

    else:
        print("invalid choice try again")
        encounter_3v1()

def go_down(): #encounter 9
    print("as you strolly step down the basement, the floor boards creek at every step going down. theres glass that you heard just break from above. you slowly go down and feel a sharp pain when you finally reach the end of the stairs") #flow to encounter_4v1

def turn_around(): #encounter 10
    print("you turn around and stroll anout 2 feet. that is when suddenly you see a giant man with a giant eye the size of a chair. his eye slowly looks into your soul. you feel your body levitating and eventually. you are ripped in 2...") #ending 1 





#choice from take_snacks 
def encounter_3v2 ():
    print("you start going down the hall as always snacking on the newly snacks you found. itll fill you up to find this token. you find the elevator to this old school theres a body in it. what is this place. you hear a bang and the elevator light turns on. run")
    print("1. run")
    print("2. RUN")

    choice=input(":")

    if choice=="1": #option 1 
        go_run()
        encounter_4v2()
    elif choice=="2": #option 2 
        go_run()
        encounter_4v2()
    else:
        print("invalid choice try again")
        encounter_3v2()


def go_run(): #encounter 11
    print("there is no way a elevator can turn on by itself. you didn't even press it. RUN. you run out of there and find a dead end. sounds of loud banging is following you as you run. you have to hide.") #flow to encounter 4v2





#choice from continue_down
def encounter_3v3():
    print("1. RUN")
    print("2. stand still")

    choice=input(":")

    if choice=="1": #option 1 
        run_continue()

    elif choice=="2": #option 2 
        stand_still()

    else:
        print("invalid choice try again")
        encounter_3v3()

  
def run_continue(): #encounter 12 
    print("you run away, you run and run and continue to keep running. you maneuver on the directions you first had. you reach the door you first came in. you are free but tramuatized with no token.") #ending 2


def stand_still(): #encounter 13
    print("you stand still. a creature with black ink like substance and a light on his head picks you up and leads you to a room. you are a wreck and you're thrown into the room. He blocks the door and locks it. you're trapped with no outlet to escape...") #ending 3





#choice from go_down
def encounter_4v1():
    print("you step on a nail when you finally step down. hurts like hell. you gotta take it out though.")
    print("1. take out of foot")
    print("2. do not take out. ")

    choice=input(":")

    if choice=="1": #option 1 
        take_out()
        encounter_5v1()
    elif choice=="2": #option 2 
        not_takeout
        encounter_5v2()
    else:
        print("invalid choice try again")
        encounter_4v1()
    
def take_out(): #encounter 14
    print("you take out in excrutiating pain. the basement door shuts on you. you take your sock to make a tourniqet out of your sock. you have to keep going") #flow to encounter 5v1

def not_takeout(): #encounter 15 
    print("you decide not to take out the nail. your steps are cruically slow and labored. the token still must be found. ") #flow to encounter 5v2




#choice from go_run
def encounter_4v2():
    print("you see a classroom with a door open and a locker you could hide in. which one are you choosing")
    print("1. Classroom")
    print("2. Locker")

    choice=input(":")

    if choice=="1": #option 1 
        hide_classroom()
        encounter_5v3()
    elif choice=="2": #option 2 
        hide_locker()
        encounter_5v4()
    else:
        print("invalid choice try again")
        encounter_4v2()

def hide_classroom(): #encounter 16 
    print("you hide in the classroom and hide under a teacher desk. you hear loud banging continuing to get closer, something bangs on the door bang bang bang. it leaves. youre safe") #flow to encounter 5v3

def  hide_locker(): #encounter 17
    print("you hide in the locker and shut it. something gets closer and closer with banging following it. its right next to you breathing in your space. the pearly white eyes this creature has is the only thing you can see between the holes in the locker. it looks at you dead in your eyes. it leaves. you're safe") #flow to encounter 5v4



#Choice from take_out 
def encounter_5v1():
    print("as you continue throught the basement you see many artifacts that have no place being in this school. you keep going through this dark hallway limping through. at the end, you see an old painting depicting the token. the token is seen on an altar with the painting. you did it you found it. lets get out of here")
    print("1. Leave")
    print("2. scope around 1 last time")

    choice=input(":")

    if choice=="1": #option 1 
        leave_basement()
        encounter_6v1()
    elif choice=="2": #option 2 
        scope_around()
        encounter_6v2()
    else:
        print("invalid choice try again")
        encounter_5v1()


def leave_basement(): #encounter 18 
    print("you leave the basement with the token at your grasp. you are retracing your steps to get out of this school") #flow to enouncter 6v1
def scope_around(): #encounter 19 
    print("you scope around and find a crowbar. this could be useful. you leave the basement with a crowbar and the token. you retrace your steps to get out of this school.") #flow to encounter 6v2





#choice from not_takeout
def encounter_5v2():
    print("as you laborly limp around the basement, there are sounds of footsteps above you but a glitter of sparkle. its the token. you get closer to the token and take it. the footsteps stop right above you")
    print("1. run out of there")
    print("2. wait it out in basement")
    
    choice=input(":")

    if choice=="1": #option 1 
        runup_basement()
    elif choice=="2": #option 2 
        waitit_out()
    else:
        print("invalid choice try again")
        encounter_5v2()

def runup_basement(): #encounter 20
    print("you run out of the basement as you slowly make it out of the door frame. a figure or man knocks you out. he takes the token and puts it in his pocket. he drags you to the front doors. you wake up and he waves at you while backing up into the darkness. he spared you. ") #ending 4
def waitit_out (): #encounter 21 
    print("you wait as the footsteps move away from above. coast is clear and you run to the door. you retrace your steps and see the front door. you check your pocket for the token and smile. you hear sirens and walk out the door. the cops are waiting for you stacked and telling you to get down. you're arrested for tresspass and theft.") #ending 5






#choice from hide_classroom
def encounter_5v3():
    print("1.?")
    print("2.???")
    choice=input(":")

    if choice=="1": #option 1 
        fall_classroom()
    elif choice=="2": #option 2 
        fall_classroom()
    else:
        print("invalid choice try again")
        encounter_5v3()

def fall_classroom (): #encounter 22
    print("you see that the coast is clear. theres no way youre finishing this. you run down the hallway and see a door as fast as you can you go for the door you open it and jump. youre falling. falling 50 ft. why is there a 50ft drop. goodbye") #ending 6



#choice from hide_locker
def encounter_5v4():
    print("1.?")
    print("2.?????")

    choice=input(":")

    if choice=="1": #option 1 
        lock_locker()
    elif choice=="2": #option 2 
        lock_locker()
    else:
        print("invalid choice try again")
        encounter_5v4

def lock_locker (): #encounter 23 
    print("as you try to calm yourself. you realize the locker has locked onto itself. you are stuck in the locker in an abandoned school. forever") #ending 7

        

#choice from leave_basement
def encounter_6v1():
    print("you make it to the front door where you orignally stepped into this place. the door is locked youre doing everything you can to open it. banging on the door ramming into it. someone hears you. you hear running. its coming closer and closer. closer and closer. dum dum dum dum you gotta open it now. pick the right choice")
    print("1.")
    print("2.")

    choice=input(":")

    if choice=="1": #option 1 
        escape_end()

    elif choice=="2": #option 2 
        escape_endnotoken()
    
    else:
        print("invalid choice try again")
        encounter_6v1()

def escape_end(): #encounter 24 
    print("the door opens. you escape with the token and run away quick into the darkness. you will come back") #ending 8

def escape_endnotoken(): #encounter 25 
    print("the man is running quicker and quicker. the token falls out of your pocket. the door opens. you run as quick as you can as you mightve just died. was it worth it?") #ending 9






#choice from scope_around
def encounter_6v2():
    print("you make it to the front door where you orignally stepped into this place. you try opening the door and it doesn't work. you take your crowbar and smash through the door. you run out as quickly as you can. you did it. you have the token and run away into the darkness. ") #ending 10









start_adventure()