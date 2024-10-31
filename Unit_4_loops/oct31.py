import random
#4 collections, tuple, set, >list, and >dictonary
#first is lists, lists are a way to store more than one value in one variable called ITEMS
#This can be acessed by the INDEX (position in list)
#index                   0                 1             2                 3
best_halo_weapons = ["Energy sword", "gravity hammer", "Skewer"]

print(best_halo_weapons[0])

Skewer = 2

print(best_halo_weapons[Skewer])

print(len(best_halo_weapons))
print(best_halo_weapons[0]) #best item
print(best_halo_weapons[len(best_halo_weapons)-1])

#lists can be changed
best_halo_weapons[2] = "Shotgun"
print(best_halo_weapons)

#list functions
#.pop(removes a item at a position), .remove(removes an item by value- remove instance of value insted of position), .append(adds a value as a new item to the end of the list), .sort(), max(), min()

Random_int  = [random.randint(0,100), random.randite(0,100), random.randite(0,100)]
print(Random_int)

#,sort(sorts int small to big)
Random_int.sort()
print(Random_int)

# max() and min
print(max(Random_int))

#string is list
print("Braden" [0])

print(len("Braden"))