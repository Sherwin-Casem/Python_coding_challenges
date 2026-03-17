if __name__ == '__main__':
    N = int(input())
    students = []
    if 2<= N <= 5:        
        for _ in range(N):
            name = input()
            score = float(input())
            students.append([name, score])
        
        scores = sorted(set([s[1] for s in students]))
        second_lower = scores[1]
        
        names = []
        for student in students:
            if student[1] == second_lower:
                names.append(student[0])
        for name in sorted(names):
            print(name)
