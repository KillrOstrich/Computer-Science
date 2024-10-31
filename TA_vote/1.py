money = 20                  # Don't spend it all in one place
fries = False               # not reccommended for kids or anyone but can be used to convince others
ba_da_blaser = False        # comes in handy for tight situations\
ron_anger = False           # Ron is angry
family_love = False         # something you do not know yet
rat = False                 # don't rat out your friends
evil = False                # why are you bad



def begaining():
    print("Your name is Johnny Salami and your a faceless grunt in the mafia, and you only have $20 to your name but things change and your gonna change em' for better or for worse, but above all you'll become a made man")     
#Endings    Made man(rich),  Made man(family), Maid man, Made(game over), Made rat, Made man(Leader), made turncoat, unmade man, man

    print("\nYour making your way down the street when you suddenly spot that weasel Ron Mcdon peddling his signiture fries on your turf what do you do?\n")
    print("1. Confront Ron Mcdon")                 # Rich / Leader / turncoat / Game Over
    print("2. go to the police and tattle")         # Rat / family / Game Over
    print("3. buy some of his Fries(-$10)")          # Maid / Leader / turncoat / unmaid man
    print("4. Leave, it's none of your business")   # Family / Rich
    

def ron():
    ron_choice = input(">")
    if ron_choice == "1":         # confrontation

        print("\nyou walk up to Ron Mcdon and question him on why he's selling on your turf. Ron Mcdon says that your family doesn't need to know about his little side hussle and offers you a little incentive")
        print("1. Take the money and stay silent (+$15)")                           # Turncoat / Rich
        print("2. 'Whack' Ron and take his stuff (+$25 and Ron Mcdon 'Fries')")     # Leader / Rich
        print("3. Do what is responsible and call the local authorities")           # Game Over
        print("4. Break his legs")                                                  # Leader / Family

        
    bribe_choice = input(">")   
    if bribe_choice == "1":                         # Ron route
        
        print("you take the bribe and walk away")   # Rich route
        global money
        money = money + 15
        print("$" + str(money))
                
    elif bribe_choice == "2": 
                                                                                                                  
        print("\nYou 'whack' Ron Mcdon in the middle of the street and take his loot you get $25, his 'fries' and his ba-da-blaser")    # very evil, grab da blaster, grab a da fries, make some money
        global ba_da_blaser
        global evil
        evil = True
        ba_da_blaser = True
        global fries
        fries = True
        money = money + 25
        print("$" + str(money))
    
    elif bribe_choice == "3":            # GAME OVER path
            print("\nYou pull out your phone and dial 9-1-1 in front of Ron Mcdon, but before you can make the call he pulls out his Ba-Da-Blaster and he completly disitigrates you.\nGAME OVER: YOU WERE MADE" + restart)
    
    
    elif bribe_choice == "4":  # You angered Mcdon and you broke his legs
                                                                                             
        print("\nYou teach Ron Mcdon a lesson and take his money and his 'fries' (Ron Mcdon will remember that")
        global ron_anger
        ron_anger = True
        money = money + 25
        print("$" + str(money))
    
    
    elif ron_choice == "2":                         # Turncoat route
       
        print("you run to the police and you tattle on Ron Mcdon and how he's selling his fries on Drury lane. The police question you a bit further what do you tell them")
        print("1. Tell them everything")           # GAME OVER
        print("2. Tell them about Ron Mcdon")      # turncoat / family / rat
        print("3. negotiate")                      # Made rat
        print("4. RUN AWAY!!!!!!")  # GAME OVER
        police = input("\n>")

        if police == "1":                   # Your a terrible rat
             print("you tell the police everything you are arrested and assassinated by Don Bozo with a suprise airhorn before you make it to trial")

        elif police == "2":                 # Double agent
            print("you rat on Ron Mcdon and they take him down and slip you a little money to keep you around")
            global rat
            rat = True
            money = money + 20
            print("$" + str(money))     # Concatnation

        elif police == "3":                 # You got the chops to be a rat
             
             print("you tell them you'll give up the info on all the dealings related to the mob, but only if you get a nice house and a heap of cash\n")
             print("you are taken away into witness protection and shipped off to Canada\n")
             print("you live the rest of your days riding moose and eating syrup in a nice house while you slowly freeze to death in a mansion surrounded by the locals you paid to be here")
             print("\nYOU ARE A RAT")        
        
        else:
             print("invalid input")
             ron()
    
    
    elif ron_choice == "3":                 # getting some 'fries'

    

        fry = input("\nYou buy fries from Ron Mcdon. Would you like to try some?\n")
        print("1. try the 'fries'")                 # DON'T EAT THE FRIES
        print("2. save the 'fries' for later")      # Rich / Leader

        fry = input(">")

        if fry == "1":          # WHY DID YOU EAT THE 'FRIES'

            print("As you are possessed by curiosity to see the hype around Ron Mcdon's 'fries' you eat one 'fry'")
            print("as soon as the 'fry' enters your mouth you feel yourself getting lighter, but you start to feel a bit strange")
            print("all of your hair is falling out and your teeth come alive and start pulling themselves out and attack you")
            print("You are overcome with fear and panic as you are now drowning in a bowl of spaghetti...")
            
            print("\n\nreality kicks in and you are at the feet of the head of the mafia The Muffin Man himself what do you do?")
            
            print("1. Tell him your very very sorry and it won't happen again")     # MAID MAN
            print("2. Offer The Muffin Man himself a 'fry'")                        # GAME OVER
            print("3. Eat another 'fry'")                                           # UNMADE MAN
            
            muffin = input(">")

            if muffin == "1":
                 print("As you tell The Muffin Man himself it won't happen again he puts his hand on your shoulder and puts you in a new line of work...\n\nMAID MAN ending\nyou now work a legitamte job and earn far more then your worth $10/per hour")
                 

                 
            elif muffin == "2":
                 print("You offer The Muffin Man himself a 'fry' and he takes it and throws it into the water, he then places you in muffin shaped concrete shoes and")
                 print("pushes you into what you used to think was water, but was actually an entire lakes worth of muffin batter\n\nGAME OVER")
                

            elif muffin == "3":
                 print("You eat another 'fry' in front of The Muffin Man himself and he's so dumfounded by you he just lets you go...")
                 print("You have become addicted to Ron Mcdons 'fries' and and you drown in a plate of Spaghetti thining you were on 'fries'")
            
            else:
                print("invalid input")
                ron()
            
        elif fry == "2":        # You have two braincells at least
             print("you do the rational thing and save the 'fries'")
             fries = True
             money = money - 10
             print("$" + str(money))

        else:
            print("invalid input")
            ron()

    elif ron_choice == "4":             # confrontation is scary
        print("You decide not to get involved it won't affect you too much")

    
    else:
        print("invalid input")
        ron()
def party():

    print("You are walking down the street when you see a party going what do you do\n")    # Life of the party
    print("1. I'm not as young as I used to be")   # be boring / man 
    print("2. I'll go but i'll go to the one across the street looks a lot more tame")
    print("3. LET'S PARTYYYYYYY!!!!!!!!")

    party_time = input(">")
    if party_time == "1":      # Boring
         print("You leave the party and go home to rest")

    elif party_time == "2":    # Embaressing

        print("you go to the party across the street and you tear up the dance floor\n but then you realize that you are a kids birthday party and everyone's staring at you")
        
        if rat == True:
            print("\nThe clown calls you up for a magic trick and the crowd thinks your his assistant\nyou go up and he pulls out a curtain and beneth the curtain he turns you into a mouse\n\nGAME OVER")
        
        elif rat == False:
            print("\n you start walking away awkwardly as the music continues to play and parents are whispering")

    elif party_time == "3":    # Party time
        print("You go to the party and you start to tear up the dance floor\n as you dance your heart out a lady walks up to you and asks you name, what do you say")
        print("1. Name's Johnny how do you do")                 # Be a decent human being
        print("2. 'continue to annhilate the dance floor'")     # Woman come and go dance is forever/ Game over
        print("3. HilOoo JoUrnY hEr nICe Tour MeT yOU")         # Social interaction is hard

        woman = input(">")
        if woman == "1":
            print("You hit it off as she asks you on a date later, do you accept")    #Rom Com
            print("1. Yes")                 # Family
            print("2. No")                  # game over
            print("3. Your not my type")    # let me down gently 
    
            date = input(">")
            if date == "1":
                print("You have a great date and fall in love after beating up a seagull that tried stealing her Baconator")            # Family gotten
                global family_love
                family_love = True
            
            elif date == "2":
                print("She flips out and calls her father 'The Muffin Man himself' and he gives you a batter bath\n\nGAME OVER")        # Let her down gently
            
            elif date == "3":
                 print("She appreciates you letting her down gently and leaves peacefully")           # good


        elif woman == "2":
             print("You dance so hard your body ignites and you go out like a super star on the dance floor")

        elif woman == "3":
            print("You scare her off as you do your best impression of a lunatic...\n\nshe was not impressed")
        
        else:
            print("invalid input")
            party()


def mugging():

    global ba_da_blaser
    global fries
    global money
    print("As you walk down the street you are stopped by a couple of hooligans what do you do")

    print("1. give them all your money")
    print("2. RUN AWAYYYYYYYYYYY!!!!!")
    print("3. beat up some teenagers")
    
    shakedown = input(">")
    if shakedown == "1":
        print("you don't want any trouble and give all your money to the teens")
        money = 0

    elif shakedown == "2":
        print("you run away from the angry teens, but your not as spry as you used to be and you fall\nyou are beat up and your money is taken away")
        ba_da_blaser == False
        fries == False
        money = 0
    
    elif shakedown =="3":
        print("you prepare to fight the teens and take everything they got on em")
        if ba_da_blaser == True:
            print("would you like to use the ba da blaster to defeat them")
            print("1. Yes")
            print("2. No")

            destroy = input(">")
            if destroy == "1":
                 print("You win your encounter with the muggers, but you disintigrated all of their belongings")
                 
                 global evil
                 evil = True
            elif destroy == "2":
                 print("you decide to fight the teens without your handy weapon and you put up a good fight, but they had a ballon knife\n\nGAME OVER")
                 restart            

            else:
                print("invalid input")
                mugging()

    else:
        print("invalid input")
        mugging()

def broken_vase():


    print("You get a call from Mr. Gingy to The Muffin Man himself's office\non the way to his office you break a vase what do you do")
    
    print("1. RUUUUUNNNNN AAAWWWWAAYYYYYYY!!!!!!")
    print("2. Sweep it under the rug")
    print("3. Plant evidence that RonMcdon did it")
    print("4. Do nothing")
    vase = input(">")
    
    if vase == "1":
        print("You run... you don't stop running... your never gonna stop running... you run for so long that your legs give out... your found in Canada a year later\n\nGAME OVER")
        restart
    elif vase == "2":
        print("you sweep the entire vase under the rug...\n as The Muffin Man himself is comming in you see him polishing his designer glasses and he trips on the massive lump in the rug...\n The Muffin Man himself's funeral was held later that month")
        print("You gain so much noteriety from whacking The Muffin man himself that all the don's name you as the new leader of the Drury Lane Crime Syndicate\n\nYOU ARE A MADE MAN")
    elif vase == "3":
        print("You paint the side of the vase red and yellow with a few dabs of white to frame Mcdon")
        global ron_anger
        ron_anger == True
    elif vase == "4":
         print("The Muffin Man himself walks in and finds you broke his vase, you won't be recieving another paycheck for a little bit")

    else:
        print("invalid input")
        broken_vase()

def rons_revenge():
     
     global ron_anger
     if ron_anger == True:
        print("Ron runs up to you with a squad of grimmace and pulls out his signiture McStick and looks really really mad\nWhat do you do")
        print("1. Negotiate")
        print("2. Run")
        print("3. FIIIGGGHHHTTTTT")
        
        ron_fight = input(">")
        
        if ron_fight == "1":
             print("As you try to explain how this is all a big mistake you are hit by the McStick and never Mc wake up again\n\nGAME OVER")
             restart
        
        elif ron_fight == "2":
             print("You run from Mcdon and his goons, but your quickly halted a piano falling on your head\n\nGAME OVER")
        
        elif ron_fight == "3":
            print("You stand to fight Mcdon and his goons when multiple piano's fall out of the sky and crush them")
        
        else:
            print("invalid input")
            rons_revenge()
def treasure():
     global ron_anger
     if ron_anger == True:
        print("you defeated Ron Mcdon and you find in his back pocket a map of all of his depots for his fries adn the code for his safe waht do you do")
        print("1. Take all of the money and 'fries'")
        print("2. donate everything to the local orphanage")
        print("3. become the head of Ron's operations")
        
        bounty = input(">")
        if bounty == "1":
             print("you take all of ron's stuff and slowly work your way out of the buisness, you reture at an early 55 years old on an unamed beach in California\n\nYOU ARE A MADE MAN")
        elif bounty == "2":
             print("You donate everything to the orphange and while they were grateful for the money they looked a little puzzled when you gave them all of Ron Mcdon's 'fries'")
        elif bounty == "3":
             print("you take over all of Mcdon's territory and all of his possestions, but sadly a piano fell on your head after you became leader\n\nGAME OVER")
        else:
            print("invalid input")
            treasure()

def boring():

    global money                
    global fries              
    global ba_da_blaser     
    global ron_anger    
    global family_love   
    global rat      
    global evil
    if money == 20 and fries == False  and ba_da_blaser == False   and ron_anger == False and family_love == False and rat == False and evil == False:
         print("CONGRADULATIONS YOU ACOMPLISHED ABSOLUTLEY NOTHING, YOU WERE GIVEN EVERY OPPERTUNITY TO DO SOMETHING EVEN MIDLY INTERESTING AND YOU CHOSE THE MOST BORING PATH EVERYTIME\n\nYOU ARE A MAN")              
                  
def traitor():
     
     global rat
     if rat == True:
           print("the police get in contact with you again, this time they want you to bring down the whole opperation\nwhat do you do")    

           print("1. say no")

           print("2. Agree")

           recruit = input(">")
           
           if recruit == "1":
                print("you say no and they beg you to reconsider, but you do not and a piano falls on your head\n\nGAME OVER \n you only had one real option")
           
           elif recruit == "2":
                print("you agree and rat out the whole family, but Don Bozo blocks your path\n he holds up a massive ballon hammerand prepares to strike, what do you do")
                print("1. FIIIGGGHHHHTTTT")
                print("2. FLLYYYY AAWWWAYYYYYYY")
                print("3. pop the ballon")
                
                bozo = input(">")
                if bozo == "1":
                    print("As you go to fight Bozo you are struck down by a clown car, full of giant clowns, 45 clowns step out and destroy you\n\nGAME OVER")
                elif bozo == "2":
                     print("you think really hard you can fly away and you start flapping your arms and you get a little bit off the ground...\nDon Bozo then crushes you with his massive hammer")
                elif bozo == "3":
                     print("you find a sharp enough object and chuck it at don Bozo's hammer it pops and sends don Bozo flying along with the clown car\nYou managed to escape the clowns and you rat on all of the mafia and you get shipped off to Norway")
                     print("you live in peace and luxery for the rest of your life\n\n YOU ARE A MADE RAT")
                else:
                    print("invalid input")
                    traitor()
     else:
       print("invalid input")
       traitor()             
     


def restart():
   again = input(" would you like to try again\n>")
   if again == "yes":
           begaining()
   elif again == "no":
           print("GAME OVER")
   else:
           print("invalid input")
        
begaining()
ron()
party()
mugging()
broken_vase()
rons_revenge()
treasure()
boring()
traitor()