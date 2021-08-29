arr = [0, 1, 1, 2, 2, 3, 3, 3, 4]
out = [0, 1, 2, 3, 4, 0, 0, 0, 0]
i = 1
x = len(arr)
while i < x:
    if arr[i] == arr[i-1]:
        del arr[i]
        x = x - 1
        i = i-1
    i += 1


print(arr)
# print number element in the array
# print the array
