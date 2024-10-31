print("you are a knight named charlesworth for the royale palace of butterland")            #butterland is a sought after palace, been around for a century
def start_adventure():
    print("The king has ordered you to explore the haunted jungles of bladesville, and retrevive the lost treasures. do you:")
    print("1. accept the journey")                          # pick 1 and you execpt the kings journey
    print("2. punch the king in the face and run away")     # pick 2 and you punch the king and flee the castle
    choice = input("- ")
    if choice == "1":
        accept_journey()
    elif choice == "2":
        Punch_king()
    else:
        print("wrong choice, try again knight.")
        start_adventure()

def accept_journey():
    print("you grab your sword, hop on your horse, and travel to bladesville.")                         # bladesville is a place where most dont want to travel to
    print("the town of bladesville is a dark land and the jungles of bladesville are very very dark.")
    print("you get to the entrance of the jungle and run into an old man with a cane and a peg for a leg.")
    print("The old man asks, What is your name young knight, do you:")
    print("1. tell the old man your real name")         # pick 1 to tell the old man your real name
    print("2. tell the old man a fake name")            # pick 2 to tell the old man your fake name
    choice = input("- ")
    if choice == "1":
        tell_name()
    elif choice == "2":
        fake_name()
    else:
        print("wrong choice, try again knight.")
        accept_journey()

def Punch_king():
    print("you decide to punch the king and flee the castle.")                                                          # punching the king/assualting the king is something you dont want to do, especially at butterland
    print("in the holy lands of butterland it consisdered instant death if you assualt and disrespect the king.")
    print("you hop on your horse and start riding as fast as you can there is 7 other knights chasing after you.")
    print("there is a river coming up and you have a few desisions to make, do you:")
    print("1. ditch the horse and swim across the aligator and snake infested waters.")                                         # pick 1 amd swim in the creature infested waters which is a easy way to get killed
    print("2. make a cut and go into the woodlands of butterland that is also known for its intense speicies of animals.")      # pick 2 and make a cut into the woodlands which is also an easy way to get killed
    choice = input("- ")
    if choice == "1":
        ditch_horse()
    elif choice == "2":
        woodlands()
    else:
        print("wrong choice, try again knight.")
        Punch_king()

def tell_name():
    print("you tell the old man your name, charlesworth")                                   # charlesworth is a family name their are 5 other charlesworth from generations prior
    print("The old name snickers at you and says 'I was once a knight before'.")
    print("you tell the old man you have a busy journey and he wishes you safe travels")
    print("you continue down the path and pull the scroll out the king gave you to see what we must do while in the jungle.")
    print("The scroll is very old and there is a picture of a temple on it, in writing it says the haunted temples of bladesville.")
    print("Ive only ever heard stories of the temples but they havent been found in nearly 200 years.")
    print("you are following the map that is on the scroll when suddenly you spot a 25 ft anocanda snake, do you:")
    print("1. jump off your horse draw your sword and fight the snake.")                       # pick 1 to jump off your horse and fight the 25ft snake
    print("2. ride as fast as you can and jump over the snake.")                               # pick 2 to ride as fast as you can over the snake, risky but maybe effective
    choice = input("- ")
    if choice == "1":
        draw_sword()
    elif choice == "2":
        jump()
    else:
        print("wrong choice, try again knight.")
        tell_name()

def fake_name(): 
    print("you tell the man a your name is sir buttonsworth.")                              # you give the mystrious old man a fake name to throw him off
    print("the old name seems to know who you are and what youre here to do.")
    print("the man sees right through the lie and pull out his knife.")
    print("before you have time to react the old man stabs you and you fall off your horse and die.")
    print("this is where the story ends, please try the other endings.")                    # first ending, of our story

def ditch_horse():
    print("you decide to ditch the horse and jump into the river.")                         #you ditched the horse and jumped into the creature infested water, risky
    print("the river is cold and muddy, you go as fast as you can to get to the other side.")
    print("you can see aligators around you.")
    print("three other knights are getting off their horses to come get you.")
    print("before you have time to draw your sword a aligtor bites you and rips you in half...")
    print("this is where the story ends, please try the other endings.")                    # second ending, of our story

def woodlands():
    print("you decided to stay on the horse and enter the woodlands of butterland.")        # you are staying on your horse, and entering the woodlands of butterland, the woodlands are known for thier inlarged species of animals
    print("you know there is a village up the way for a hideout.")
    print("the only problem is the feirce speicies that live in the butterland woodlands.")
    print("you are jumping over broken down tress with yuor horse trying to get away from the king.")
    print("the next thing you know an anceint gorilla comes swooping down from the trees above.")
    print("The monkey stands 8 ft tall and weighs upwards of 400 pounds.")
    print("thers a few options, do you:")
    print("1. turn around and fight the seven other knights.")                              # pick 1 to turn around and fight the 7 knights that have been following you
    print("2. stand your ground and try to injure the gorilla and get away.")               # pick 2 to to try to kill or injure the gorilla to get out of the area
    choice = input("- ")
    if choice == "1":
        turn_around()
    elif choice == "2":
        fight_gorilla()
    else:
        print("wrong choice, try again knight.")
        woodlands()

def draw_sword():
    print("you decide to jump off the horse to kill the anocanda")                          # you jump off your horse to try and kill the very powerful snake
    print("the snake attaks first and tries to bite you, you dodge the attak.")
    print("the snake whips his tail which hits us.")
    print("Just as the snakes trying to wrap us up we grab our sword as fast as we can.")
    print("We are almost fully wrapped up by the snake when we pierce right through the belly.")
    print("The snake lays there slain, you did it knight you defeated the anocanda.")
    print("you pull the scroll out and realize we are only about 5 miles from the location")
    print("Its starting to turn night and the jungle is definitly not safe in the dark, do you:")
    print("1. try to make it 5 miles before nightfall.")                                    # pick 1 to try to make it to the temples before nightfall, so we dont encounter any creatures
    print("2. make a camp in the woods and risk being attaked in the night.")               # pick 2 and risk being killed in the night, ending this part of the story
    choice = input("- ")
    if choice == "1":
        make_it()
    elif choice == "2":
        make_camp()
    else:
        print("wrong choice, try again knight.")
        draw_sword()

def jump():
    print("you decide to try to jump over the 25 ft anoconda.")                            # You decide its a better idea to jump over the snake than try to fight it
    print("with a running start with your horse you go as fast as you can.")
    print("you get near the snake and jump as high as youve ever jumped on a horse.")
    print("just as you think you made it saftley the snake curls around and swallows you and your horse.")
    print("this is where the story ends, please try the other endings.")                    # you die so this part of the story ends

def turn_around():
    print("you decide to turn around and fight the seven knights.")                        # you are gonna try to turn around and fight the highly skilled knights
    print("the knights are very skilled fighters and will do anything the king asks of them.")
    print("as a fleeing knight its going to be hard to fight against the knights")
    print("you draw your sword and run toward the knights.")
    print("you fight for what seems hours. A secret knight hidden in the bushes comes from behind and perices through you.")
    print("this is where the story ends, please try the other endings.")                       # you die so this part of the story ends

def fight_gorilla():
    print("you decide to fight the big gorilla because the knights are very hard to beat 7 on 1")                                                           # you are gonna try to fight the big gorilla because the knights are very hard to fight
    print("The gorilla has one weakness his chest, hitting the gorilla in the chest is the easiest way to critically hitting him.")
    print("you draw your sword and rush toward the big amimal, you start running around him to get a good shot of his chest.")
    print("the gorilla attaks and kills the seven knights chasing after you. while he is distracted you stay waiting and when you have the prefect shot.")
    print("you hit the gorilla right in the chest and he instantly falls, you must make a run for it, do you:")
    print("1. head for the village we talked about earlier in the story.")                                              # pick 1 and head for the village up the way, to get away
    print("2. flee to the next county that is heavily populated and easy to hide.")                                     # pick 2 to flee to the next county, this county is very populated easy place to hide
    choice = input("- ")
    if choice == "1":
        village()
    elif choice == "2":
        next_county()
    else:
        print("wrong choice, try again knight.")
        fight_gorilla()

def make_it():
    print("you decide its a better choice to try to make it to the temples instead of making a camp.")                  # you are gonna try to make it to the temple before nightfall, becasue their are a lot of creatures in the woods at night
    print("after a five mile horse ride you make it to the temples just before nightfall.")
    print("You hear a mysterious noise coming from one of the temples, do you:")
    print("1. Go explore the temple and find out whats making the noise.")                                              # pick 1 to go inside the temple to see whats making the nosie
    print("2. stay outside till morning have the chance of getting woken up by something mysterious in the night.")     # pick 2 to stay outside till morning becasue we dont know what inside
    choice = input("- ")
    if choice == "1":
        explore()
    elif choice == "2":
        outside()
    else:
        print("wrong choice, try again knight.")
        make_it()

def make_camp():
    print("you decide its better to stay here the night and make a camp because its getting dark.")                     # you stay and make a camp because its a hard travel to make before the sun goes down
    print("you set up camp and decide its time to go to bed.")
    print("while you are sleeping a nightly creature wakes you up a nasty jungle worm.")
    print("The nasty jungle worm have teeth six times sharper than a great white shark.")
    print("before you have time to wake up and fight the creature, the worm kills you.")
    print("this is where the story ends, please try the other endings.")                                                # you die this part of the story ends

def village():
    print("you decide to head for the quiet village.")                                                                  # you decide to head for the queit viallge that isnt as highly populated
    print(" you make it to the village and stop at the el royal saloon, after all that fighting you're very hungry.")
    print("there is a mysterious man sitting in the corner, its a weird old man with a cane.")
    print("the man asks what your name is and you give him a fake name becasue you expect there to be a bounty on you.")
    print("the old man sees through your lies and stabs you because we know too much informantion on the temples of bladesville, he takes you back to the king and claims his prize money.")
    print("this is where the story ends, please try the other endings.")                                                # you get caught, game over

def next_county():
    print("you decide its safer to go to the next county over because we most likley have a bounty on us.")             # if you assualt a king, you have a very high bounty dead or alive
    print("you make it to the other very populated county.")
    print("you see two diffrent buildings that peak your intrests, do you:")
    print("1. go into the diner hall on the corner of the street.")                                                     # pick 1 to walk to the dinner hall ot get a bite to eat
    print("2. go into the bed hall and rent out a room for the night.")                                                 # pick 2 to go to the bedhall and rent out a room, and rest
    choice = input("- ")
    if choice == "1":
        diner_hall()
    elif choice == "2":
        bed_hall()
    else:
        print("wrong choice, try again knight.")
        next_county

def explore():
    print("you decided to go inside the temple to find out whats making the strange noises.")                           # walk inside the temple and see what making the weird noises
    print("you keep hearing the strange noise and you notice its coming from behind a big metal door.")
    print("you go to the doors and try to open it with all your might but the door is over 5k pounds.")
    print("these temples are very heavily boobey trapped, theres most likley a hidden way into the room.")
    print("you take a step toward the wall and relize one of the concrete slabbed walls look diffrent than the others.")
    print("you put your hand into the concrete peice and the door latch unlocks and swings open.")
    print("before you can react a massive spider comes out of room spitting acid evrywhere.")
    print("you draw your sword and try to fend off the spider, do you:")
    print("1. try your hardest to defeat the spider, and then go look and see whats in the mysterious room.")           # pick 1 to fight the spider, to retreive the treasure
    print("2. run for the room to see if we can find the lost treasure.")                                               # pick 2 to run stright to the room, avoid the spider to get the treasure
    choice = input("- ")
    if choice == "1":
        fight_spider()
    elif choice == "2":
        Room()
    else:
        print("wrong choice, try again knight.")
        explore()

def outside():
    print("you decide its safer to stay outside because the temples are very dangerous.")                               # you are staying outside for the night to avoid fighting anything but sleepimg outisde has risks
    print("In the middle of the night you are woken up by a strange noise.")
    print("you wake up and relize we are 150 ft abov the ground in a giant posinous birds nest.")
    print("you scream and are isntantlly killed by the posinous venom.")
    print("this is where the story ends, please try the other endings.")                                                # you die this part of the story ends

def diner_hall():
    print("you decide to go to the diner hall because you get hungry after a day of travel.")                           # you decide to get a bite to eat at the diner hall, becasue travling makes you hungry
    print("you sit down order a drink and some food and brainstorm a plan.")
    print("The king has been a dictator for the butterlands so you think to take him out.")
    print("Tommorrow is the day the king comes and visits the town we are in.")
    print("you have a couple choices to choose from, do you:")
    print("1. take out the king tommorrow to stop the dictatorship.")                                                   # pick 1 to take out the king tommorrow and stop the dictatorship set by the king
    print("2. live out the rest of your days as a blacksmith.")
    choice = input("- ")
    if choice == "1":
        take_out()
    elif choice == "2":
        blacksmith()
    else:
        print("wrong choice, try again knight.")
        diner_hall()

def bed_hall():
    print("you decide to get a room at the bed hall because its tiring after a day of travel/fleeing.")                                     # you get a room at the bedhall the bedhall is a very old building
    print("you go inside and get a room the man at the counter is a bridge troll he hands you your key and you go inside your room.")
    print("you sit and think that the king will do nothing until we are dead so for the greater good we must take our own life.")
    print("This is where the story ends, please try the other endings.")                                                                    # you die this part of the story ends 

def fight_spider():
    print("you decide to fight the massive acid spitting spider.")                                                                          # you decide to fight the spider, the spider is very large but he has disadvantages
    print("as a knight we know where the critial hitting points of most creatures are, the spiders critial spot is its web spinner so take that out and the spider will be deafted.")
    print("you run around the spider to hit its web spinner the spider spits acid and it almost hits us.")
    print("you stab the spider in the spinner and he vanishes into dust, 'was it just a guardian spirit.")
    print("you walk into the room with the massive room and its filled with gold, mountains of gold but in the middle of the room you see something.")
    print("its a massive dimond around 50 karats. you grab the dimond and the building starts to break. walls crumbling ceilings rumbling.")
    print("you run as fast as you can outside, you jump on your horse and head back for the castle.")
    print("you make it back to the palace and go to the king, you pull out the dimond and the king is very happy becasue the dimond was his great granfathers greatest discovery and its finally back into the castle where it belongs.")
    print("this is where the story ends, please try the other endings.")                                                                    # this is the true ending to one of the stories

def Room():
    print("you decide to run into the room and find a room filled with gold and a great big dimond in the center of the room.")             # you run right into the room istead of fighting the spider
    print("you start bagging up the coins and run to get the dimond, you grab the dimond and the spider closes the big door trapping you inside.")
    print("but becasue you picked the dimond up the entire room starts getting destoryed, amd you have no way out.")
    print("this is where the story ends, please try the other endings.")                                                                    # you die this part of the story ends

def take_out():
    print("You decide to take out the king of butterland.")                                                                                 # you are going to kill the king because he is a bad man that evryone thinks is the greatest person ever, thats just not true
    print("we sleep the night and get a nice nights rest before it all ends.")
    print("you stnad on the side of the street and you see the king is in town.")
    print("the king is set to be eating at the royale de palace, a very nice resturant.")
    print("The king goes into the resturant, and you sneak into his buggy.")
    print("the king comes out of the resturant gets in the buggy and you put a knife to his throat, the king pleds for his life but you know what must be done.")
    print("you take the kings life and the dictator ship ends in butterland")
    print("this is where the story ends,please try the other endings.")                                                                     # this is the true ending of one of the stories

def blacksmith():
    print("you decide to spend the remainding years of your life as a blacksmith.")                                                         # you decide to live the rest of your life as a blacksmith
    print("you go into the local blacksmithing shop and ask for a job.")
    print("you stay working their until you die of maleria 30 years later.")
    print("this is where the story ends, please try the other endings.")                                                                    # you die of a disease, this is also a true ending

start_adventure()




