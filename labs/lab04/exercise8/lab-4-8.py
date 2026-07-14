distance = float(input())
if distance > 2:
    distance = distance - 2
    fare = 4 + distance * 1.2
else:
    fare = 4
afterMidnight = input()
if afterMidnight == "yes":
    fare = fare + 3
print(fare)
