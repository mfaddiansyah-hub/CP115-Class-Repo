grade = float(input())

valid_count = 0
total = 0

while grade != -1:

    if grade >= 0 and grade <= 100:
        valid_count += 1
        total += grade
        grade = float(input())
        continue

    grade = float(input())

average = total / valid_count

print(valid_count)
print(f"{average:.2f}")
