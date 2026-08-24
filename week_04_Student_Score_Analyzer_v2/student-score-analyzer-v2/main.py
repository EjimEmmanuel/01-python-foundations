import json
from pathlib import Path
from utils import (calculate_average, get_status, find_weak, find_best, need_support )    


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "students.json"
REPORT_FILE = BASE_DIR / "reports" / "report.txt"

def load_students(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
""" writing the report to a file """
def write_report(path, report):
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)
    return report


def main():
    try:
        students = load_students(DATA_FILE)
    except FileNotFoundError:
        print(f"Could not find student data at {DATA_FILE}")
        return
    except json.JSONDecodeError as error:
        print(f"could not decode file {error}")
        return
    if not students:
        print("Student data is really empty.")
        return
    for student in students:
        average = calculate_average(student)
        status = get_status(average)
        student["average"] = average
        student["status"] = status
        student["needsupport"] = need_support(student, average)
    ### Class average
    class_total = 0
    for student in students:
        class_total += student["average"]
    class_average = class_total / len(students)
    #### 
    best_student = find_best(students)
    
    weak_student = find_weak(students)
    """report-writing """
    report = generate_report(student, students, weak_student, best_student, class_average)
    report_result = write_report(REPORT_FILE, report)
    print(report_result)


def generate_report(student, students, weak_student, best_student, class_average):
    lines = []
    lines.append("=" * 50)
    lines.append("")
    lines.append("================== STUDENT SCORE ANALYZER =================")
    lines.append("")
    lines.append("=" * 50)
    for count, student in enumerate(students, start=1):
        lines.append(
            f"{count}. {student['name']:<10} "
            f"Average: {student['average']:>5.2f}  "
            f"{student['status']:<4}  "
    )
    lines.append("")
    lines.append(f"Class Average: {class_average:.2f}")
    lines.append(f"Best student: {best_student['name']} - {best_student['average']:.2f}")
    lines.append(f"Weak student: {weak_student['name']} - {weak_student['average']:.2f}")
    return "\n".join(lines)



if __name__ == "__main__":
    main()