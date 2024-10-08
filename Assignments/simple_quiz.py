

score = 0
a = input("what is 5 + 10? ")
a = int(a)

if a == 15:
    print("correct")
    score = score + 1

else:
    print("incorrect")

b = input("what is 20 - 8? ")
b = int(b)

if b == 12:
    print("correct")
    score = score + 1

else:
    print("incorrect")

c = input("what is 9 x 10? ")
c = int(c)

if c == 90:
    print("correct")
    score = score + 1

else:
    print("incorrect")

d = input("what is 9 / 3? ")
d = int(d)

if d == 3:
    print("correct")
    score = score + 1

else:
    print("incorrect")

e = input("what is -9 + 8? ")
e = int(e)

if e == -1:
    print("correct")
    score = score + 1

else:
    print("incorrect")

score = str(score)
print("your score is " + score + "/5")