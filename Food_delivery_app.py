#An online food delivery app gives 10% discount on orders above ₹300. Ask the user for order cost and estimate the total bill and print it.

a=float(int(input()))
if (a>300):
    print(a-(a*10)/100)
else:
    print(a)
