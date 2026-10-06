number = int(input())

score = 0
ignored = 0

while number != 0:

    if number > score:
        score += number
        number = int(input())
        continue

    ignored += 1

    number = int(input())

print(score)
print(ignored)
