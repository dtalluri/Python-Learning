# program for listing all the files

import os

x = os.listdir(".")
print(x)

# Create a file called output.txt

z = os.listdir(".")
if "abc" in z:
    exit
else:
    os.mkdir("abc")
