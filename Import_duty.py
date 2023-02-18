#Write a program that imports math module and uses its builtin fuctions to calculate the result.

import math
a=input().split()
for i in a:
    x=int(i)+math.factorial(int(i))
    print(x)
    x=0
