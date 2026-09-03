from utils import (calculate_average, Find_Best, Find_Weak, Need_support, get_status)


import json
class_total = 0 
needing_support = []


def load_students(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def generage_report(student, students, best_student, weak_student, class_average):
    lines = []
    lines.append("=" * 50)
    lines.append(" ")
    lines.append("============== STUDENT SCORE ANALYSER ============")
    lines.append(" ")
    lines.append("=" * 50)
    lines.append(" ")

    for count, student in enumerate(students, start=1):
            lines.append(
            f"{count}. {student['name']:<10} "
            f"Average: {student['average']:>5.2f}  "
            f"Status: {student['status']:<4}  "
    )
    lines.append(" ")
    lines.append(f"class Average: {class_average:.2f} ")
    lines.append(f"Best Student: {best_student["name"]} - {best_student["average"]:.2f} ")
    lines.append(f"Weakest Student: {weak_student["name"]} - {weak_student["average"]:.2f} ")
    lines.append("Students Needing support:")
    for student in needing_support:
        lines.append(f"{student["name"]} - {student["average"]:.2f} -- {student["attendance"]}% ")
    return "\n".join(lines)

def write_report(path, report):
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)
    return report

    

def main():
    try:
        students = load_students("./data/practical.json")
    except FileNotFoundError:
        print("This file was not found")
    except json.JSONDecodeError:
        ("The file data is malformed")
    else:
        for student in students:
            average = calculate_average(student)
            status = get_status(average)
            student["average"] = average
            student["status"] = status
            need_support = Need_support(student)  
            student["Need_support"] = need_support
            if student["Need_support"]:
                needing_support.append(student)
    best_student = Find_Best(students)
    weak_student = Find_Weak(students)
    for student in students:
        class_total =+ student["average"]
    class_average = class_total / len(students)
    report = generage_report(student, students, best_student, weak_student, class_average)
    write = write_report("./reports/report.txt", report)
    print(write)





if __name__ == "__main__":
    main()