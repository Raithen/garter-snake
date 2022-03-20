scores = [92, 78, 65, 89, 86, 55, 91, 64, 89]

high_score = 0

for score in scores:
    if score > high_score:
        high_score = score

print(high_score)