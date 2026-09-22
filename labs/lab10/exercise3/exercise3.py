target_points = int(input())
total_points = 0
rounds_played = 0

while total_points < target_points:
    rounds_played += 1
    points = int(input())
    total_points = total_points + points

print(total_points)
print(rounds_played)
