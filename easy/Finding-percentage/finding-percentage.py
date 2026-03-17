if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if not 2 <= n <= 10:
        exit()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        if len(scores) != 3:
            exit()
        if not all(0 <= s <= 100 for s in scores):
            exit()            
        student_marks[name] = scores
     
    query_name = input()
     
    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)
    print(f"{avg:.2f}")
