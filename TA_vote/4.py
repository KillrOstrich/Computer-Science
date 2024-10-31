import random

# Initialize total fish variable
total_fish = 0

# Initialize player skills
rage = 9000
fire_elem = 1
wind_elem = 1
physical_ability = 3
fast_learner = 2

# Story Introduction
def intro():
    print("Your story begins with you trapped in a world heavily influenced by magic and swords. As you spawn in the world, there are also other people that are in the world. You must navigate the forest in order to reach the village which is safe from all harm.")
    print("You are in the presence of a great mage.")
    print("The mage says:")
    print(">WELCOME TO THIS WORLD. As the last person here, I will give you all the magic skills that everyone did not take when coming here.")
    print("You have learned level 1 fire element, level 1 wind element, Unique skill: fast learner level 2 (learn things twice as fast), and level 3 physical ability.")
    print("Go ahead and start your adventure")
    start_story()

# First Encounter
def start_story():
    print("You are spawned in the middle of a forest. What would be your first action:")
    print("1. Figure a way to navigate the forest and head to the village.")
    print("2. Turn back and try to go back home.")
    choice = input("> What is your decision (1 or 2)\n>")

    if choice == "1":
        forest_entrance()       #This bring them to 2nd encounter
    elif choice == "2":
        print("You could not find your way back home so you are forever lost in the forest.")
        print("GAME OVER")
        exit()  #Just an ending/Not true ending
    else:
        print("Invalid choice. Try again.")
        start_story()

# Second Encounter
def forest_entrance():
    print("You have entered the forest and you notice you're quite hungry.")
    print("What would you do:")
    print("1. Continue on your journey and head to the river.")
    print("2. Eat some of the mushrooms that you see on the floor.")
    choice = input("> What is your decision (1 or 2)\n>")

    if choice == "1":
        river_encounter()       #3rd
    elif choice == "2":
        mushroom_encounter()        #Future consequences
    else:
        print("Invalid choice. Try again.")
        forest_entrance()       #Prevents other things

# Third Encounter
def river_encounter():
    print("You head to the river and see some fish.")
    print("You try to grab some fish in the water but then you collect 1 fish.")
    print("But then you encounter a Komodo Dragon crawling towards you.")
    print("What would you do:")
    print("1. Fight the Komodo Dragon.")
    print("2. Run away from it.")
    choice = input("> What would you choose (1 or 2)\n>")

    if choice == "1":
        fight_komodo() 
    elif choice == "2":
        flee_komodo()
    else:
        print("Invalid choice. Try again.")
        river_encounter()


def fight_komodo():
    global physical_ability, total_fish  #Making them global
    physical_ability += 1                #they gain 1 in physical
    fish_gained = random.randint(1, 10)     #A random amount of fish they gain/Effects the story
    total_fish += fish_gained
    print(f"You have fought the Komodo Dragon, killing it and you gained {fish_gained} fish. And you have gained +1 physical ability.")         #using formating to store fish
    print("You have fought the Komodo dragon, defeating it and gaining new skills!")
    back_in_forest()

def flee_komodo():
    global total_fish
    total_fish += 1
    print("You flee from the Komodo Dragon gaining 1 fish.")
    back_in_forest()




# 4th Encounter
def mushroom_encounter():
    print("You eat the mushroom and now your hunger is restored. Then, you continue your walk into the forest.")            #This from 2nd encounter
    print("Suddenly, you feel dizzy and your vision blurs.")
    print("You realize the mushrooms were poisonous. You must quickly save yourself.")
    print("What would you do:")
    print("1. Try to find an antidote in the forest.")
    print("2. Sit down and hope the effects wear off.")
    choice = input("> What is your decision (1 or 2)\n>")

    if choice == "1":
        find_antidote()
    elif choice == "2":
        print("You sit down, hoping the effects will wear off, but they don't.")
        print("Your vision fades to black, and you realize this is the end of your adventure.")
        print("GAME OVER")
        exit()
    else:
        print("Invalid choice. Try again.")
        mushroom_encounter()


def find_antidote():
    print("You desperately search for an antidote and find a strange herb that seems promising. Then you end up back in the forest.")           #Heal from picking the muchroom path
    print("You eat the herb and slowly start to feel better.")
    back_in_forest()

# 5th Encounter
def back_in_forest():
    print("You find yourself back in the forest, feeling better but still wary of your surroundings.")
    print("What would you do next:")
    print("1. Try to navigate to the village.")
    print("2. Find a safe place to rest.")
    choice = input(">What is your decision (1 or 2)\n>")

    if choice == "1":
        encounter_bandits()
    elif choice == "2":
        find_cave()
    else:
        print("Invalid choice. Try again.")
        back_in_forest()

# 6th Encounter
def encounter_bandits():
    print("You continue your journey through the wood and encounter some bandits.")
    print("1. Fight the bandits.")
    print("2. Run away from the bandits to get some rest in a cave.")
    choice = input("> What is your decision (1 or 2)\n>")

    if choice == "1":
        print("You have been captured by the bandits, selling you off to slavery.")
        print("GAME OVER")
        exit()
    elif choice == "2":                                         #They gain bonus from this
        find_treasure()
    else:
        print("Invalid choice. Try again.")
        encounter_bandits()


def find_treasure():
    global fire_elem, wind_elem, physical_ability, fast_learner                     #Adding to global variables/They should have 4 in all stats
    print("You found a chest that gave you +4 on all your abilities.")
    fire_elem += 4
    wind_elem += 4
    physical_ability += 4
    fast_learner += 4
    print("Then you find a cave. You go into the cave and get some rest.")
    find_cave()


def find_cave():
    global total_fish
    print("You are in a cave. You are hungry so you use the fish that you have.")                   #If they went the mushroom path they die/if they went the komodo dragon path they live
    if total_fish > 0:                                                                      #Encounters playing a role
        total_fish -= 1
        print(f"You eat a fish to restore your energy. You have {total_fish} remaining.")
    else:
        print("You have no fish to eat and you die in the cave.")
        print("GAME OVER")
        exit()
    middle_of_forest()

#7th Encounter
def middle_of_forest():
    print("Now after exiting the cave, you see a group of people.")         #This splits the path for the user
    print("1. Interact with the group of people.")
    print("2. Ignore the group of people.")
    choice = input(">Which would you choose (1 or 2)\n>")

    if choice == "1":
        encounter_allies()
    elif choice == "2":
        encounter_bandit_solo()
    else:
        print("Invalid choice. Try again.")
        middle_of_forest()

# 8th Encounter
def encounter_allies():
    print("You interacted with the group of people, befriending them and teaching how to use their magic. They in return help you try to reach the village.")           #A function to lvl up the user/They should pick 1 if they want to progress
    print("Now that you have allies, you guys encounter Goblins and a wolf.")
    print("1. Fight the Goblins and wolf.")
    print("2. Run away from the Goblins and wolf.")
    choice = input("Which would you pick (1 or 2)\n>")

    if choice == "1":
        gain_abilities()
    elif choice == "2":
        print("You and your allies ran away from the Goblins and wolf don't gain any experience.")
        after_goblins()
    else:
        print("Invalid choice. Try again.")
        encounter_allies()

# 9th Encounter
def encounter_bandit_solo():                                                                #If they click 2 of the 7th encounter
    global fire_elem, wind_elem, physical_ability, fast_learner
    print("You ignore them and encounter a single bandit.")
    print("1. Fight the Bandit.")
    print("2. Run away from the bandit.")
    choice = input("Which would you pick (1 or 2)\n>")

    if choice == "1":
        if fire_elem >= 4 and wind_elem >= 4 and physical_ability >= 4 and fast_learner >= 4:               #They should have 4 in all points rn
            print("You beat the bandit, obtaining a map to the village and you exit the forest.")
            print("GAME COMPLETED")                                                                         #1ST DISTINIT ENDING
            exit()
        else:
            print("You died to the bandit.")
            print("GAME OVER")
            exit()
    elif choice == "2":
        print("You ran so fast that you accidentally ran over a cliff leading to your death.")
        print("GAME OVER")
        exit()
    else:
        print("Invalid choice. Try again.")
        encounter_bandit_solo()

#
def gain_abilities():                                                           #They have 7 in all stats
    global fire_elem, wind_elem, physical_ability, fast_learner
    fire_elem += 2
    wind_elem += 2
    physical_ability += 2
    fast_learner += 2
    print("You have beaten the Goblin and wolf leveling up all your abilities +2. And you and your allies are back in the forest.")
    after_goblins()

# 10th Encounter
def after_goblins():
    print("After the encounter with the Goblins, you see a cave.")                  #This gets them ready for the true ending
    print("You go towards the cave and then you see a Three headed wolf")
    print("1. Do you wish to fight the Three headed wolf")
    print("2. Do you wish to run from the three headed wolf")
    choice = input("What option would you pick (1 or 2)\n>")
    if choice == "1":
        three_headed_wolf()
    elif choice == "2":
        after_three_headed_wolf()
    else:
        print("Invalid choice. Try again.")
        after_goblins()


def three_headed_wolf():
    global fire_elem, wind_elem, physical_ability, fast_learner
    
    if fire_elem >= 7 and wind_elem >= 7 and physical_ability >= 10 and fast_learner >= 8:
        print("You beat the Three headed Wolf gaining 10 PLUS ABILITY POINTS")
        
        fire_elem += 10
        wind_elem += 10
        physical_ability += 10
        fast_learner += 10
        print(f"Fire Element: {fire_elem}, Wind Element: {wind_elem}, Physical Ability: {physical_ability}, Fast Learner: {fast_learner}")                      #They should have 17 for all stats
    else:
        print("You died from the Three-Headed-Wolf due to low stats.")
        print("GAME OVER")
        exit()
    after_three_headed_wolf()

# 11th Encounter
def after_three_headed_wolf():
    print("After the encounter with the Three headed wolf you SEE THE VILLAGE. Despreate you can your group start to run to it.")           #If they followed the right path they should beat it
    print("Getting closer to the village you see Big powerfull mob of people")
    print("1. Engage in combat with the mob.")
    print("2. Run away from the mob.")
    choice = input("What option would you pick (1 or 2)\n>")
    if choice == "1":
        mob_encounter()
    elif choice == "2":
        after_mob()
    else:
        print("Invalid choice. Try again.")
        after_three_headed_wolf()


def mob_encounter():
    global fire_elem, wind_elem, physical_ability, fast_learner
    if fire_elem >= 17 and wind_elem >= 17 and physical_ability >= 20:
        print("You have beaten the mob of people due to your strong abilities and your allies helping you and REACH THE VILLAGE")
        print("YOU HAVE BEATEN THE GAME")                                                                                                       #2ND DISTINCT ENDING
        exit()                                                                                                                                      #The true ending if everything goes good. #I'll minus 14 stats on everything to be kind to people who made it past this part
    else:                                                                                       #1st True ending
        print("You and your group has been captured by the mob selling to slavery")
        print("GAME OVER!")
        exit()

# 12th Encounter
def after_mob():

    print("Your allies enage in combat with the mob but out of scaredoom you ran away leaving the group behead.")       #They should have 7 or more right now for fire and wind
    print("This leads to them beening captured my the mob of people")
    print("1. Do you wish to countine your journey in the the forest")
    print("2. Do you wish to stay in the forest and cry for your allies")
    choice = input("What option would you pick (1 or 2)\n>")
    if choice == "1":
        mob_goblins()
    elif choice == "2":
        print("You finished crying now you want countine your jounery")
        mob_goblins()
    else:
        print("Invalid choice. Try again.")
        after_mob()

# 13th encounter
def mob_goblins():
    print("You then encounter a mob of goblins")
    print("1. Do you wish to fight them as a revolve to get stronger ")
    print("2. Do you wish to ingnore them")
    choice = input("What option would you pick 1 or 2\n>")
    if choice == "1":
        mob_goblins_one()
    elif choice == "2":
        print("You ingnored them, but one of them caught you and now the goblins cooked you")
        print("GAME OVER")
        exit()
    else:
        print("Invalid choice. Try again.")
        mob_goblins()

def mob_goblins_one():          #Some tiny perk for people who are sturggling/I nerf it to people who missed the treasure
    global fire_elem, wind_elem, physical_ability, fast_learner, rage
    if fire_elem >= 3 and wind_elem >= 3 and physical_ability >= 3 and fast_learner >= 3:                           #They gain new skill rage
        print("You defeated all the goblins due to your rage and you earn a new skill and gain + 10 in all stats>")
        print("You learn Rage: Rage is level 9000: Rage lets you boost all your stats by 9000: It has a one time use")
        fire_elem += 10
        wind_elem += 10
        physical_ability += 10
        fast_learner += 10
        print(f"Fire Element: {fire_elem}, Wind Element: {wind_elem}, Physical Ability: {physical_ability}, Fast Learner: {fast_learner}, Rage: {rage}")
        cave_two()
    else:
        print("You died due to not having enought stats")
        print("GAME OVER")
        exit()

# THEY HAVE 17 IN ALLLLLLL STATS OR 13
def cave_two():
    print("You are near a cave and sense a strong being")
    print("Wanting to be strong you go in the cave")
    print("YOU ENCOUNTER A LVL 30 SNAKE BOSS AND SEE the bodies of vituims")
    print("You enagage in combat")
    battle_snake()

#14th Encounter
def battle_snake():
    print("You are now in battle mode you now you make the dicision of every the movement your player makes")               #Putting them in battle mode means they make every decision/ every movement could get them killed or saved
    print("Your player looks at the snake with a bold look to take it down.")
    print("He rushes at the snake witha slight prediction he sees that the snake would hit left")
    print("Where do you want to dodge")
    print("1. Left")
    print("2. Right")                                                                   #Should pick Right/ 2
    choice = input("What option would you pick 1 or 2\n>")
    if choice == "1":
        print("That was the wrong move the snake hit left")
        print("GAME OVER")
        exit()
    elif choice == "2":
        print("That was the right move the snake went left.")
        battle_snake_one()
    else:
        print("Invalid choice. Try again.")
        battle_snake()

#15th Encounter
def battle_snake_one():
    print("With that slight prediction your character rolled left")
    print("You the snake long tail was stuck on the ground which you land one it with your fire magic.")
    print("The snake it now has 70% hp left")
    print("The snake gets agitated, and now it quickly hits you back")
    print("With that hit the snake inject some of it's poison in you")                                      #They get poisoned
    print("Then the snake tries to attack you by spinning around. How would you dodge it?")
    print("1. Jump over it")
    print("2. Try to out run the snake")                                                                                #Should jump over it/ 1
    choice = input("What option would you pick 1 or 2\n>")
    if choice == "1":
        print("You have jump over the snake spinning attack, successfully avoiding it.")
        battle_snake_two()
    elif choice == "2":
        print("As you try to out run the snake you lose your stamina and die to the snake.")
        print("GAME OVER")
        exit()
    else:
        print("Invalid choice. Try again.")
        battle_snake_one()

#16th Encounter
def battle_snake_two():
    print("After successfully avoiding the snake you launch a deadly counter attack blinding the snake.")           #Its blind
    print("The snake out of agony screams out loud further increasing the poison spreading in your body.")
    print("Closer to victory you then see some shine behind the snake.")
    print("1. Do you wish to deliver the finishing blow to the snake")              #They can auto kill snake if they pick this
    print("2. Do you wish to obtain the shiny object")                                          #This gives them the antidote
    choice = input("What option would you pick 1 or 2\n>")
    if choice == "1":
        finishing_blow()
    elif choice == "2":
        shiny_object()
    else:
        print("Invalid choice. Try again.")
        battle_snake_two()

#17th Encounter
def finishing_blow():
    print("As you run up the cliff of the cave and dive towards")
    print("The snake predicts your movement and shoots his tail towards you.")
    print("The tail moves so fast you don't know where go. Where would you dodge?")                         #50/50 option just to make the game fun
    print("1. Right")                                                                       #Right pick
    print("2. Left")
    choice = input("What option would you pick 1 or 2\n>")
    if choice == "1":
        print("You've successfully dodged the snake/You killed the snake.")
        after_finishing_bow()
    elif choice == "2":
        print("You've unsuccessfully dodged the snake")
        print("GAME OVER")
        exit()
    else:
        print("Invalid choice. Try again.")
        finishing_blow()

#Still got shiny_object left

def after_finishing_bow():
    global fire_elem, wind_elem, physical_ability, fast_learner, rage               #They gain some stats
    print("End of Battle Mode")
    print("You successfully beaten the snake and gain + 50 in all ability")
    fire_elem += 50
    wind_elem += 50
    physical_ability += 50
    fast_learner += 50
    rage += 50
    print(f"Fire Element: {fire_elem}, Wind Element: {wind_elem}, Physical Ability: {physical_ability}, Fast Learner: {fast_learner}, Rage: {rage}")
    print("You then walk out the the cave extremely tried, but then you experience a deadly attack on your body.")
    print("It must have been the snake poison. You heavily clinch on to you body hopeful trying to over come the poison.")
     # 30% chance of survival
    survival_chance = random.random()
    if survival_chance <= 0.30:                                                                         #Sixteen Encounter effecting this story
        print("On death door you miraculously survive the poison.")
        after_snake()
    else:
        print("The poison overcomes you and takes your life.")
        print("GAME OVER")
        exit()

#Shiny object
def shiny_object():
    global fire_elem, wind_elem, physical_ability, fast_learner, rage
    print("You run towards the shiny object desperately in order to figure out what it is.")
    print("The snake attacks you but you dodge it. This gives you enough time to reach the shiny object and noticing that it is a chest.")
    print("Seeing that it is a chest you open it and it gives you an antidote for the poison and + 10 in all stats.")
    fire_elem += 10                         #Gain something from the chest
    wind_elem += 10
    physical_ability += 10
    fast_learner += 10
    rage += 10
    print("The snake predicts that you are near the chest so he strikes you down with ultra fast tail.")
    print("Now that you are stronger you predict the snake and you dodge the attack.")
    print("Then you deliver a deadly long air like attack with your sword killing the snake")
    print("You successfully beaten the snake and gain + 50 in all ability")
    print("End of Battle Mode")
    fire_elem += 50
    wind_elem += 50                     #They beat Snake/ They have 60 or 70 in each stats
    physical_ability += 50
    fast_learner += 50
    rage += 50
    print(f"Fire Element: {fire_elem}, Wind Element: {wind_elem}, Physical Ability: {physical_ability}, Fast Learner: {fast_learner}, Rage: {rage}")
    print("You then drink the antidote for the poison in your body and exit the cave.")
    after_snake()

#18th Encounter
def after_snake():
    print("After beating the snake your are now the strongest person in the forest")
    print("You then see bandits taking away someone. What would you do:")
    print("1. Attack the bandits")
    print("2. Ignore the bandits")
    choice = input("What option would you pick 1 or 2\n>")
    if choice == "1":
        print("You've beaten the bandits saving the people")
        journey_to_village()
    elif choice == "2":
        print("You have ignored the bandits")
        journey_to_village()
    else:
        print("Invalid choice. Try again.")
        after_snake()

#19th Encounter/New story for user
def journey_to_village():
    print("After the encounter with the bandits you think that you should become the king of the forest instead of going to the village")           #This splits the outcome of the story/Lets user pick there story.
    print("Where do you want to continue your story?")
    print("1. Head to the village")
    print("2. Become King of the forest")
    choice = input("What option would you pick (1 or 2)\n>")
    if choice == "1":
        village()
    elif choice == "2":
        king_forest()
    else:
        print("Invalid choice. Try again.")
        journey_to_village()

#20th Encounter                                                                               Dont forget king_forest function
def village():
    print("Has you you continue walking you a group of people in the over the bushes")
    print("1. Do you wish to interact with them")
    print("2. Do you wish to ignore them.")
    choice = input("What option would you pick (1 or 2)\n>")
    if choice == "1":
        family()
    elif choice == "2":
        continue_journey()
    else:
        print("Invalid choice. Try again.")
        village()

#Ending
def family():
    print("As you approach them they turn out to be your family")
    print("They have built a house to stay and are living peacefully")
    print("Out of happyness you join them and live a happy life")
    print("YOU HAVE BEATEN THE GAME")                                                   #3RD DISTINCT ENDING
    exit()


def continue_journey():
    print("As you continue your walk in the forest you then see the village, but then you see a mob.")
    print("Since your overwhelming strong you defeat the mob gaining + 10 in all stats.")
    print("You have now reach the village.")
    print("YOU'VE BEATEN THE GAME")                                                 #4TH DISTINCT ENDING
    exit()

#21th Encoutner
def king_forest():
    print("With the resolve of become you then sense a gaint being on top of a mountain")
    print("You run towars the mountain knowing that you can take down the beast")
    print("You encounter a lvl 8000 Giant Wolf")
    print("Before you could run away the cave door closes and you are left you fight it")
    print("Looking at the monster you decide to use a skill")
    print("What skill would you use?")
    print("1. Fire")
    print("2. Wind")
    print("3. Rage")                                                                            #They should pick Rage/3 if they are smart
    choice = input("What option would you pick (1, 2 or 3)\n>")
    if choice == "1":
        print("You use your skill at the Wolf but it had no effect on the Wolf, so the Wolf quickly killed you")
        print("GAME OVER")
        exit()
    elif choice == "2":
        print("You use your skill at the Wolf but it had no effect on the Wolf, so the Wolf quickly killed you")
        print("GAME OVER")
        exit()
    elif choice == "3":
        king()
    else:
        print("Invalid choice. Try again")
        king_forest()

#Final Function
def king():
    global fire_elem, wind_elem, physical_ability, fast_learner
    print("You used your rage skill buffing your all you stats by 9000")
    fire_elem += 9000
    wind_elem += 9000
    physical_ability += 9000
    fast_learner += 9000
    print(f"Fire Element: {fire_elem}, Wind Element: {wind_elem}, Physical Ability: {physical_ability}, Fast Learner: {fast_learner}")
    print("With these buffed stats you are strong enough to beat the Giant Wolf")
    print("With many attacks from the Wolf you dodged them and land a finishing blow to the wolf becoming the KING OF THE FOREST")                      #5TH DISTINCT ENDING
    print("GAME COMPLETED")                                                                                                                                         #2nd True ending
    exit()






    

    










    







def sum_of_story():
    intro()
    start_story()
    forest_entrance()
    river_encounter()
    fight_komodo()
    flee_komodo()
    mushroom_encounter()
    find_antidote()
    back_in_forest()
    encounter_bandits()
    find_treasure()
    find_cave()
    middle_of_forest()
    encounter_allies()
    encounter_bandit_solo()
    gain_abilities()
    three_headed_wolf()
    after_three_headed_wolf()
    mob_encounter()
    after_mob()
    mob_goblins()
    mob_goblins_one()
    cave_two()
    battle_snake()
    battle_snake_one()
    battle_snake_two()
    finishing_blow()
    after_finishing_bow()
    shiny_object()
    after_snake()
    journey_to_village()
    village()
    continue_journey()
    king_forest()
    king()
    exit()
sum_of_story()