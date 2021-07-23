# ask for a number and store inside n.
# create a list with size n.
# prompt for n numbers and store into previously created array
# find sum,average
# n = int(input("Enter a number: "))
# x = [1]*n
# print('n =', n)
# for i in range(0, n):
#     x[i] = int(input("Please enter n different numbers (n is shown above): "))
# print(x)

# *
# **
# ***
# ****

# n = int(input("Enter a number: "))
# for i in range(0, n):
#     for j in range(i, n):
#         print("*", end="")
#     print("")

#      *
#     ***
#    *****
#   *******
#  *********

# n = int(input("Enter a number: "))
# for i in range(0, n):
#     for k in range(i, n):
#         print(" ", end='')
#     for j in range(0, 2*i+1):
#         print("*", end='')
#     print("")


n = int(input("Enter a number: "))
for i in range(n-1, -1, -1):
    for k in range(i, n):
        print(" ", end='')
    for j in range(0, 2*i+1):
        print("*", end='')
    print("")
