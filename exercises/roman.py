# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# convert roman number into decimal

def roman(x):
    if x == "I":
        return 1
    elif x == "V":
        return 5
    elif x == "X":
        return 10
    elif x == "L":
        return 50
    elif x == "C":
        return 100
    elif x == "D":
        return 500
    elif x == "M":
        return 1000
    else:
        print("Error, enter a valid roman number")


def parse(italic):
    sum = 0
    prevnum = 1001
    for i in italic:
        m = roman(i)
        if prevnum >= m:
            sum = sum + m
        else:
            sum = m - sum
        prevnum = m
    print(sum)


def main():
    x = input("Please enter a roman number: ")
    parse(x)


if __name__ == "__main__":
    main()
