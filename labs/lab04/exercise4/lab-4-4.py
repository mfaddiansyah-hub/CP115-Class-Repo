weight = float(input())
ticketPrice = float(input())
if weight == 0:
    finalPrice = ticketPrice - 10
else:
    if weight <= 15:
        finalPrice = ticketPrice
    else:
        weight = weight - 15
        finalPrice = ticketPrice + weight * 4
print(finalPrice)
