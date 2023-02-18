#Karishma and her father started a shop for selling market goods to the customers. But the father doesn't know how to do business, but Karishma does. She explained how one can buy goods at a cheaper price and market to the customers and make them buy the products

n1=float(input())
n2=float(input())
n3=int(input())
if(n1>n2):
    amount=(n1-n2)*n3
    print("Total Loss Amount = {0}".format(amount))
elif(n2>n1):
    amount=(n2-n1)*n3
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss!!!")
