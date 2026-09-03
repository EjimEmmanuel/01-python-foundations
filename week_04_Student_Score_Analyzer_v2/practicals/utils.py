def calculate_average(student):
    return (student["math"] + student["english"] + student["science"] / 3)

def get_status(average, pass_mark=50):
    return "Pass" if average >= pass_mark else "Fail" 
def Need_support(student):
    if student["average"] < 50 or student["attendance"] < 75:
        return True
    return False

def Find_Best(students):
    best_student = students[0]
    for student in students[1:]:
        if student["average"] > best_student["average"]:
            best_student = student
    return best_student

def Find_Weak(students):
    West_student = students[0]
    for student in students[1:]:
        if student["average"] > West_student["average"]:
            Warningest_student = student
    return West_student