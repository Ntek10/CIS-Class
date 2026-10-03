#M6p4.py      Nick    10/02

#input

ticketQty= int(input("Enter number of tickets: "))

#process

if ticketQty>=25:
    ticketPrice= 50
else:
    if ticketQty>=10:
        ticketPrice= 60

    else:
        if ticketQty>=5:
            ticketPrice= 70

        else:
            ticketPrice= 75

totalCost= (ticketQty*ticketPrice)

#output

print("-------Summary-------")

print("Number of tickets: ", ticketQty)

print("Price per ticket: ", ticketPrice)

print("Total cost: ", totalCost)



                     
