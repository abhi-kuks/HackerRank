Question : https://www.hackerrank.com/challenges/finding-the-percentage/problem


n = int(input("Enter Number of students in class: "))
student_marks ={}
scores = []
for _ in range(n):
    name , *line = input().split()
    scores = list(map(float , line))
    student_marks[name]=scores
query_name = input("\nEnter the name of the student:")
query_name=query_name.title()
if query_name in student_marks:
    l=student_marks[query_name]
    avg = sum(l) / len(l)
    print(f"{avg:.2f}")
else:
    print(f"{query_name} not in class.")
