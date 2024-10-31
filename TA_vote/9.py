



def start_game(): # intro

    print("Welcome to the Coastedge Police Station!")
    print("You are a rookie officer assigned to investigate strange occurrences.")
    first_choice()



def first_choice(): #option

    print("\nYou enter the dark and eerie police station.")

    print("1: Check the evidence room.")

    print("2: Investigate the holding cells.")

    print("3: Go to the chief's office.")

    

    choice = input("What do you want to do? (1/2/3): ")

    

    if choice == '1': 

        evidence_room()

    elif choice == '2':

        holding_cells()

    elif choice == '3':

        chiefs_office()

    else:

        print("Invalid choice. Please choose again.")

        first_choice()



def evidence_room():

    print("\nThe evidence room is cold and filled with dust.")

    print("You see a mysterious box glowing in the corner.")

    print("1: Open the box.")

    print("2: Leave the room.")

    

    choice = input("What do you want to do? (1/2): ")

    

    if choice == '1':

        ending_one()

    elif choice == '2':

        first_choice()

    else:

        print("Invalid choice. Please choose again.")

        evidence_room()



def holding_cells():

    print("\nThe holding cells are dark and filled with whispers who loves to haunt and make fun of people.")

    print("You hear a voice calling your name.")

    print("1: Investigate the voice.")

    print("2: Ignore it and leave.")

    

    choice = input("What do you want to do? (1/2): ")

    

    if choice == '1':

        ending_two()

    elif choice == '2':

        first_choice()

    else:

        print("Invalid choice. Please choose again.")

        holding_cells()



def chiefs_office():

    print("\nThe chief's office is covered in shadows and some stinky green slime.")

    print("You find a file labeled 'Case 666'.")

    print("1: Read the file.")

    print("2: Destroy the file.")

    

    choice = input("What do you want to do? (1/2): ")

    

    if choice == '1':

        ending_three()

    elif choice == '2':

        ending_four()

    else:

        print("Invalid choice. Please choose again.")

        chiefs_office()



def ending_one(): # the differnt ending for whats goes on  

    print("It claims your soul, and you become part of the haunt.")

    print("Ending: You are now a ghost haunting the station forever.")



def ending_two():  # the differnt ending for whats goes on 

    print("\nYou follow the voice and discover a lost inmate's spirit.")

    print("It helps you escape, but you are cursed to remember the station's horrors.")

    print("Ending: You leave, but the haunting memories never fade .")



def ending_three():# the differnt ending for whats goes on 

    print("\nThe file reveals dark secrets about the station's past.")

    print("As you read, you unleash the spirits of the wrongfully imprisoned.")

    print("Ending: The spirits claim the station, and you vanish without a trace but letting the spirit take over your body and watching it leave the police station  .")



def ending_four(): # the differnt ending for whats goes on 

    print("\nYou destroy the file, but the spirits are angered.")

    print("They haunt you relentlessly until you go mad.")

    print("Ending: You lose your mind, wandering the station as a broken soul .")



def ending_five(): # the differnt ending for whats goes on 

    print("\nYou manage to leave the station, but a shadow follows you home.")

    print("You realize the haunt has followed you into your life.")

    print("Ending: The horror continues as you face it every night.")



# Start the game

start_game()

