# 001011+100001=101100

a = "1011"
b = "100001"

c = ""


def convBinary(x):
    sum = 0
    for i in range(0, len(x)):
        if x[i] == "1":
            p = 2**(len(x)-i-1)
            sum += p
    return sum


def convInteger(x):
    binary = ""
    while x != 0:
        binary = str(int(x % 2)) + binary
        x = int(x/2)
    return binary


y = convBinary(a)
z = convBinary(b)
print(y+z)
f = convInteger(y+z)
print(f)
