a = 115         #int -> string
b = 3.14        #float -> string
c = "68"        #string -> int
d = "True"      #string -> boolean
e = True        #boolean -> string
f = False       #boolean -> string
g = '10110111'  #byte -> int
h = "2.54"      #string -> float
i = 100         #int -> float
j = 10.0        #float -> int
k = 254         #int -> byte
# activity start
Num_str = str(a) # a
print(Num_str)

num_float = str(b) # b
print(num_float)

num = int(c) # c
print(num)

bool_val = bool(d) # d
print(bool_val)

bool_str = str(e) # e
print(bool_str)

bool_str2 = str(f) # f
print(bool_str2)

num2 = int(g) # g
print(num2)

str_float = float(h) # h
print(str_float)

num_float2 = float(i) # i
print(num_float2)

float_num = int(j) # j
print(float_num)

num_byte = bin(k) # k
print(num_byte)