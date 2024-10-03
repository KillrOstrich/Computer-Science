def Data_three():
    A = input("give me a word")                #retriving varibles
    b = input("now give me a whole number")
    c = input("finally give me a decimal")

    B = int(b)             #converting nessicary varibles
    C = float(c)
    D = str (B + C)        #converting int and float to string

    return D + " " + A      #return

D = Data_three()      #function to variable
print(D)         #printing