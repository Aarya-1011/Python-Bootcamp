#Write a Python program to print a box like pattern of asterics (*) as shown below with size according to the input from the user.

x=int(input())
for i in range(x):
    for j in range(x):
        if i==0 or i==x-1 or j==0 or j==x-1:
            print('*',end='')
        else:
            print(' ',end='')
      
    print()
