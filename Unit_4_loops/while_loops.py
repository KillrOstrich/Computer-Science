real_pass = "ninjalowtaper"
entered_pass = ""
attemt = 0
while entered_pass != real_pass:
    entered_pass = input("please enter password")

    if entered_pass == real_pass:
        print("access granted")

    else:
        print("access denied")
        print("try again")
        attemt += 1
        print("attemt #" + attemt)
