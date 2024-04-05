def sort_students(students):
    # Sắp xếp sinh viên theo số bài làm đúng giảm dần và số lượt submit tăng dần
    students.sort(key=lambda x: (-x[1][0], x[1][1], x[0]))

def main():
    N = int(input("Nhập số lượng sinh viên: "))
    students = []
    
    for _ in range(N):
        name = input().strip()
        correct, submits = map(int, input().split())
        students.append((name, (correct, submits)))
    
    sort_students(students)
    
    # In ra bảng xếp hạng
    for student in students:
        print(student[0], student[1][0], student[1][1])

if __name__ == "__main__":
    main()
