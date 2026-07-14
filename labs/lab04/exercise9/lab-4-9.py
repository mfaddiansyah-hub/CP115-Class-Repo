gb = int(input())
planA = 10 + gb
planB = 25 + (gb - 20) * 3
if planA < planB:
    bill = planA
else:
    bill = planB
print(bill)
