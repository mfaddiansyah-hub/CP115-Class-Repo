minutes = int(input())

customers = 1
total_minutes = minutes

while total_minutes <= 60:

    if total_minutes == 60:
        break

    minutes = int(input())

    customers += 1
    total_minutes += minutes

print(customers)
print(total_minutes)
