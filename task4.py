grades = []
while True:
    grade = input("Enter a grade (-1 to stop): ")
    if grade == '-1':
        break
    grades.append(int(grade))

average_grade = int(sum(grades) / len(grades))

print("\nAverage grade:", average_grade)
print("Grades in order:")
for grade in grades:
    print(grade)
