# python list
x = [10, 2, 3, 4]
for i in range(0, 4):
    print("x[", i, "] = ", x[i])

y = [2, 7, 0, 3]
z = [5]*4
print(z)

for i in range(0, 4):
    z[i] = x[i]+y[i]
print(z)


total = 0
for i in range(0, 4):
    total += z[i]
print(total)
print(sum(z))

# total = 0
# total = total + z[0]
# total = total + z[1]
# total += z[2]
