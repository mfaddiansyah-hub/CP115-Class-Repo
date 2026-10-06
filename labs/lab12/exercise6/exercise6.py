a = int(input())

overtake_round = 0
count = 1

while a != -1:

    if (count % 2) != 0:
        teamA = a
        count += 1
        a = int(input())
        continue
    else:
        teamB = a

    if teamA >= teamB:
        overtake_round += 1
    else :
        overtake_round += 1
        break

    count += 1
    a = int(input())

if a == -1:
    overtake_round = 0

print(overtake_round)