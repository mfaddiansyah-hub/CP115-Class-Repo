num_rounds = int(input())
final_score = 0
bonus = 0

for i in range(num_rounds):
    score = int(input())

    if score > 100:
        bonus = score * (20/100)
    else:
        bonus = 0
        
    final_score = final_score + score + bonus

rounds_processed = num_rounds

print(f"{final_score:.1f}")
print(rounds_processed)
