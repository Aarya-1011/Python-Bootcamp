#Following is KTU grading system(in percentage):
#Below 40 - F (Fail)
#40 to below 55 - P (Pass)
#55 to below 60 - D
#60 to below 65 - C
#65 to below 70 - C+
#70 to below 75 - B
#75 to below 80 - B+
#80 to below 85 - A
#85 to below 90 - A+
#90 and above - S
#Ask user to enter the total marks of the subject, marks she obtained and find the corresponding grade and print it.

a = int(input())
b = int(input())
x = b/a*100
if x<40:
    print(F)
elif x>=40 and x<55:
    print("P")
elif x>=55 and x<60:
    print("D")
elif x>=60 and x<65:
    print("C")
elif x>=65 and x<70:
    print("C+")
elif x>=70 and x<75:
    print("B")
elif x>=75 and x<80:
    print("B+")
elif x>=80 and x<85:
    print("A")
elif x>=85 and x<90:
    print("A+")
elif x>=90:
    print("S")
