def square(number):
    result = number * number
    return result


def sub(num1, num2):
    result = num1 - num2
    return result


def main():
    # number = int(input("Enter a number: "))
    result = square(5) + square(10)
    print(result)
    result = sub(9, 5)
    print(result)


if __name__ == "__main__":
    main()
