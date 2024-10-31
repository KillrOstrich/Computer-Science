#Create a text adventure game about the Bread-stealing Bandit.
#You are a detective that has beens sent to catch him. YOU MUST HAVE AT LEAST 20 ENCOUNTERS INSIDE OF FUNCTIONS!
#If the player fails / gets a bad ending, put a bread pun in there.
#(The Bread-stealing Bandit bakes his victims into bread.)
#List of bread puns:

#You got turned into toast. Butter luck next time!
#You got turned into bread... c'mon, try again! You can't let him baguette away with this!
#You got turned into bread... quit loafing around! Try again.
#You let your guard down... you're toast. Try again!
#Try again! Bready, set, go!

#Endings:

#Good ending
#Bad ending
#Elden Ring ending
#Fired ending
#Failure ending
#Death ending(s)

#1
def BreadySetGo():
    print("'Detective! People have been going missing, and a bunch of bakeries have been robbed of all their bread! All signs point towards the Bread-stealing Bandit... He's finally returned. We need you to find him and arrest him! Are you up to the task?'")
    print("1. Yes! Justice will be served!\n")
    print("2. Pfft, no way! Skill issue. Deal with it yourself.\n")

    choice = input(">")

    if choice == "1":
        thestreet()
    elif choice == "2":
        print("'What a shame... we were told you were the best. Clearly we were mistaken.' GAME OVER. You got fired, and your reputation was destroyed. Try again!")
        BreadySetGo()
    else:
        print("Invalid response. Please try again.")
        BreadySetGo()

#2
def thestreet():
    print("You walk out onto the street and see a sketchy guy walking towards you. He says he will help you if you give him some money. Do you:")
    print("1. Accept his offer and give him $200.\n")
    print("2. Say 'no thank you,' and walk away.\n")

    choice = input(">")
    if choice == "1":
        downtown()

    elif choice == "2":
        print("'What a shame... JUMP 'EM, BOYS!!!' Suddenly, you see a bunch of people running at you. They steal everything you have and then run off... You got jumped. Game over. Try again. Bready, set, go!")
        BreadySetGo()

    else:
        print("Invalid response. Please try again.")
        thestreet()



#3
def downtown():
    print("You give the shady-looking man $200. He chuckles to himself. 'Thanks, man...' and then he walks away. It appears you've been scammed... that's okay, though. The show must go on!")
    print("You can either chase the theif to try and get your money back, or you can stop for some lunch. What do you choose?:")
    print("1. Let's stop for some lunch. I'm hungry!\n")
    print("2. I'm not gonna let him baguette away with this!\n")

    choice = input(">")
    if choice == "1":
        Eavesdropping()
    elif choice == "2":
        print("You go after the theif, but he's long gone. You decide to walk further downtown to try to get more answers.")
        Eavesdropping()
    else:
        print("Invalid response. Please try again.")
        downtown()

#4
def Eavesdropping():
    print("You sit down at an outside table and wait for someone to take your order. You then overhear two teens talking about the Bread-stealing Bandit. Do you:")
    print("1. Ignore them. They're just a couple of stupid teens gossiping. Darn whippersnappers!\n")
    print("2. Walk up to them and ask a few questions. Any information is useful!\n")

    choice = input(">")
    if choice == "1":
        print("Wow, some detective you are. Suddenly, you see a bakery down the street that was closed. The bakery is usually open at this time. You decide to go and investigate.")
        breadstore()
    elif choice == "2":
        print("The teens tell you that the Bandit had apparently beem spotted in the area a few hours go. According to them, he had robbed another bakery down the street. You decide to go to the bakery to investigate.")
        breadstore()
    else:
        print("Invalid response. Please try again.")
        Eavesdropping()

def breadstore():
    print("You enter the bakery. There is a man at the counter with a terrified and shocked expression. You ask him what happened. 'Didn't you hear?' He said, 'The Bread-stealing bandit robbed my store. Not only that, but he turns his victims into bread! I'm Lucky to be alive!' Do you:")
    print("1. Attempt to comfort the man\n")
    print("2. Call the man a wimp\n")

    choice = input(">")
    if choice == "1":
        print("You get the man to calm down and then ask him some questions. He says that even though the bandit's face was covered and he was wearing all black, he could still see his piercing yellow eyes that seemed to stare into his soul. (YES, the bandit's eyes are yellow. Just go with it.)")
        uglyhat()
    elif choice == "2":
        print("You call the man a wimp and tell him to man up. He gets mad and throws a bread knife at you. He yells at you to leave the store and never come back. Congrats, you dumb detective! Now you didn't get the answers you need, and the Bandit was never caught. Game over. Try again.")
        BreadySetGo()
    else:
        print("Invalid response. Please try again.")
        breadstore()

def uglyhat():
    print("You ask around to see if anyone had seen someone with yellow eyes. A lady tells you that she saw some weirdo in the mirror store wearing the most hideous had known to man and admiring his reflection. She couldn't really see his face, but, but she did notice his strange yellow eyes. Do you:")
    print("1. Head over to the hat store down the street\n")
    print("2. Go to the mirror store\n")

    choice = input(">")
    if choice == "1":
        print("You walk down the street to the hat store and ask the owner if anyone with yellow eyes had bought a hat recently. She says yes and explains that a guy with yellow eyes and dark brown hair had stopped by an hour or two ago.")
        checkingthecameras1()
    elif choice == "2":
        print("You go to the mirror store and ask the owner if they say a guy wearing an ugly hat came in. He says yes and explains that he had stopped by an hour or two ago.")
        checkingthecameras2()
    else:
        print("Invalid response. Please try again.")
        uglyhat()

def checkingthecameras1():
    print("You decide the check the cameras. You see the Bandit talking to someone and then handing him a slip of paper. You immediately recognize the guy recieving the paper as one of the Bandit's old associates. He had escaped from prison recently. When the two exit the store, you notice that the man had accidentally dropped the peice of paper. You go to the section of the store they had been in and find the peice of paper. You pick it up and realize that there is an address written on it. Do you:")
    print("1. Go straight to the address\n")
    print("2. Go outside to see if anyone had seen where they had went\n")

    choice = input(">")
    if choice == "1":
        print("You go to the address. However, the Bandit is waiting for you. The second you open the door, he jumps out and stabs you. You're toast. (Literally.) Try again!")
        BreadySetGo()
    elif choice == "2":
        print("You go outside and a mysterious woman walks up to you. She is wearing sunglasses and has long, blond hair. She tells you that she knows excactly where the Bandit is, and she can take you to him.")
        mysteriouslady()
    else:
        print("Invalid response. Please try again.")
        checkingthecameras1()

def checkingthecameras2():   #The mirror store version.
    print("You decide the check the cameras and see the bandit talking to someone, whom you immediately recognize as one of his old associates who had recently escaped from prison. The Bandit hands him a slip of paper. When they exit the store, you notice that the man had accidentally dropped the peice of paper. Do you:")
    print("1. Head to the section of the store where the paper was dropped\n")
    print("2. Continue watching the footage... you have an uneasy feeling...\n")

    choice = input(">")
    if choice == "1":
        print("When you go to the section of the store where you had seen the Bandit talking to the other man, you find the paper still lying on the ground and pick it up. You then notice the front doors slide open. The two were back. They must have realized that they had dropped the peice of paper. They notice you holding it. The Bandit's friend pulls out a gun and shoots you. Game over. Try again.")
        BreadySetGo()
    elif choice == "2":
        print("You decide to wait a little bit. Something tells you it's not safe to go back into the main area of the store. You continue watching the cameras. Suddenly, both the Bandit and his friend walk back into the store and begin to look for something. They return to the section of the store they had previously been in. They find the peice of paper and pick it up. Then they leave again. You walk out of the store to see where they went, when suddenly a mysterious woman approaches you. She has long, blond hair and is wearing sunglasses. She tells you that she knows where the Bandit went, and she can take you to him.")
        mysteriouslady()
    else:
        print("Invalid response. Try again.")
        checkingthecameras2()

def mysteriouslady():
    print("The woman waits for your response. Do you:")
    print("1. Agree to follow her\n")
    print("2. Tell her that she sounds like a man\n")

    choice = input(">")
    if choice == "1":
        print("You agree to follow the woman. The two of you arrive at a shady-looking house on the far side of town. You enter the house.")
        insidethehouse()
    elif choice == "2":
        print("You tell the woman that she sounds like a man. She gets offended and slaps you across the face. She then turns and walks away. You yell after her, 'Wait! I'm sorry!'. The woman sighs and turns around. 'Follow me,' she says. You follow her to the far side of town, and the two of yoy stop in front of a shady-looking house. 'He's in there,' the woman tells you. You enter the house.")
        insidethehouse()
    else:
        print("Invalid response. Please try again.")
        mysteriouslady()

def insidethehouse():
    print("Once you're in the house, you turn around, but the woman is gone. You decide to look for the Bandit. Do you:")
    print("1. Go into the living room\n")
    print("2. Go into the basement\n")

    choice = input(">")
    if choice == "1":
        print("You decide to check the living room first. You see some nerdy-looking guy playing Elden Ring on a PS5. You walk up to him and realize that it's Mr. Osowski. 'Mr. Osowski!? What are you doing here!?' you ask. 'The Bandit kidnapped me,' he replies. You give him a confused look. 'The door is right there. You can literally just get up and leave,' you say. 'But I'm busy playing Elden Ring!' He responds. You shake your head and then facepalm.")
        mrosowski()
    elif choice == "2":
        print("You go into the basement, however, the Bandit is waiting for you. You see the bodies of a bunch of dead bakers. You manage to escape the house, but that sight will haunt you for the rest of your life. You got the BAD ENDING. Try again!")
        BreadySetGo()
    else:
        print("Invalid response. Please try again.")
        insidethehouse()

def mrosowski():
    print("You think you might be able to convince Mr. Osowski to help you. Do you:")
    print("1. Tell him Elden Ring is trash and that Fortnite is better.\n")
    print("2. Tell Mr. Osowski that if he helps you find the Bandit, you will give him a special, secret, limited edition, unreleased sequel of Elden Ring.\n")

    choice = input(">")
    if choice == "1":
        print("Mr Osowski gasps dramatically. 'HOW DARE YOU!!!' He yells into the next room. 'BANDIT!!! There's a detective here! They're trying to arrest you! GET 'EM!!! Suddenly, the Bandit runs into the room with a knife. You panic. 'WAIT!!! I WAS JUST KIDDING!!! ELDEN RING IS GOATED!!!' The Bandit stops and looks over at Mr. Osowski. The next thing you know, you're all taking turns playing Elden Ring. The end? You got the ELDEN RING ending. Want to play again?")
        BreadySetGo()
    elif choice == "2":
        print("Mr. Osowski immediately agrees, and you decide to go to the basment. Before you can begin to walk down the stairs, however, Mr. Osowski warns you that the Bandit is waiting for them, and he has a knife. He offers to distract the Bandit with a smoke bomb. You nod, and the two of you enter the basement.")
        thebasement()
    else:
        print("invalid response. Please try again.")
        mrosowski()

def thebasement():
    print("Mr. Osowski agrees to help you. You decide to go into the basement. He warns you that the bandit is hiding down there with a knife, waiting for you. He offers to distract him. You walk to the bottom of the stairs. Mr. Osowski throws a smoke bomb into the basement. Nothing happens. Confused, you enter the basement. Suddenly, the blond woman from earlier walks down the stairs and startles you. Do you:")
    print("1. Panic and throw a donut at her\n")
    print("2. Panic and throw Mr. Osowski at her\n")

    choice = input(">")
    if choice == "1":
        print("The donut does absolutely nothing. The woman gets angry and stabs you. CONGRATS, you died! But don't worry, I'm gonna let you try again. It's the yeast I can do.")
        BreadySetGo()
    elif choice == "2":
        print("You pick up Mr. Osowski and throw him at her, causing her sunglasses and wig to fall off. Mr. Osowski is mad at you. 'YOU JERK!' He yells.")
        shesaman()

    else:
        print("Invalid response. Please try again.")
        thebasement()

def shesaman():
    print("That's when you notice the sunglasses and wig lying on the ground. The person looks up at you, and you realize that he has yellow eyes and dark brown hair. That's right, folks... SHE'S A MAN!!! *Insert dramatic music* Do you:")
    print("1. Attempt to fight the Bandit\n")
    print("2. Run for the door\n")

    choice = input(">")
    if choice == "1":
        print("You run towards the Bandit and immediately get stabbed in the stomach. Yeah... you never stood a chance. You're toast. (Literally.) Try again!")
        BreadySetGo()

    elif choice == "2":
        print("You and Mr. Osowski run for the door and back up the stairs into the living room. The door is boarded up. You hear the bandit running up the basement stairs behind you. 'Let's go upstairs. I'm sure there's something we can use to fight him,' you say. You see Mr. Osowski trying to drag the PS5 up the stairs. You let out an exasperated sigh and yell, 'WE DON'T HAVE TIME TO PLAY ELDEN RING!!!'. You grab his arm and run upstairs.")
        thediary()

    else:
        print("Invalid response. Please try again.")
        shesaman()

def thediary():
    print("You manage to baracade yourselves in a small office. You look and see a diary on the desk. Do you:")
    print("1. Read the diary.\n")
    print("2. Leave it be.\n")
#Choosing not to read the diary will not effect the outcome in any way, but the player will not know the villain's backstory unless they read it.
    choice = input(">")
    if choice == "1":
        print("You open up the diary and start to read about how the bandit used to attend baking school. You read that he was never very good at baking and got bullied for it by the other chefs. If fact, his cooking sucked SO BADLY that he got kicked out. He decided that if he didn't get a chance to be a good baker, then nobody else should, either. That's why he does what he does. Stealing bread, killing bakers and using their remains to bake make bread, etc. You decide to take the diary to use as evidence. Suddenly, you see a crowbar near the door.")
        escaping()
    
    elif choice == "2":
        print("You decide not to read the diary, however you still pick it up to see if you can use it as evidence. Something in the corner of the room catches your eye. You see a crowbar near the door.")
        escaping()
    else:
        print("Invalid response. Please try again.")
        thediary()

def escaping():
    print("You pick up the crowbar, quickly open the door, and hit the Bandit in the head. He passes out. You run back downstairs and into the living room. You use the crowbar to remove the planks from the door. You open it and wait for Mr. Osowski. Mr. Osowski pick up his PS5 and runs out the door with you. It's dark outside. You can choose to either run across the road for help or run into a creepy, shady-looking alleyway to hide. Do you:")
    print("1. Run across the road\n")
    print("2. Run into the creepy alleyway\n")

    choice = input(">")
    if choice == "1":
        print("You forgot to look both ways and got run over by a car... nice going. Try again!")
        BreadySetGo()
    elif choice == "2":
        print("You run into the alleyway and reach a dead end. You hear the Bandit yelling. He must have woken up. He turns the corner to find you and Mr. Osowski. You're getting ready to fight the Bandit when suddenly, you hear someone yell, 'JUMP 'EM, BOYS!!!' The shady-looking guy who you had given your money to all those hours ago was back, and he had his squad with him. They jumped the Bandit and beat him until he was unconscious. You handcuff the Bandit and call the station to come and take him away. The shady-looking guy, who turns out to be a guy named Sam, thanks you for the money you had given him and explained that it had really helped him and his guys out. After they leave, Mr. Osowski asks for his limited-edition copy of Elden Ring. You tell him that you lied to him, but still offer to buy him all the donuts he wants. He agrees, and the nightmare is finally over. You survived. You got the GOOD ENDING. Congrats! If you want, you can play again. Try to get all of the endings!")
        BreadySetGo()
    else:
        print("Invalid response. Please try again.")
        escaping()


BreadySetGo()


#Thanks for playing! I really hope you enjoyed the game! :)