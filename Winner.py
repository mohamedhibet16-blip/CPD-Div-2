n = int(input())
rounds = []

# Step 1: store rounds and compute final scores
final_score = {}

for _ in range(n):
    name, score = input().split()
    score = int(score)
    rounds.append((name, score))
    
    if name not in final_score:
        final_score[name] = 0
    final_score[name] += score

# Step 2: find maximum score
max_score = max(final_score.values())

# Step 3: find candidates
candidates = set()
for name in final_score:
    if final_score[name] == max_score:
        candidates.add(name)

# Step 4: simulate again to find who reached max_score first
current_score = {}

for name, score in rounds:
    if name not in current_score:
        current_score[name] = 0
    
    current_score[name] += score
    
    if name in candidates and current_score[name] >= max_score:
        print(name)
        break
