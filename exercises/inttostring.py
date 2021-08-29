def convint(x):
    sum = 0
    for i in range(0, len(x)):
        if x[i] == "0":
            sum = sum * 10
        elif x[i] == '1':
            sum = sum * 10 + 1
        elif x[i] == '2':
            sum = sum * 10 + 2
        elif x[i] == '3':
            sum = sum * 10 + 3
        elif x[i] == '4':
            sum = sum * 10 + 4
        elif x[i] == '5':
            sum = sum * 10 + 5
        elif x[i] == '6':
            sum = sum * 10 + 6
        elif x[i] == '7':
            sum = sum * 10 + 7
        elif x[i] == '8':
            sum = sum * 10 + 8
        elif x[i] == '9':
            sum = sum * 10 + 9
    return sum


y = convint("102")
print(y)
