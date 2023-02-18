#Write a python program to accept two strings as input. Each line of the input will be a name in reverse. Print a wedding card that displays “ Name-1 weds Name-2”, where Name-1 and Name-2 are their names in proper order.

x = input()
y = input()
reversed_x= x[::-1]
reversed_y = y[::-1]
print(reversed_x +" weds "+ reversed_y)
