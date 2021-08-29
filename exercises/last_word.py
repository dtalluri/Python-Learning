# Create a program to find the length of the last word in a string
# ex: "Hello John" will give you 4


def last_word(x):
    length = x.split()
    print(length[-1])


def main():
    x = input("Please enter a sentence: ")


if __name__ == "__main__":
    main()
