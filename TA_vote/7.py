def start_adventure(): #start function
    print("Welcome to the start of your exploration chose a route to travel. Do you:")
    print("1.  north") # 3 player choices
    print("2.  east")
    print("4.  west")

    choice = input("> ")

    if choice == "1":
        travel_north()
    elif choice == "2":
        travel_east()
    
    elif choice == "4":
        travel_west()
    else:
        print("Wrong choice. Try again.")
        start_adventure()

def travel_north(): # what happens when you chose one of the 3 options
    print("You start walking north but realize it's to cold")

def travel_east():
    print("You start riding your horse east until you find something disturbing on the way")

def travel_west():
    print("You start traveling west but end up in the middle of a dessert")

def north(): # start another function for route north
    print("You walk back to your home and grab a coat to bring with you so the cold does not affect you")

def east(): # start function for east and list options you have
    print("You find a dead person in the middle of the path and you can't continue this way. do you:")
    print("1. turn back and find a different route east")
    print("2. continue on the same route but go off course into the strange woods next to the route.")

    choice = input("> ")

    if choice == "1":
        find_new_route()
    elif choice == "2":
        enter_woods()
    else:
        print("You can't do that try again")
        east()

def find_new_route(): # what happens when you chose an option from route east
    print("You go back to where you started but found a different path amd decide to follow it. Jokes on you you've been fooled there is not another route east,you decide to follow this random path and get lost and eventually you have no more food and you strave to death you end here.")    #1st ending

def enter_woods():
    print("you decided to alter your path and now are forced to travel through the strange woods you know nothing about. Now you stand at the entrace of the strange woods.")

def west():
    print("You ended up in the middle of a dessert and are trapped with no water but you see a small spring and decide to go towards it.")

def going_north(): #chose your option for route north
    print("You started traveling north again with your coat but you get caught in a blizzard. you see a house near by but you don't know the people. do you:")
    print("1. Go the strangers house and see if you can stay there")
    print("2. keep walking and hope you make it out of the blizzard.")

    choice = input("> ")

    if choice == "1":
        strangers_house()
    elif choice == "2":
        keep_walking()
    else:
        print("can't do that try again")
        going_north()

def strangers_house(): #options for north
    print("The strangers allow you stay with them until the blizard passes. you enter the home but instantly fell something is off.")

def keep_walking():
    print("you decide to keep walking and hope the blizzard passes. the blizzard casues issues seeing and you don't know where your going and get off track. You end up in the middle of no where and become trapped forever in the blizzard. your done forever")# ending
    
def dessert(): # options in west route 
    print("your in need of water and head towards a spring in the dessert. When you get to the spring you notice the water looks weird. Do you:")
    print("1. take the chance and drink the water")
    print("2. don't drink the water and hope to make it out without water")

    choice = input("> ")

    if choice == "1":       # chose an option
        drink_water()
    elif choice == "2":
        do_not_drink()
    else:
        print("you can't do that, try again")
        dessert()

def drink_water():
    print("You took the risk and drink the spring water. luckily it just looked werid and was safe")

def do_not_drink():
    print("you did not drink the water and could not make it out of the dessert. if you chose this option your adventure ends here.") # 2nd ending

def dessert_west(): #chose an option for this route
    print("you ran our of water. Do you.")
    print("1. try to find another spring for water")
    print("2. Trt to get out of the dessert without water")

    choice = input("> ")

    if choice == "1":
        find_dif_spring()
    elif choice == "2":
        leave_dessert()
    else:
        print("You can't do that try again!")
        dessert_west()

def find_dif_spring(): # what happens for each option
    print("You failed. You could not find another spring for water in the dessert and you become dehydrated which ends your story") # ending

def leave_dessert():
    print("You were about to make it out of the dessert with no water but something terrible happend. you encountered dessert demons and could not fight them off because you were so weak. the dessert demons make it impossible to obtain any water. you can't make it out and get trapped in the sand dunes with the rest of the dessert demons.") # ending

def strange_woods(): # chose what you want to do in the woods
    print(" you are standing at the entrace of the strange woods and are scared to enter. Do you")
    print("1. enter the woods and hope nothing bad happens ")
    print("2. you chicken out and go back home")

    choice = input("> ")

    if choice == "1":
        mysterious_woods()
    elif choice == "2":
        go_home()
    else:
        print("you can't do that try again!")

def mysterious_woods(): # what happens when you do something in the woods.
    print("You decide to enter the woods but right as you enter you start hearing something that is off")

def go_home():
    print("you chickened out and the people of your home town are angry and decide to banish you forever. Game over") # 3rd ending


def weird_house_north(): # chose any of the options
    print("your in the starngers house but notice something is off. Do you")
    print("1. ingnore the feeling and still stay there")
    print("2. start looking aroud the house and see if you can notice something wrong")
    print("3. You think the people that let you stay are kind and simply ask them if there hiding anything")

    choice = input("> ")

    if choice == "1":
        stay_home()
    elif choice == "2":
        snoop_around()
    elif choice == "3":
        ask_owners()
    else:
        print("WRONG. can't chose that try again")
        weird_house_north()

def stay_home(): # what happens when you chose one of the above options
    print("You ingonored the feeling and found the house pretty comfy")

def snoop_around():
    print("you think you your looking around secretly but the owners found you doing this and hated it so you got kicked out. You didn't survive outside for long until hypothermia started and you died. Adventure over ")     # another ending

def ask_owners():
    print("The owners were infact hiding something, the entire time this was a trap. The owners can't reveal what they are hiding but you could not leave so they trapped you in there dungeon forever. This means your story is over.") # ending
        

def woods_route(): # chose an option for this encounter
    print("Something is off in the woods but you don't know what. Do you")
    print("1. act like nothing is wrong and keep on going through the woods")
    print("2. Leave the woods becasue your scared something is going to happen")
    print("3. You try to see what is wrong in the spooky woods")

    choice = input("> ")

    if choice == "1":
        keep_on_going()
    elif choice == "2":
        leave_woods()
    elif choice == "3":
        snoop_woods()
    else:
        print("INCORRECT, you can't do that try agian")
        
        woods_route()

def keep_on_going(): # what happens when you chose an option for this encounter
    print("You decide to keep on moving through the woods and your almost to other side of the woods but before you exit there is something big blocking the exit")

def leave_woods():
    print("you tried to leave the woods but there is a special curse in the woods that doesn't allow you to leave unless you explore the entire woods. The curse traps you here forever. this is your ending") # Another ending

def snoop_woods():
    print("You start snooping around the woods to see what is wrong but this is a grave mistake. while snooping around you encouter a giant angry bear. The bear dislikes the fact that you are snooping around so he grabs you with his teeth and rips you to shreds. Your adventure comes to a close.") #ending

def north_home(): # chose an option for this encounter
    print("The blizzard has passed and the owners are going to make you leave soon but you barely have any materials left. do you")
    print("1. Try to talk to the owners and convince them to let you stay longer untl you figure something out")
    print("2. Leave the house and try to find more materials before you run out")

    choice = input("> ")

    if choice == "1":
        convince_owners()
    elif choice == "2":
        leave_house()
    else:
        print("wrong choice try again")

        north_home()

def convince_owners(): # what happens for each option
    print("You beg the owners to let you stay and they say no and kick you out. shortly after this you run out of materials on your route and can't move on anymore. The cold weather gets to you and you freeze forever. you story commes to a cold ending") # ending

def leave_house():
    print("you left the house but luckily on your route north you found a shop to restock on materials so you can continue your journey")
    
def big_animal(): # chose an option for this encounter
    print("the thing blocking the exit of the forest is a huge bear. Do you")
    print("1. You noticed a sword nearby and decide to grab it and hopefully defeat the bear ")
    print("2. Decide to test your speed and try to run around him to exit")
    print("3. Simply go around the bear because you think he is nice and not mean")

    choice = input("> ")

    if choice == "1":
        grab_sword()
    elif choice == "2":
        out_run_bear()
    elif choice == "3":
        go_around_bear()
    else:
        print("you can't do that. Try again!")

        big_animal()

def grab_sword():       # what happens when you chose an option from the encounter
    print("you grabbed a sword you noticed near by and started attacking the bear. This was a mistake you miss your swing with the sword and the bear steps on you with your paws. when he stepped on you it pushed you into the ground and you were stuck forever. adventure ends here") #ending

def out_run_bear():
    print("you thought you were fast enough but this was not the case. The bear caught up with you and threw you into another universe. Story over")    #ending

def go_around_bear():
    print("You go around the bear and he lets you pass. The bear likes that you didn't try any tricks to get past and allows you to exit the woods and continue your route east ") 

def traveling_north(): # chose an option you want to do for the encoutner
    print("You were able to restock on your materials for your route north. Your almost finished with your route north but now you have to cross a dangerous mountain to finish. Do you")
    print("1. try to climb the mountain and cross it even if it's extremly dangerous")
    print("2. Travel around the mountain on a random route you know nothing about")

    choice = input("> ")

    if choice == "1":
        climb_mountain()
    elif choice == "2":
        go_around_mountain()
    else:
        print("you can't do that. Try again!!")

        traveling_north()

def climb_mountain():   # what happens for each option 
    print("Even though it was dangerous to climb the mountain you made it safely over and find the final destination north")

def go_around_mountain():
    print("You though it would be safer to go around the mountain but you were wrong. You took a random route and it was a dead end you were stranded forever. Unforunately your done forever") #ending

def exit_woods(): # chose what you want to do for the encounter
    print("The bear let you past and you exited the woods. You see your final destination. Do you")
    print("1. Go to the final spot")
    print("2. Stay where you are because you don't want to finish your journey yet.")

    choice = input("> ")

    if choice == "1":
        final_destination()
    elif choice == "2":
        stay_put()
    else:
        print("you can't do that try again")

        exit_woods()

def final_destination(): # what happens from your choice
    print("congratulations you have finished your journey east. Your story comes to a happy ending here")       #ending

def stay_put():
    print("You wanted to keep going and not end your journey. unfortunately you made a bad mistake by staying put because the final detination spot pulls anyone in there that is close. But by pulling you into the final destination the forces used tear you apart. Your journey comes to a gruesome end")   #ending

def final_north():
    print("Congrats on passing the mountain and every other challenge you have made it to the final destination. unfortunately this means your time comes to an end. Adveneture over")

print("thanks for playing please try again")        #final, thanks for playing.