magazineNumber = int(input())
if unitPrice >= 5:
    unitPrice = 5
else:
    unitPrice = 7
finalPrice = magazineNumber * unitPrice
print(finalPrice)
