#Anson has a huge collection of currencies of different country. He decided to count the total number of distinct currencies in his collection. He asked for your help. You pick the currency notes one by one from a stack of N currency notes.
#Find the total number of distinct currency notes.

a=int(input())
b=[]
for i in range(a):
    c=input()
    b.append(c)
d=set(b)
print(len(d))
