#The start of the story, give background information about the adventure
def start_of_the_adventure():
    print("You are in the 17th Airborne Division or The Golden Talons")
    print("The date is January 3rd, 1945")
    print("DAY 1: DAY BEFORE THE MISSION")
start_of_the_adventure()
#The first choice, deciding to go or not
def day1_the_decision():#Encounter num 1
    print("You have been in the 17th Airborne Division for 2 years.")
    print("You have been waiting to be deployed and the time finally arrived.")
    print("The mission, if you decide to go on, would soon be known as\nDead Man's Ridge.")
    print("Here are your options.\n1. Accept the mission\n2. Refuse getting deployed.")
    deciding = input("> ")
    if deciding == "1":
        go_on_mission()
    elif deciding == "2":
        dont_go()
    else:
        print("Decide by using 1 or 2")
        day1_the_decision()
def go_on_mission():
    print("You have decided to go, you start flying out tonight.")
    day2_the_jump()
def dont_go():#Arrested 1st way for game to end
    print("You were arrested for insubordination.\nGAME OVER")
#The second choice, leads to if you jump early, you could live, if you stay for longer you have a chance of get shot down.
def day2_the_jump():#2nd encounter
    print("DAY 2: THE JUMP\nJannuary 4th, 1945, it is 8:00. The drop time is 8:15.")
    print("You are almost to the drop point, nerves are getting to you. you have done over 100 drops, but this one feels different.")
    print("8:15, the pilot says he wants to go a little further before the jump, but you were told to stay on the mission.")
    print("1. Stay on the plane and jump somewhere else\n2. Tell your team to jump now")
    the_jump = input("> ")
    if the_jump == "2":
        jump_now() 
    elif the_jump == "1":
        wait_to_jump()
    else:
        print("Decide by using 1 or 2")
        day2_the_jump()
def jump_now():
    print("8:23, you and your team have just landed and are packing up your parachutes")
    day2_boots_down()
def wait_to_jump():
    print("8:23, you here flack and AA guns shooting. Gunfire lights up the sky all around you.")
    import random 
    r = random.random()
    if r < 0.50:
        print("The wing of the plane has been clipped, you and your team need to jump now.")
        day2_outside_dp()
    else:
        print("The plane was shot down and crashed.\nGAME OVER")#second way the game can end
#The 3rd encounter, deciding where to go.
def day2_boots_down():
    print("You and your team landed in the drop zone. The plan is to move to the North and push up to the front lines.")
    print("But there is a town 10 miles to the North-East, and to the West there is a known Axis artillery base.")
    print("1. Go North\n2. Go North-East to the town\n3. Go West to the Axis base")
    where_march = input("> ")
    if where_march == "1":
        print("You and your team are marching North")
        day2_march_north()
    elif where_march == "2":
        print("You decided to go to the town.")
        day2_the_town()
    elif where_march == "3":
        print("You are going to a known enemy base")
        day2_go_to_axis_artillery_base()
    else:
        print("Decide using 1,2 or 3")
        day2_boots_down()
#If you survive the plane you are here, another encounter
def day2_outside_dp():#4th encounter
    print("You landed East of the drop point by 5 miles. There is a town just North of you position.")
    print("1. Go to the town\n2. Go around the town to the front lines")
    where_going_from_outside_dp = input("> ")
    if where_going_from_outside_dp == "1":
        print("You are going to the town")
        day2_the_town()
    elif where_going_from_outside_dp == "2":
        print("You are going around the town to the front lines.")
        day2_march_north()
    else:
        print("Decide using 1 or 2")
        day2_outside_dp()
def day2_march_north():#5th encounter 
    print("You decided to march North with your battalion, avoiding the town.\n21:42, you have been marching all day and the soldiers want to stop for the night.")
    print("1. Make camp and stay the night\n2. Keep marching")
    camp_or_not = input("> ")
    if camp_or_not == "1":
        print("You camp on the cold winter plains.\n22:16, you can't feel your hands or feet. You can't move at all.")
        print("You died from hypothermia.\nGAME OVER")
    elif camp_or_not == "2":
        print("19:52, you keep marching and come up on a forest. Your battalion is exhausted so you decide to spend the night.")
        day2_stay_night()
    else:
        print("Decide using 1 or 2")
        day2_march_north()

def day2_stay_night(): #14th encounter
    print("1. Make camp in the forest\n2. Make camp on the icy plains")
    stay_the_night = input("> ")
    if stay_the_night == "1":
        print("You made camp in the forest.")
        day3_the_trees()
    elif stay_the_night == "2":
        print("You camp on the cold winter plains.\n23:57, you can't feel your hands or feet. You can't move at all.")
        print("You died from hypothermia.\nGAME OVER")#3rd way game ends
    else:
        print("Decide using 1 or 2")
        day2_stay_night()

def day3_the_trees():#17th encounter
    print("DAY 3: THE TREES\nJanuary 5th, 1945, it is 6:08")
    print("You get your battalion up. You look out to the planes and see footprints, but they are different from the standard issue boots that your battalion have")
    print("1. Follow the footprints\n2. Go back to your battalion")
    footprints = input("> ")
    if footprints == "1":
        print("You follow the footprints, you walk a ways to follow them...Bang!\nYou got shot by the Axis\nGAME OVER")
    elif footprints == "2":
        print("You go back and as you are getting closer you see blood on the snow.")
        print("There are gunshots now, you caught one in the shoulder.\nGAME OVER")
    else:
        print("Decide using 1 or 2")
        day3_the_trees()

#If you full on assault you have a 20% chance of surviving, if you survive you get captured. 
#If you split you have a 45% chance of living and taking over the base, otherwise you can run away. 
def day2_go_to_axis_artillery_base():#6th encounter
    print("11:25, you are almost to the Axis base.\nYou have came up with 2 plans to attack.")
    print("1. Go all in with a frontal assault\n2. Split into 2 teams and attack from the North and South.")
    axis_artillery_assault = input("> ")
    if axis_artillery_assault == "1":
        print("11:53, you see the Axis forces.\n12:07, the assault begins, you order your troops to open fire. The sound of gunfire floods your ears.")
        print("13:48, you are outgunned and outnumbered. You have lost over half of your battalion.")
        print("But the rest of your troops stand strong.")
        import random 
        r = random.random()
        if r < 0.20:
            print("15:18, the Axis forces used up almost all their resources at the beginning.")
            print("Your forces stormed and claimed the base. All Axis forces have either retreated or been taken out.")
            day3_control_base()
        else:
            print("16:27, there are only a few of you left. Ammo is depleted and you are just laying on the ground.")
            print("Your attack failed, almost all the soldiers that followed you are dead.")
            print("The Axis soldiers have surrounded you, a group walks up to you and grabs you. You have been captured by the Axis forces.\nGAME OVER")
#You have been captured by the Axis, another way the game ends.

    elif axis_artillery_assault == "2":
        print("11:53, you are approaching the Axis base, you split your battalion into 2 groups. You are going with the 1st group, assaulting from the south.")
        print("12:34, the other team radios you, they are waiting for the order to attack.\n12:35, the attack has started.")
        import random
        r = random.random()
        if r < 0.45:
            print("14:41, you have pinched the base, the 2nd group has started to invade inside the base.")
            print("Your forces stormed and claimed the base. All Axis forces have either retreated or been taken out.")
            day3_control_base()
        else:
            print("15:54, you barely hear any gunfire from the North.")
            print("The last radio transmission you got from the 2nd group was 40 minutes ago, they said they were having a hard time holding the Axis back.")
            print("The Axis are pushing you, there is only one thing you can do. You get what is left of your battalion to retreat.")
            print("17:24, you ran from the Axis, helicopters are picking you up to bring you back home.\nGAME OVER")
    else:
        print("Decide by using 1 or 2")
        day2_go_to_axis_artillery_base()

def day3_control_base():#7th encounter
    print("You decide it is best to stay the night at the base.")
    print("DAY 3: AT THE BASE")
    print("6:02, you are getting up your battalion. You have orders to stay at the base until reinforcements arrives.")
    print("1. Stay at the base\n2. Take a small team to keep going")
    decide_at_the_base = input("> ")
    if decide_at_the_base == "1":
        print("You decide to follow orders and keep the base secure.")
        print("It has been a few days, reinforcements finally arrived. The battle is almost to an end.")
        print("Your battalion has been instructed to stay at the base for the remainder of the war.\nGAME OVER")
        #5th way the game ends
    elif decide_at_the_base == "2":
        print("You take a team of 25 other soldiers to go, but where are you going?")
        day3_where_to_go_from_base()
    else:
        print("Decide using 1 or 2")
        day3_control_base()

def day3_where_to_go_from_base():#15th encounter
    print("1.You can go North to the front lines\n2. You can go North-East to the town")
    base_where_go = input("> ")
    if base_where_go == "1":
        print("You start marching North.\n21:04, your troops are getting tired and want to stop for the night.")
        day2_stay_night()
    elif base_where_go == "2":
        day3_the_town_from_base()
    else:
        print("Decide using 1 or 2")
        day3_where_to_go_from_base()

def day3_the_town_from_base():#18th encounter
        print("You are headed to the town.\n12:36, you are entering the town, it looks deserted.")
        print("You are walking down the road and suddenly you see 2 Axis soldiers walk around the corner.")
        print("1. Do you open fire at them\n2. Do you tell your squad to hide")
        the_2_solders = input("> ")
        if the_2_solders == "1":
            print("You and your team open fire at the soldiers, both of the enemy soldiers are down but one of your teammates has hit in the arm.")
            day2_town_battle()
        elif the_2_solders == "2":
            print("Your squad hid behind the corner of a building, you see the soldiers walk away from you.")
            day2_follow_solders()
        else:
            print("Decide using 1 or 2")
            day3_the_town_from_base()
    
def day2_the_town():#8th encounter
    print("You are headed to the town.\n9:13, you are entering the town, it looks deserted.")
    print("You are walking down the road and suddenly you see 2 Axis soldiers walk around the corner.")
    print("1. Do you open fire at them\n2. Do you tell your battalion to hide")
    the_2_solders = input("> ")
    if the_2_solders == "1":
        print("You and your team open fire at the soldiers, both of the enemy soldiers are down and your team doesn't any injuries.")
        day2_town_battle()
    elif the_2_solders == "2":
        print("Your squad hid behind the corner of a building, you see the soldiers walk away from you.")
        day2_follow_solders()
    else:
        print("Decide using 1 or 2")
        day2_the_town()

def day2_follow_solders():#9th encounter
    print("1. Do you take a small group to follow them\n2. Do you let them walk away from you")
    go_after = input("> ")
    if go_after == "1":
        print("You take your group to go after them.")
        day2_trailing_the_solders()
    elif go_after == "2":
        print("You let them go.")
        day2_ambush_by_axis()
    else:
        print("Decide using 1 or 2")
        day2_follow_solders()

def day3_trailing_axis_scouts():#19th encounter 
    print("12:43, you have been following the soldiers throughout the town with your team.")
    print("You hear a lot of talking, the soldiers walk into what looks like a town center. There are more soldiers outside.")
    print("1. Are you going to attack the 5 soldiers outside\n2. Are you going to return to the rest of your battalion")
    town_center=input("> ")
    if town_center == "1":
        print("You attacked to soldiers, 2 of your guys got shot it the leg.")
        print("Suddenly the whole courtyard is full of Axis soldiers. Gunfire is everywhere.\nYou got shot in the chest a few times.\nGAME OVER")
    elif town_center == "2":
        print("You walk back to your battalion and you feel like someone is looking at you so you turn around.")
        print("There are 4 Axis soldiers in the street, they are lifting their guns up. You lift yours up")
        day2_town_battle()
    else:
        print("You have to decide using 1 or 2")
        day3_trailing_axis_scouts()

def day2_trailing_the_solders():#10 encounter 
    print("9:24, you have been following the soldiers throughout the town with a team of 7 others.")
    print("You hear a lot of talking, the soldiers walk into what looks like a town center. There are more soldiers outside.")
    print("1. Are you going to attack the 5 soldiers outside\n2. Are you going to return to the rest of your battalion")
    town_center=input("> ")
    if town_center == "1":
        print("You attacked to soldiers, 1 of your guys got shot it the leg.")
        print("Suddenly the whole courtyard is full of Axis soldiers. Gunfire is everywhere.\nYou got shot in the chest a few times.\nGAME OVER")
    elif town_center == "2":
        print("You walk back to your battalion and you feel like someone is looking at you so you turn around.")
        print("There are 4 Axis soldiers in the street, they are lifting their guns up. You lift yours up")
        day2_town_battle()
    else:
        print("You have to decide using 1 or 2")
        day2_trailing_the_solders()

def day2_ambush_by_axis():#11th encounter
    print("It has been a few hours, suddenly you see 40 or more Axis soldiers running at you. Bullets from both sides start flying.")
    print("1. Keep fighting\n2. Run away and call for backup")
    town_ambush = input("> ")
    if town_ambush == "1":
        print("The Axis soldiers have surrounded you. They are closing in and you have lost a lot of soldiers.")
        print("You have been shot in the neck.\nGAME OVER")
    elif town_ambush == "2":
        print("You have ran with a few soldiers.")
        day2_go_back()
    else:
        print("Decide using 1 or 2")

def day2_go_back():#16th encounter
    print("You left most of your troops behind, are your really going to leave them?")
    print("1. Go back\n2. keep going")
    troops_left_behind = input("> ")
    if troops_left_behind == "1":
        print("You go back, your troops are surrounded and are getting shot down. Axis soldiers see you running toward them.")
        print("You were gunned down by the Axis soldiers\nGAME OVER")
    elif troops_left_behind == "2":
        print("You start to run from the Axis, suddenly you get shot in the leg.")
        print("An Axis sniper is aiming at you, they lock and load another round... BANG!\nGAME OVER")
    else:
        print("Decide using 1 or 2")
        day2_go_back()


def day2_town_battle():#12th encounter
    print("It is silent. The Axis soldiers bodies are laying in the middle of the road")
    print("You hear people running, the sound of magazines clanking and helmets hitting against weapons.")
    print("Suddenly you see 40 or more Axis soldiers running down the road")
    print("Bullets started flying, soldiers from both sides started yelling and falling")
    print("You are pinned down in gunfire for hours\n15:18, the gunfire has died down, it is silent.")
    print("You look around, there are only 16 other soldiers around you. You rally them up and go into a building adjacent to you.")
    print("1. Do you stay in the building until the morning\n2. Do you go out and keep searching the town")
    day2_in_the_building = input("> ")
    if day2_in_the_building == "1":
        print("You decided to stay in the building, you are exhausted so you wait until the morning to decide what to do next.")
        day3_in_the_building()
    elif day2_in_the_building == "2":
        print("You decided to go out and look around the town.")
        print("You see Axis solders outside, you decide to go back in.")
        day3_in_the_building()
    else:
        print("Decide using 1 or 2")
        day2_town_battle()

def day3_in_the_building():#13th encounter
    print("DAY 3: IN THE BUILDING \nJannuary 5th, 1945, it is 5:43.")
    print("You heard gunshots from the North. You have been ordered to go North to the front lines. \n1. Do you go to the gunshots\n2. Do you go around them")
    round_or_not = input("> ")
    if round_or_not == "1":
        print("You come up on a firefight between the French and Axis, you and your team join in.")
        print("You won the battle, a helicopter is here to pick you up.\nGAME OVER")#4th way the game ends
    elif round_or_not == "2":
        print("You go around, suddenly you hear gunshots and your soldiers are dropping.")
        print("Then you fall to the ground...you got shot in the back.\nGAME OVER")
    else:
        print("Decide using 1 or 2")
        day3_in_the_building()


day1_the_decision()

