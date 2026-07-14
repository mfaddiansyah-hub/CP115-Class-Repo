minutesBefore = int(input())
if minutesBefore < 0:
    pass
else:
    if minutesBefore > 30:
        price = 80 - 15
    else:
        price = 80
    membership = input()
    if membership == "yes":
        price = price * 0.85
    print(price)
