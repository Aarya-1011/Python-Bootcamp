#Given 5 pairs of numbers and names. You have to print out the names in ascending order based on the numbers assosciated with the name.

di={}
li=list()
for i in range(5):
    x=input().split()
    p=int(x[0])
    li.append(p)
    di[p]=x[1]
li.sort()
for i in li:
    print(di[i])
