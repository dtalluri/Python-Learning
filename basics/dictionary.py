x = {
    "Bob": 800,
    "alice": 350
}

print(x)

x["Joe"] = 23

print(x)

x["Bob"] = 900
print(x["Bob"])

for i in x:
    x[i] = x[i]+100

print(x)
