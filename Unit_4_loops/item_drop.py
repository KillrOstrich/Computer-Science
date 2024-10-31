import random
def drop_item():
    roll = random.randint(0,10000)
    if roll < 7000:
        print("NORMAL ITEM")

    elif roll < 9000:
        print("MAGIC ITEM")
        
    elif roll < 9900:
        print("RARE ITEM")
        
    elif roll < 9990:
        print("LEGENDARY ITEM")
        
    elif roll <= 10000:
        print("UBER ITEM")

    if input("Play again?\n>") == "y":
        drop_item()

drop_item()