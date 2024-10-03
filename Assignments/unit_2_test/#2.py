def add_three(a, b, c):
    print(a + b + c)    #how the function will add the variables
    return a + b + c

x = input()      #retriving variables
y = input()
z = input()

d = int(x)       #converting variables to intergers
e = int(y)
f = int(z)
F = add_three(d, e, f)   #function in variable
print(F)       #printing