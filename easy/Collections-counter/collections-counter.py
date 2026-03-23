from collections import Counter
X = int(input())
sizes = list(map(int, input().split()))
N = int(input())

total = 0

sizedic = Counter(sizes)

for _ in range(N):
    size, price = map(int, input().split())
    
    if sizedic[size]>0:
        total+=price
        sizedic[size]-=1
print(total)
