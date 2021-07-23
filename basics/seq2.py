x = ["apple", "leaves", "dog"]
# for i in range(0, len(x)):       printing the list
#     print(x[i])

# for i in x:                      printing a list
#     print(i)

print(x)
# add item to list
x.append("cat")
print(x)

y = [3, 4, 5]
# combine two different lists
# x.extend(y)
x = x+y
print(x)

x.remove("dog")
# remove item from a list
print(x)
x.pop(1)
# remove item from a list using index
print(x)


c = [30, 3, 57, 12, 37]
c.sort()
# sorts in numerical order
print(c)

y = ["truck", "house", "tree", "car"]
y.sort(reverse=True)
# sorts in reverse order
print(y)

for i in y:
    if "a" in i:
        print(i)
