hours = float(input())
if hours <= 2:
    parkingFee = 0
else:
    if hours <= 5:
        hours = hours - 2
        parkingFee = hours * 2
    else:
        hours = hours - 5
        parkingFee = 3 * 2 + hours * 3
if parkingFee <= 30:
    pass
else:
    parkingFee = 30
print(parkingFee)
