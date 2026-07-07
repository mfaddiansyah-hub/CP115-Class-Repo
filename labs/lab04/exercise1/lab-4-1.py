kwh = float(input())
if kwh <= 100:
    charges = 0.3
    totalBill = kwh * charges
else:
    if kwh <= 200:
        charges = 0.5
        totalBill = 100 * 0.3 + kwh - 100 * charges
    else:
        charges = 0.75
        totalBill = 100 * 0.3 + 100 * 0.5 + kwh - 200 * charges
print(totalBill)
