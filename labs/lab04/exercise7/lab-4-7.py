tempRoom = int(input())
tempTarget = int(input())
if tempRoom < tempTarget:
    power = tempTarget - tempRoom
    power = power * 10
else:
    if tempRoom > tempTarget:
        power = tempRoom - tempTarget
        power = power * 8
    else:
        power = 0
if power > 100:
    power = 100
print(power)
