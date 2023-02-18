#Write a python program to accept a string as input. Create a new string by removing the first two characters from the input string and converting all the alphabets to smaller case. Print the new string as output.

name = input()
first_name = name[2::1]

first_name.lower()
print(first_name.lower())
