def rank(students):
    sorted_students = sorted(students.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))
    return sorted_students

def main():
    tess = int(input())
    students = {}
    for _ in range(tess):
        name = input()
        correct, submit = map(int, input().split())
        students[name] = (correct, submit)
    
    students = rank(students)
    for student in students:
        print(student[0] + " " + str(student[1][0]) + " " + str(student[1][1]))


main()