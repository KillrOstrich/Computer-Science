def devide_two_num():
    try:
     x = int(input("what is the first number?\n>"))
     y = int(input("what is the second number?\n>"))
     print(x/y)
    except:
       print("Invalid input")
       print("use numarical symbole")
       devide_two_num()