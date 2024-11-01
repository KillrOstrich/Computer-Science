#for loops is big deal
#allows programmer to repeat

for i in range(90,101):
    print(i)

fav_food = ["eggs bene", "mac'n cheese", "steak"]

for food in fav_food:
    print(food)

for i in range(10,-1,-1):
    print(i)

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total = total + num
print(total)

ints = [1, 2, 3, 4, 5]
newlist = []
for i in ints:
    newlist.append(i*i)

print(newlist)

stringy = input("please enter word\n>")
numvowels = 0
for s in stringy:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1

print(numvowels)

try:
    multi = int(input("gimme int\n>"))
except:
    print("womp")

for i in range(0,multi+1):
    print(str(multi) + " X " + str(i) + " = " + str(multi*i))

names = ["pete", "john", "paul", "bob"]
for name in names:
    print("Hello, " + name + "!")