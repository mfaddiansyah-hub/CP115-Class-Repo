# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

coffee = 3.50
muffin = 2.10
water = 1.05

qtycoffee = int(input())
qtymuffin = int(input())
qtywater = int(input())

totalcoffee = float(qtycoffee) * coffee
totalmuffin = float(qtymuffin) * muffin
totalwater = float(qtywater) * water

subtotal = totalcoffee + totalmuffin + totalwater
tax = subtotal * (6/100)
fulltotal = subtotal + tax

print(f"========== RECEIPT ==========\nItem\tPrice\tQty\tTotal\nCoffee\t${coffee}\t{qtycoffee}\t${totalcoffee:.2f}\nMuffin\t${muffin}\t{qtymuffin}\t${totalmuffin:.2f}\nWater\t${water}\t{qtywater}\t${totalwater:.2f}\n-----------------------------\nSubtotal\t\t${subtotal:.2f}\nTax (6%)\t\t${tax:.2f}\nTotal\t\t\t${fulltotal:.2f}\n=============================")