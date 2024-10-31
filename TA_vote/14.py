def start_adventure():
    print("Welcome to los santos pick a team")
    print("1. police")   #list of teams
    print("2. civilian ")

    choice = input("> ")

    if choice == "1":  #pick a team
        join_police()
    elif choice == "2":
        join_civilian()
    
    else:
        print("Invalid choice. Try again")
        start_adventure()
def join_police():
    print("Welcome to team Police, pick a department")  #joining police
    print("1. detective")
    print("2. traffic cop")

    department = input("> ")
    if department == "1":
        detective()
    elif department == "2":
        cop()
   
    else:
        print("invalid choice. try again")
        join_police()
def detective():
    print("hello detective there are 2 cases on file choose a case to start on")
    print("1. the donut bandit")
    print("2. the runaway")

    case = input("> ")
    if case == "1":
        bandit()
    elif case == "2":
        runaway()
    else:
        print(" invalid character try again")
        detective()

def bandit():
    print("the bandit just robbed the donut shop what will you do ")
    print("1. chase him")
    print("2. look at the cameras")

    choice= input("> ")
    if choice == "1":
        print(" you caught the donut bandit it was wheatgg, you beat the game")
        start_adventure()
    elif choice == "2":
        print("the cameras are wiped and he got away you failed the mission")
        start_adventure()


def runaway():
    print("the runaway was last seen in the back of walmart, what will you do")
    print("1. go to walmart and look for him")
    print("2. call walmart to get the camera footage")

    q1 = input("> ")
    if q1 == "1":
        go()
    elif q1 == "2":
        call()
    else:
        print("invalid character try again")
        runaway()

def go():
    print("your in walmart and you see the runaway what will you do")
    print("1. call for backup ")
    print("2. go and try to arrest him")
    q2= input("> ")
    if q2 == "1":
        print("wait for back up")
        backup()
    elif q2 == "2":
        arrest()
    else:
        print("invalid character try again")
        go()
def backup():
    print("while waiting for backup to come what are you gonna do")
    print("1. wait where you are")
    print("2. go get a donut at the bakery")

    q4= input("> ")
    if q4 == "1":
        stay()
    elif q4 == "2":
        bakery()
    else:
        print("invalid character try again")
        backup()
def bakery():
    print("you ate 100 donuts and beat the world record")
    start_adventure()

def stay():
    print(" backup is here and they arrested him you beat the game")

def arrest():
    print("you arrested him!!!")
    start_adventure()

def call():
    print("walmart sent the footage and the runaway is there, what will you do")
    print("1. go to  walmart with backup")
    print("2. sit in your office")
    q3= input("> ")
    if q3 == "1":
        a1()
    elif q3== "2":
        print(" you got fired for being lazy")
        start_adventure()
    else:
        print("invalid character try again")
        call()
def a1():
    print(" your group arrested the runaway congrats you won")
    start_adventure()
def cop():
    print("now that your a cop pick a place to start")
    print("1. 40th st")
    print("2.the highway")

    road = input("> ")
    if road == "1":
        print("someone ran up to your car and took it> GAME OVER")
    elif road== "2":
        highway()
    else:
        print(" invalid character try again")
        cop()
def highway():
    print("someone just passed you going 100 mph what will you do")
    print("1. chase after him")
    print("2. let him go")
    print("3. call for backup and eat a donut")
    
    q5 = input("> ")
    if q5 == "1":
        chase()
    elif q5 == "2":
        print("your boss found out you let him go now your fired")
        start_adventure()
    elif q5 == "3":
        print(" you ate too many donuts now your paralized and collect disability")
        start_adventure()
def chase():
    print("you stoped him and saved the day")
    start_adventure()

    





def join_civilian():
    print(" Welcome to team Civilian, your job is to be an outstanding citizen what will you do today")
    print("1. go to the store")
    print("2. stay home")
    q6= input("> ")
    if q6 == "1":
        leave()
    elif q6 == "2":
        stay_home()
    else:
        print("invalid character try again")
        join_civilian()
    
def leave():
    print("what store do you want to go to")
    print("1. target")
    print("2. walmart")

    q7=input("> ")
    if q7 == "1":
        target()
    elif q7 == "2":
        walmart()
    else:
        print("invalid character try again")

def stay_home():
    print("what do you want to do at home")
    print("1. play video games")
    print("2. do laundry")
    print("3. watch a movie")

    q1=input("> ")
    if q1 == "1":
        game()
    elif q1 == "2":
        laundry()
    elif q1 == "3":
        movie()
    else:
        print("invalid character try again")
        stay_home()
def target():
    print("on your way to target you get caught speeding what will you do")
    print("1. run from the police")
    print("2. stop for the police")

    q1=input("> ")
    if q1 == "1":
        run()
    elif q1 == "2":
        stop()
    else:
        print("invalid character try again")
        target()
    
def walmart():
    print("your at walmart and while you were shopping someone was running from the police what will you do")
    print("1. try to stop him with your shopping cart")
    print("2. move out the way")

    q1 = input("> ")
    if q1 == "1":
        stop_him()
    elif q1 == "2":
        move()
    else:
        print("invalid character try again")
        walmart()
    
def game():
    print("while you are playing games you hear a window break what will you do")
    print("1. hide and call the police")
    print("2. go investigate")

    q1=input("> ")
    if q1 == "1":
        hide()
    elif q1 == "2":
        investigate()
    else:
        print("invalid character try again")
        game()

def run():
    print("your gatting chased!!! there's an exit coming up will you take it")
    print("1. yes")
    print("2. no")

    q1=input("> ")
    if q1 == "1":
        yes()
    elif q1 == "2":
        no()
    else:
        print("invalid character try again")
        run()
def stop():
    print("the officer gave you your third ticket of the week and you got arested")
    print("you are NOT an outstanding citizen. FAILED ")
    start_adventure()
def no():
    print("there was traffic  on the highway and you were caught")
    start_adventure()

def stop_him():
    print("you stopped the criminal and the city awarded you the medal of honor")
    print("you completed your task")
    start_adventure()

def move():
    print("the police are dissapointed you failed your task start over")
    start_adventure()
    
def hide():
    print("you called the police they will be there in 10 minutes, you need a wepon what will you take")
    print("1. crowbar")
    print("2. baseball bat")
    print("3. slingshot")

    q1 = input("> ")
    if q1 == "1":
        crowbar()
    elif q1 == "2":
        bat()
    elif q1 == "3":
        slingshot()
    else:
        print("invalid character try again")
        hide()
def crowbar():
    print("you picked up the crow bar")
    wepon()
def bat():
    print("you picked up the bat")
    wepon()
def slingshot():
    print("you picked up the slingshot")
    wepon()

def wepon():
    print("you hear him coming are you sure you want to hide?")
    print("1. yes,hide")
    print("2. no, attack")

    q1 = input("> ")
    if q1 == "1":
        stay_hidden()
    elif q1 == "2":
        attack()
    else:
        print("invalid character try again")
        wepon()

def attack():
    print("he is stronger than you and you died")
    start_adventure()
    
def stay_hidden():
    print("he didnt find you and the police arrested him you successfully evaded the burgler ")
    start_adventure()


def investigate():
    print("a robber is in your house what now")
    print("1. go hide and call the police")
    print("2. attack him")

    q1 = input("> ")
    if q1 == "1":
        hide()
    elif q1 == "2":
        attack()
    else:
        print("invalid character try again")
    
def yes():
    print("you were able to escape the cops and saved your reputation")
    print("now start over")
    start_adventure()

def laundry():
    print("while doing laundry a robber jumped in the laundry window> GG < try again")
    stay_home()

def movie():
    print("what movie do you want to watch")
    print("1. avatar")
    print("2. cars 2")
    
    q1 = input("> ")
    if q1 == "1":
        watch_movie()
    elif q1 == "2":
        watch_movie()
    else:
        print("invalid character try again")
        movie()
def watch_movie():
    print("while you were watching a movie you heared a window break what will you do")
    print("1. hide")
    print("2. investigate")

    q1 = input 
    if q1 == "1":
        hide()
    elif q1 == "2":
        investigate()
    else:
        print("invalid character try again")
        watch_movie()



    start_adventure()

