if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    if 2 <= n <= 10 and all(-100<=i<=100 for i in arr):               
                max_score = max(list1)
                while max_score in list1:
                    list1.remove(max_score)
    print(max(list1))
