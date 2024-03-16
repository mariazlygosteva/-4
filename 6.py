score = input().split(":")
team1_score = int(score[0])
team2_score = int(score[1])

if team1_score > team2_score:
    print(1)
elif team2_score > team1_score:
    print(2)
else:
    print(0)