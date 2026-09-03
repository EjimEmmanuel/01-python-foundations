 ##   WEEK 4 ANSWERS
1. b
2. b
3. b
4. b
5. a
6. c
7. b
8. b
9. b
10. b
11. b
12. a
13. b
14. a
15. a
16. a
17. b
18. a
19. b
20. c
21. a
22. a
23. a
24. a 
25. a
26. c
27. a
28. a
29. b
30. b








##       WEEK 4 SECTION B THEORY
1. functions are useful and reusable because of it adequate reusability across files and another functions and are used where repeatable codes are to be written, they also give meaningfull names to defiinite responsiblities that perform a distinct task.

2. function definition is defining a function with a keyword "def" and a meaningful name relating to the task of the function, then followed by the function logical task and the values to return while function caling is calling a function that has already been defined when the function is to be used and assigned to a variable if the returned value of the called function is to be printed.

3. Parameter is the value that is passed to a function while the function is being defined while an argument is the value that is provided and passed to the function while the function is being called
Example:
Parameter ---->   def main(name):
Argument -----> main("emmanuel")

4. The difference between return keyword and print keyword is that return is used to give back a  value of a function to the caller while the print is mainly use to display output especially strings and ints, return is reusable because of the holding of function values and giving of function values back when needed especially when a function is called.

5. local variable is the variable that is defined inside a function and that is only usable inside that function, it can't be accessed outside the function where it is define and after a function is called the variable is no longer accessible. 
fuction scope simply means where a defined variable can be accessed or used.

6. Python module is a part of python library that aids in the importation of reusable functions that has reusable features bult-in into it.
`main.py` and `utils.py` may have different responsibilities becasuse the utils.py file is likely to be used hold reusable functions that have different tasks that can be imported to  another file and even main.py file as module while the main.py file is mainly used to orgainise the project code and it is where the reusable defined fuctions on utlis.py file is mainly called and used.

7. `if __name__ == "__main__":` This is a conditional expression that simply tells python to run the code in a file when the file is directly executed but not imported.

8. File modes `r`: is used to read a JSON or TEXT file, `w`: it is also used to wirte a JSON or TEXT filea file  and it can overwrite a file if the file already has content, and `a`: is used to append a text on a file that has already has had some content. w can be dangerous because it opens a file for writing and overwrites any existing content.

9. JSON is javascript object of notation, it consists an array of objects that is used to structure data.
## syntax: json ---->   true
##    ""   python --->  True.
`json.load()`: this expression is used to load json data in file into a python object. while  `json.loads()` is used to convert a python object into a json data.

10. how you would read a traceback in a multi-file project: A traceback should be read in a way that will eb convinent on multi-file project by reading the last line of the traceback exception and the line of code where the exception might come from and by checking and debugging across files and even where function calling is done.

Mention the final exception line and a relevant frame from your own code: 


# WEEK 4 Section C — Code Tracing and Reasoning

# Section C — Code Tracing and Reasoning

**15 marks: 5 questions, 3 marks each**

Write the exact output and explain briefly.

## C1. Definition, call, and return

```python
def double(number):
    return number * 2

result = double(6)
print(result)
```
## exact output
12

## Brief explaination
The function is returning the double of the parameter passed to it, so the argument which is six is been doubled





## C2. Default and keyword arguments

```python
def get_status(score, pass_mark=50):
    if score >= pass_mark:
        return "Pass"
    return "Fail"

print(get_status(60))
print(get_status(score=60, pass_mark=70))
```
## exact output
PASS
FAIL

## Brief explaination
The function has return keyword but on the first function call the argument met the function condition criteria and one value is returned and on the second function calling the argument didn't meet the function condition criteria due to the keyword argument that overshadowed the default parameter then the other value is returned




## C3. `print()` versus `return`

```python
def show_average(a, b):
    print((a + b) / 2)

result = show_average(10, 20)
print(result)
```

## exact output
15
None

## Brief Explaination
The print function does'nt return any value to the function, it displays the value.  and that's why the result variable has a none value,



## C4. Importing from another module

Assume `utils.py` contains:

```python
def calculate_average(a, b):
    return (a + b) / 2
```

And `main.py` contains:

```python
from utils import calculate_average

average = calculate_average(70, 90)
print(average)
```

What does running `main.py` print?


## exact output
What does running `main.py` print?: it prints 80 as the average.


## Brief Explaination
it is because the `utils.py` contains the defined function that performs the average calculating task, while the `main.py` imports it and prints the average.

## C5. JSON string parsing and exception flow

```python
import json

text = '{"name": "Ada", "active": true}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Bad JSON")
else:
    print(data["name"])
    print(data["active"])
finally:
    print("Finished")
```

---

## Exact output 
Ada
true
Finished

## Brief Explaination
The code tried to catch every exception relating to json and prints it to the user in a friendly way if any and print the data on the json file.


# WEEK 4 Section D — Debugging, Files, JSON, and Modules

**15 marks: 5 questions, 3 marks each**

For each question:

- identify the problem;
- name the error type or logic issue where appropriate;
- write a corrected version.




## D1. A function that cannot be reused as intended

```python
def calculate_average(a, b, c):
    print((a + b + c) / 3)

average = calculate_average(70, 80, 90)

if average >= 50:
    print("Pass")
```


## ERROR NAMING:
A function that does prints a value rather returning the value.


## CORRECTED VERSION:
```python
def calculate_average(a, b, c):
    return((a + b + c) / 3)

average = calculate_average(70, 80, 90)

if average >= 50:
    print("Pass")
```

## D2. Local scope mistake

```python
def build_message(name):
    message = f"Hello, {name}"

build_message("Ada")
print(message)
```

The programmer wants to print the message outside the function.


## ERROR NAMING:
Invalid variable scope: defining a variable inside a function


## CORRECTED VERSION:
```python
def build_message(name):
    return(f"Hello, {name}")

message = build_message("Ada")
print(message)
```





## D3. Import failure

Project structure:

```text
student_analyzer/
├── main.py
└── utils.py
```

`utils.py` contains:

```python
def calculate_average(student):
    return (student["math"] + student["english"] + student["science"]) / 3
```

But `main.py` contains:

```python
from utils import average
```

Explain the likely problem and correct the import.


## ERROR NAMING:
The problem on the import is that the fuction name on the import module is not clearly specified

## CORRECTED VERSION:
Project structure:

```text
student_analyzer/
├── main.py
└── utils.py
```

`utils.py` contains:

```python
def calculate_average(student):
    return (student["math"] + student["english"] + student["science"]) / 3
```

But `main.py` contains:

```python
from utils import calculate_average
```




## D4. Wrong file mode

The program should add a new log entry **without deleting previous entries**:

```python
with open("learning.log", "w", encoding="utf-8") as file:
    file.write("Week 4 completed\n")
```

Explain the problem and correct it.

## ERROR NAMING:
The problem is that the file mode is not the appropiate one to do th expected because the file mode "w" will overwrite the file content if any and it is dangerous. the file mode "x" is the most suitable.

## CORRECTED VERSION:
The program should add a new log entry **without deleting previous entries**:

```python
with open("learning.log", "x", encoding="utf-8") as file:
    file.write("Week 4 completed\n")
```



## D5. Missing file and malformed JSON are handled too broadly

```python
import json

try:
    with open("data/students.json", "r", encoding="utf-8") as file:
        students = json.load(file)
except:
    print("Something went wrong")
```

Rewrite the exception handling so that a missing file and malformed JSON produce **different, specific messages**.

## ERROR NAMING:
The problem is how the missing file and the malformed json exception is handled
## CORRECTED VERSION:
```python
import json

try:
    with open("data/students.json", "r", encoding="utf-8") as file:
        students = json.load(file)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("The file data is malformed")
```
# Section E — Practical Coding Task

```python


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


```
