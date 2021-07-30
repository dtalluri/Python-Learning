# 121 252 10201


def palindrome(number):
    nstr = str(number)
    rstr = "".join(reversed(nstr))
    if nstr == rstr:
        return True
    return False


def main():
    number = int(input("Enter a number: "))
    if palindrome(number):
        print("It's a palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()
