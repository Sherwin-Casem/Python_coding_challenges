from collections import namedtuple

n = int(input())

# read column names
columns = input().split()

# create namedtuple class
Student = namedtuple('Student', columns)

total = 0

for _ in range(n):
    data = input().split()
    student = Student(*data)  # unpack values
    total += int(student.MARKS)

average = total / n
print(f"{average:.2f}")
