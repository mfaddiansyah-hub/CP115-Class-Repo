num_rounds = int(input())

for i in range(num_rounds):
    score = int(input())

    if score > 100:
        bonus = score * (20/100)
        final_score = final_score + score + bonus
    else:
        final_score = final_score + score

rounds_processed = num_rounds

print(f"{final_score:.1f}")
print(rounds_processed)
