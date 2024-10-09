x = input("how fast are the wind speeds in MPH? ")
x = int(x)

if x < 74:
    print("tropical storm")

elif x < 96:
    print("category 1 Hurricane")

elif x < 111:
    print("category 2 hurricane")

elif x < 130:
    print("category 3 hurricane")

elif x < 157:
    print("category 4 hurricane")

elif x >= 157:
    print("category 5 hurricane")