#M5p3.py      Nick      09/23

#input
bookNumber= int(input("Number of books: "))

#input
bookCost= float(input("Cost per book: "))

#process
orderTotal= bookCost*bookNumber 

#process
if orderTotal> 50.00:
    shipping=0.00

#process
else: 
    shipping= 25.00

#output
print("Order total: ",orderTotal)

#output
print("Shipping charge: ",shipping)
