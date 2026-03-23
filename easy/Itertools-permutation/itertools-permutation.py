from itertools import permutations

# Read input
S, k = input().split()
k = int(k)

# Generate permutations
for p in permutations(sorted(S), k):
    print(''.join(p))
