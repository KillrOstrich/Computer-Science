prime = True
cost = 25
age = 18
consent = False

if prime:
    if age >= 18:
        print("free shipping")
    elif consent:
        print("free shipping")
    else:
        print("no free shipping")

elif cost >= 25:
    if age >= 18:
        print("free shipping")
    elif consent:
        print("free shipping")
    else:
        print("no free shipping")

else:
    print("no free shipping")


raining = input("is it raining?\n>")

if raining.lower() == "yes":
    outside = input("are you going outside")
    
    if outside.lower("yes"):
        print("bring an umbrella")
    
    else:
        print("no umbrella")

else:
    print("no umbrella")