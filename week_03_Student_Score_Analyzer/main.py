

students = [
    {"name": "Ada", "math": 78, "english": 82, "science": 74, "attendance": 92},
    {"name": "David", "math": 64, "english": 58, "science": 61, "attendance": 80},
    {"name": "Zainab", "math": 91, "english": 88, "science": 95, "attendance": 97},
    {"name": "Chinedu", "math": 45, "english": 52, "science": 48, "attendance": 72},
    {"name": "Mariam", "math": 83, "english": 79, "science": 86, "attendance": 90},
    {"name": "Tobi", "math": 38, "english": 44, "science": 41, "attendance": 68},
    {"name": "Aisha", "math": 70, "english": 75, "science": 72, "attendance": 88},
    {"name": "Emeka", "math": 59, "english": 63, "science": 57, "attendance": 76},
    {"name": "Ngozi", "math": 87, "english": 90, "science": 84, "attendance": 94},
    {"name": "Samuel", "math": 50, "english": 48, "science": 52, "attendance": 73},
]
PASS_MARK = 50
MIN_ATTENDANCE = 75
class_total = 0
pass_count = 0
fail_count = 0
best_student = students[0]
weak_student = students[0]
student_help = []
below_pass = []
needs_help = []


for student in students:
    average = (student["math"] + student["english"] + student["science"]) / 3
    average = round(average, 1)
    student["average"] = average


for student in students:
    if student["average"] >= PASS_MARK:
        student["status"] = "Pass"
        pass_count += 1
    else:
        student["status"] = "Fail"
        fail_count += 1
#### calculate the class average
for student in students:
    class_total +=  student["average"]
class_average = class_total / len(students)
print(f"Class average: {class_average:.1f}")

### finding the best and weak student

for student in students:
    if student["average"] > best_student["average"]:
        best_student = student
        print(f"Best studzzzent: {best_student['name']} — {best_student['average']}")
    elif best_student["average"] == student["average"] and best_student["name"] != student["name"]:
        runner_up_1, runnerup_2 = best_student, student
        print(f"Best stufffdent: {runner_up_1['name']} — {runnerup_2['name']} — {runner_up_1['average']}")
for student in students:
    if student["average"] < weak_student["average"]:
        weak_student = student
    elif weak_student["average"] == student["average"] and weak_student["name"] != student["name"]:
        runner_up_1, runnerup_2 = weak_student, student
        print(f"Weak student: {runner_up_1['name']} — {runnerup_2['name']} — {runner_up_1['average']}")


print("Weak student:", weak_student["name"])

###### filtering students who need help based on average and attendance
for student in students:
    if student["average"] < PASS_MARK or student["attendance"] < MIN_ATTENDANCE:
        student_help.append(student) 
for _ in student_help:
    print(f"needhelp: {_["name"]}")

### filtering students who are below pass mark
for student in students:
    if student["average"] < PASS_MARK:
        below_pass.append(student)
        print(f"below_pass: {_["name"]}")
### filtrering students who need help based on average and attendance
for student in students:
    if student["average"] < PASS_MARK or student["attendance"] < MIN_ATTENDANCE:
        needs_help.append(student)

### printing the final report
print()
print("================== STUDENT SCORE ANALYZER =================")
print()
for count, student in enumerate(students, start=1):
    print(
        f"{count:>2}. "
        f"{student['name']:<10} "
        f"Average: {student['average']:>5.1f}  "
        f"{student['status']:<4}  "
        f"Attendance: {student['attendance']}%"
    )
print()
print("-------------------- CLASS SUMMARY ---------------------")
print()
print(f"Class Average: {class_average:.1f}")
print(f"Best Student: {best_student['name']} — {best_student['average']}")
print(f"Weak Student: {weak_student['name']} — {weak_student['average']}")
print(f"Pass Count: {pass_count}")
print(f"Fail Count: {fail_count}")
print()
print("Students below pass threshold:")
if (len(below_pass)) == 0:
    print("No students below pass threshold.")  
else:
    for student in below_pass:
        print(f"- {student['name']} — {student['average']}")
print()
print("Students needing help are below:")
for student in needs_help:
    print(f"- {student['name']} {student['average']} — Attendance: {student['attendance']}%")
print("=" * 60)