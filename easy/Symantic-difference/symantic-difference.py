n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

result = sorted(a.symmetric_difference(b))

for num in result:
    print(num)