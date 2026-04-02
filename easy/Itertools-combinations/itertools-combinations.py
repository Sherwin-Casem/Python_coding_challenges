from itertools import combinations

# Read input
S, k = input().split()
k = int(k)

# Sort the string
S = sorted(S)

# Generate combinations
for i in range(1, k + 1):
    for c in combinations(S, i):
        print(''.join(c))
