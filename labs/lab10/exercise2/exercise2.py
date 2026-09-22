num_days = int(input())
danger_threshold = float(input())
danger_days = 0
average_temp = 0
total_temp = 0

for i in range(num_days):
    temperature = float(input())

    if temperature > danger_threshold:
        danger_days += 1

    total_temp = total_temp + temperature

average_temp = total_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")
