
### calculate average
def calculate_average(student):
    return (student["math"] + student["english"] + student["science"]) / 3

### get_status
def get_status(average, pass_mark=50):
    if average >= pass_mark:
        return "PASS"
    return "FAIL"


### finding best_student
def find_best(students):
    best_student = students[0]
    for student in students[1:]:
        if student["average"] > best_student["average"]:
            best_student = student
    return best_student
### finding weak_student

def find_weak(students):
    weak_student = students[0]
    for student in students[1:]:
        if student["average"] < weak_student["average"]:
            weak_student = student
    return weak_student 


### needing support
def need_support(student, average):
    return average < 50 or student["attendance"] < 75
