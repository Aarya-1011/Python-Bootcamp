#Write a python program to print all the numbers in a given range that are divisible by 5 and numbers that are divisible by 3 but not divisible by both, 5 and 3

n=int(input())
m=int(input())
while n<=m:
    if n%3==0 and n%5==0:
        pass
    elif n%5==0:
        print(n)
    elif n%3==0:
        print(n)
    n=n+1
