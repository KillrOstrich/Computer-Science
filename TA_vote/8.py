def start_adventure():                                                                                   # starting function
    print("You and your immeadiate family want to see other relatives, where do you want to go?")        # asking user where they want to go
    print("1. Washington, on the west coast")                                                            # option to go to Washington
    print("2. Maine, on the east coast")                                                                 # option to go to Maine

    choice = input("> ")

    if choice == "1":
        go_to_washington()
    elif choice == "2":
        go_to_maine()
    else:
        print("Invalid choice, try again.")
        start_adventure()

def go_to_washington():                                                             # start of the Washington function
    print("You have decided to go to Washington, how do you want to get there?")    # asking how you want to travel
    print("1. Walk")                                                                # option 1 (walk)
    print("2. Take a horse and wagon")                                              # option 2 (take a horse and wagon)

    choice = input ("> ")

    if choice == "1":
        walk_to_washington()
    elif choice == "2":
        wagon_to_washington()
    else:
        print("invalid choice, try again.")
        start_adventure()

def go_to_maine():                                                                  # start of the Maine function
    print("You have decided to go to Maine, how do you want to get there?")         # asking how you want to travel
    print("1. Walk")                                                                # option 1 (walk)
    print("2. Take a horse and wagon")                                              # option 2 (take a horse and wagon)

    choice = input("> ")

    if choice == "1":
        walk_to_maine()
    elif choice == "2":
        wagon_to_maine()
    else:
        print("invalid choice, try again.")
        start_adventure()

# USER DECIDED WHERE THEY WANTED TO GO AND HOW TO GET THERE. BELOW IS FUNCTIONS FOR AFTER THE USER DECIDED HOW TO GET THERE


def walk_to_washington():                                                                                                           # walking to washington function
    print("You are walking to Washington. How do you plan on getting to the other side of the Rocky Mountains?")                    # asking user how to get over rocky mountains
    print("1. Go over the mountain. This is faster but the forecast shows there will possibly be a snowstorm")                      # option 1 (go over the mountain to get there)
    print("2. Go around the mountains. This is longer and you will miss that possible snowstorm")                                   # option 2 (go around the mountain)

    choice = input("> ")

    if choice == "1":
        over_rocky_mountains()
    elif choice == "2":
        around_rocky_mountains()
    else:
        print("invalid choice, start over")
        start_adventure()


def wagon_to_washington():                                                                                               # wagon and horse to washington
    print("You have decided to take a wagon and horse to Washington. When do you want to leave?")                        # asking user when they want to leave
    print("1. Tomorrow")                                                                                                 # option 1 (you would leave tomorrow morning)
    print("2. Friday")                                                                                                   # option 2 (you would leave friday morning)

    choice = input("> ")

    if choice == "1":
        leave_tomorrow()
    elif choice == "2":
        leave_friday()
    else:
        print("invalid choice, start over")
        start_adventure()


def walk_to_maine():                                                                                                                # walking to maine function
    print("You have decided to walk to Maine. How do you plan on getting to the other side of the Appalachian Mountains?")
    print("1. Go over the mountains. This would be quicker, but there is a possibility you would run into some hillbillies")        # option 1 (go over the mountains)
    print("2. Go around the mountains. This would take longer, but it is safer and you could run out of food")                      # option 2 (go around the mountains)

    choice = input("> ")

    if choice == "1":
        over_appalachian_mountains()
    elif choice == "2":
        around_appalachian_mountains()
    else:
        print("invalid choice, start over")
        start_adventure()


def wagon_to_maine():                                                                                                                       
    print("You have decided to take a wagon and horse to Maine, this is the longest journey, what do you want to bring?")                   # wagon and horse to maine funcion
    print("1. Lots of food and water, a spare wheel, a bow, arrows, a knife, tent, and a jacket")                                           # option 1 (lots of food)
    print("2. Little food and water, lots of blankets, a knife, fire equipment, tent, and medicine")                                        # option 2 (little food)

    choice = input("> ")

    if choice =="1":
        lots_of_food()
    elif choice == "2":
        little_food()
    else:
        print("invalid choice, start over")
        start_adventure()


#  FUNCTIONS OF MORE CHOICES LIKE GOING OVER OR AROUND MOUNTAINS, WHEN THE USER WANTS TO LEAVE, AND WHAT THEY WANT TO BRING


def over_rocky_mountains():                                                                                                                                                       # go over rocky mountain function
    print("You have picked to go over the rocky mountains. When you are on top of the mountains a blizzard decides to come on top of the mountain. What do you want to do?")      
    print("1. Stay on top of the mountain and wait for the blizzard to pass by")                                                                                                  # option 1 (stay on top of mountain)
    print("2. Keep walking to the other side of the mountain through the blizzard")                                                                                               # option 2 (walk through the blizzard)

    choice = input("> ")

    if choice == "1":
        stay_on_mountain()
    elif choice == "2":
        keep_walking_rockies()
    else:
        print("invalid choice, start over")
        start_adventure()


def around_rocky_mountains():                                                                                                                                       # around rocky mountain function
    print("You decided to go around the rocky mountains, which is the longer route. You are starting to run out of food, what do you want to do?")
    print("1. Turn around and go home")                                                                                                                             # option 1 (go home)
    print("2. Keep going and go hunting for food")                                                                                                                  # option 2 (hunt for food)

    choice = input("> ")

    if choice == "1":
        go_home()
    elif choice == "2":
        hunt_for_food_rockies()
    else:
        print("invalid choice, start over")
        start_adventure()


def leave_tomorrow():                                                                                                            # leave tomorrow function
    print("You have decided to leave tomorrow morning. What do you want to do?")
    print("1. Go to bed")                                                                                                        # option 1 (go to bed)
    print("2. Pack your stuff")                                                                                                  # option 2 (pack your stuff)

    choice = input("> ")

    if choice == "1":
        go_to_bed()
    elif choice == "2":
        pack_your_stuff()
    else:
        print("invalid choice, start over")
        start_adventure()
        
        
def leave_friday():                                                                                                                                    # leave friday function
    print("You have decided to leave Friday, what do you want to do to pass time?")                 
    print("1. Go to work")                                                                                                                             # option 1 (go to work)
    print("2. go visit your neighbors at their bakery")                                                                                                # option 2 (go visit neighbors)

    choice = input("> ")

    if choice == "1":
        go_to_work()
    elif choice == "2":
        visit_neighbors_bakery()
    else:
        print("invalid choice, start over")
        start_adventure()


def over_appalachian_mountains():                                                                                              # go over appalachian mountains function
    print("You have decided to go over the appalachian mountains and run into hillbillies. What do you want to do?")
    print("1. go talk to them")                                                                                                # option 1 (go talk to hillbillies)
    print("2. fight them")                                                                                                     # option 2 (fight hillbillies)

    choice = input("> ")

    if choice == "1":
        talk_to_hillbillies()
    elif choice == "2":
        fight_hillbillies()
    else:
        print("invalid choice, start over")
        start_adventure()


def around_appalachian_mountains():                                                                                                                     # go around appalchian mountains function
    print("You have picked to go around the appalachian mountains. By doing this you started to run out of food, what do you want to do?")
    print("1. Stop at the nearest village")                                                                                                             # option 1 (stop at the nearest village)
    print("2. Carry on your journey")                                                                                                                   # option 2 (carry on your journey)

    choice = input("> ")

    if choice == "1":
        stop_at_village()
    elif choice == "2":
        carry_on_journey()
    else:
        print("invalid choice, start over")
        start_adventure()


def lots_of_food():                                                                                                                                # lots of food function
    print("You have picked to bring a lot of food and your wheel broke, what do you want to do?")
    print("1. fix it with spare wheel")                                                                                                            # option 1 (fix wheel)
    print("2. ditch it and keep going without your wagon and go with your horse")                                                                  # option 2 (ditch wagon)

    choice = input("> ")

    if choice == "1":
        fix_wheel()
    elif choice == "2":
        ditch_wagon()
    else:
        print("invalid choice, start over")
        start_adventure()


def little_food():                                                                                                                           # little amount of food function
    print("You have picked to bring a little amount of food, what do you want to do?")
    print("1. carry on the trip")                                                                                                            # option 1 (carry on your journey)
    print("2. stop at the nearest store")                                                                                                    # option 2 (stop at the nearest store)

    choice = input("> ")

    if choice == "1":
        go_with_little_food()
    elif choice == "2":
        stop_at_store()
    else:
        print("invalid choice, start over")
        start_adventure()


# START OF MORE FUNCTIONS

def stay_on_mountain():                                                                                                                      # stoy on mountain function
    print("You have stayed on top of the mountain and you got buried in snow and died from hypothermia. start over")                         # user dies
    start_adventure()                                                                                                                        # start the game over


def keep_walking_rockies():                                                                                                                     # keep walking on the rockies function
    print("You have decided to walk through the blizzard, you made it out alive. You see a small town in the distance, do you want to?")
    print("1. stop at the town")                                                                                                                # option 1 (stop at the town)
    print("2. not visit the town")                                                                                                              # option 2 (don't stop at the town)

    choice = input("> ")

    if choice == "1":
        stop_at_town()
    elif choice == "2":
        not_visit_town()
    else:
        print("invalid choice, start over")
        start_adventure()


def go_home():                                                                                                                                  # go home function
    print("You have decided to go home and you live happily ever after. start game over")                                                       # user  lives happily ever after and game starts over
    start_adventure()

def hunt_for_food_rockies():                                                                                                                     # hunt for food on rockies functtion
    print("You run into a wolf while hunting for food, what do you want to do?")                                                                 # user runs into a wolf
    print("1. Try to befriend it")                                                                                                               # option 1 (befriend wolf)
    print("2. try to fight it")                                                                                                                  # option 2 (fight the wolf)

    choice = input("> ")

    if choice == "1":
        befriend_wolf()
    elif choice == "2":
        fight_wolf()
    else:
        print("invalid choice, start over")
        start_adventure()

def go_to_bed():                                                                                                                                                                         #go to bed function
    print("You have decided to go to bed right away. When you wake up you found out that you have been effected by a plague that is going through your town. Do you want to:")
    print("1. cancel the whole trip")                                                                                                                                                    # option 1 (cancel trip)
    print("2. go see the doctor")                                                                                                                                                        # option 2 (go see doctor)

    choice = input("> ")

    if choice == "1":
        cancel_trip()
    elif choice == "2":
        go_see_doctor()
    else:
        print("invalid choice, start over")
        start_adventure()

def pack_your_stuff():                                                                                                                                                                  # pack your sstuff function
    print("You have finished packing and are planning on going to bed, what do you want to do before you go to bed?")
    print("1. make something to eat before bed")                                                                                                                                        # make something to eat
    print("2. go shower")                                                                                                                                                               # go shower

    choice = input("> ")

    if choice == "1":
        make_food()
    elif choice == "2":
        go_shower()
    else:
        print("invalid choice, start over")
        start_adventure()

def go_to_work():                                                                                                                                                       # go to work function
    print("You have decided to go to work and decided to never go to Washington. Start over")
    start_adventure()

def visit_neighbors_bakery():                                                                                                                                           # visit neighbors function
    print("You have decided to go visit your neighbors at their bakery. They kidnap you and force you to work for them the rest of your life. Try the game again")      # user is kidnapped
    start_adventure()                                                                                                                                                   # start the game over

def talk_to_hillbillies():                                                                                                                                                                                  # talk to hillbillies function
    print("You go to talk the hillbillies and they take you into the local blacksmith. They take you to the basement and lock you up in the dungeon for the rest of your life. Try the game again")         # user is locked up for life
    start_adventure()

def fight_hillbillies():                                                                                                                                                # fight hillbillies
    print("You have picked to fight the hillbillies and they end up poisoning you and you die. Start over")                                                             # user died
    start_adventure()

def stop_at_village():                                                                                                                                                  # you stop at the village
    print("They had magical powers that took all of your knowledge away and trained you to be a farmer. Start over")                                                    # you are trained to be a farmer, start over
    start_adventure()

def carry_on_journey():                                                                                                                                                 #  carry on journey function
    print("You have decided to carry on with your journey, do you want to camp out in the middle of the woods?")
    print("1. Yes")                                                                                                                                                     # option 1 (yes)
    print("2. No")                                                                                                                                                      # option 2 (no)

    choice = input("> ")

    if choice == "1":
        camp_out_woods()
    elif choice =="2":
        dont_camp_woods()
    else:
        print("invalid choice, start over")
        start_adventure()

def fix_wheel():                                                                                                                                                        # fix wheel function
    print("You decided to fix the wheel and you forgot to tie your horse up while fixing it and the horse roams off. What do you want to do?")
    print("1. find the horse")                                                                                                                                          # option 1 (find the horse)
    print("2. leave everything and just walk the rest")                                                                                                                 # option 2 (walk rest of the waY)

    choice = input("> ")

    if choice == "1":
        find_horse()
    elif choice == "2":
        leave_everything()
    else:
        print ("invalid choice, start over")
        start_adventure

def ditch_wagon():                                                                                                                                                                                  # ditch wagon function
    print("You decided to ditch your wagon and take your horse. While crossing over a river, your horse got stuck. You tried to get your horse out and you died of drowning. Start over")           # usere dies by drowning, start over
    start_adventure()

def go_with_little_food():                                                                                              # little amount of food function
    print ("You run out of food and die of starvation. start over")                                                     # you run out of food and die of starvation
    start_adventure()

def stop_at_store():                                                                                                                                                                                                                       # stop at store function
    print("You have decided to go the store and you got hit by another horse and buggy on the way. You are in critical condition and spend months in the hospital, while there is nothing to save you. You died 3 months later. Start over")           # critically injured to due to get hit by a horse and buggy and die, start over
    start_adventure()



# START OF THE NEXT ROUND OF FUNCTIONS (MORE TOWARDS THE ENDING)
    
def stop_at_town():                                                                                                                                                     # stop at town function
    print("You have picked to stop at the town and they do not allow outside people to come in. They hold you captive and use you as a sacrafice. Start over")          # used as a sacrafice
    start_adventure()

def not_visit_town():                                                                                                               # not to stop at town function
    print("You picked not to visit the town and made it there safely. Congratualations, you have won the game. start over")         # USER WINS THE GAME    
    start_adventure()

def befriend_wolf():                                                                                                                # user befriends the wolf function
    print("You and the wolf have become best friends and you live happily ever after with the wolf and it's pack. Try again")       # user lives with the wolves the rest of their live, start over
    start_adventure()

def fight_wolf():                                                                                                                                                                                                  # fight wolf function
    print("You have picked to fight the wolf. During the intense battle the wolf called for back up to help injure you. They eventually leave you alone and you end up bleeding to death. Start over")             # user bleeds to death by fighting wolves, start over
    start_adventure()

def cancel_trip():                                                  # user cancels trip function
    print("You cancelled the whole trip, start over")               # cancel trip, start over
    start_adventure()

def go_see_doctor():                                                                                            # go see doctor function
    print("You go see the doctor and your symptoms keep getting worse. You die a week later. Start over")       # user dies of sickness, start over
    start_adventure()

def make_food():                                                                                                                                        # make food function
    print("You made food but there was an accidental cross contamination with peanuts and die due to a severe allergic reaction. start over")           # user dies of severe allergic reaction
    start_adventure()

def go_shower():                                                                                    # go shower function
    print("You slipped trying to get out of the shower and got put into a coma. start over")        # user gets concussion and put into a coma, start over
    start_adventure()

def camp_out_woods():                                                                           # camp out in woods function
    print("You have decided to camp out in the woods, do you want to start a fire?")            # ask user if they want to start a fire
    print("1. Yes")                                                                             # option 1 (yes)
    print("2. No")                                                                              # option 2 (no)

    choice = input("> ")

    if choice == "1":
        start_fire()
    elif choice == "2":
        no_fire()
    else:
        print("invalid choice, start over")
        start_adventure()

def dont_camp_woods():                                                                                                                  # don't camp out in woods functtion
    print("You decided not to camp in the woods and then the night comes fast and you are lost in the woods forever. start over")       # user is lost in the woods forever, start over
    start_adventure()

def find_horse():                                                                                       # find horse function
    print ("You tried to find your horse and accidentally fell off a mountain. start over")             # user falls off the mountain, start over
    start_adventure()

def leave_everything():                                                                                                                                                         # leave everything function
    print("You decided to leave everything and walk the rest of the way there. You ran out of food and no one was near to give you some, you died of starvation. Start over")   # user died of starvation, start over
    start_adventure()

# MORE FUNCTIONS

def start_fire():                                                                                                         # start fire function
    print("You accidentally set your tent on fire while you were in it and couldn't get out alive, start over")           # set tent on fire and died in fire, start over
    start_adventure()

def no_fire():                                                                                                          # no fire function
    print("You picked not to start a fire and get severe hypothermia and have to ampuatate your feet. start over")      # got severe hypothermia and had to amputate feet, start over
    start_adventure()


start_adventure()