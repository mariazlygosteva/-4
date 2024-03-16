scores = input().split()
highest_score = int(scores[0])

for score in scores:
    if int(score) > highest_score:
        highest_score = int(score)

print(highest_score)