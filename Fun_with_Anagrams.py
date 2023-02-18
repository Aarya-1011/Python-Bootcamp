#Write a python function to check whether two strings are anagrams or not.
#(An anagram is a word that is formed by rearranging the letters of another word.)

x=input()
y=input()
if sorted(x)==sorted(y):
    print('Yes')
else:
    print('No')
