speed = int(input())

total_readings = 0
longest_streak = 0

prev_streak = 0
current_streak = 0

while speed >= 0:

    if speed < 20:
        current_streak += 1
    else:
        prev_streak = current_streak

    if current_streak >= prev_streak:
        longest_streak = current_streak
    else:
        longest_streak = prev_streak

    total_readings += 1

    speed = int(input())

print(total_readings)
print(longest_streak)
