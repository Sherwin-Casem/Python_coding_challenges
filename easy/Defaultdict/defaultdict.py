from collections import defaultdict

n, m = map(int, input().split())

# store positions of each word
positions = defaultdict(list)

# read group A
for i in range(1, n + 1):
    word = input()
    positions[word].append(i)

# read group B and print results
for _ in range(m):
    word = input()
    
    if word in positions:
        print(*positions[word])
    else:
        print(-1)
