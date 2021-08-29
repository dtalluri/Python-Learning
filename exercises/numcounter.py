a = "178901229"


# def count(x, k):
#     c = 0
#     for j in k:
#         if j == x:
#             c += 1
#     return c

d = {}

for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
print(d)

# for x in a:
#     b = count(x, a)
#     if x == "1":
#         print(b, "ones")


# x = a.count("1")
# print(x, "ones")
# x = a.count("2")
# print(x, "twos")
# x = a.count("3")
# print(x, "threes")
# x = a.count("4")
# print(x, "fours")
# x = a.count("5")
# print(x, "fives")
# x = a.count("6")
# print(x, "sixes")
# x = a.count("7")
# print(x, "sevens")
# x = a.count("8")
# print(x, "eights")
# x = a.count("9")
# print(x, "nines")
