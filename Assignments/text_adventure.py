def start():   # function to start
    st = input("congrats! you have been given the opertunity to become a super soldier. do you accept? >") #y or n Q for first split
    ST = st.lower #makes st awnser lower case to fit if statment

    if ST == "yes":
        procide() # the continue path

    elif ST == "no":
        walk_away() # the first ending

    else: # solve errors
        print("awnser yes or no, try again.")
        start() 

def walk_away(): # first ending where you walk away
    print("you say no and walk away.")
    print("status: Chicken") #status of your ending
    start_over() #function to start over

def start_over():
    an = input("would you like to startover? >")
    AN = an.lower

    if AN == "yes":
        start()

    elif AN == "no":
        print("ok")
        start_over()
    
    else:
        print("yes or no, try again")
        start_over()

def procide(): #continues the story
    print("")

start()