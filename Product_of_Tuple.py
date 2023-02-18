#Given an integer n and n space-separated integers as input, create a tuple, t , of those n integers. Then compute the product of all numbers in the given tuple

a=int(input())
x=map(int,input().split())
y=tuple(x)
b=1
for i in y:
    b=b*i
print(b)
