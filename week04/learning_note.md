 ## THINGS I LEARNT

1. Do not confuse None with:
    • 0;
    • False;
    • "";
    • an empty list.
They are all different values.

2. A function can return a value.
A side effect is something extra the function does outside of returning a value.
Printing, writing files, changing variables, and changing lists are side effects.
Side effects are not bad, but they should be used clearly and carefully

3. Common persistent storage includes:
    • text files;
    • JSON files;
    • CSV files;
    • databases;
    • object storage.

4. Do not copy Python literals directly into JSON without understanding the syntax.

5. from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "students.json"
REPORT_FILE = BASE_DIR / "reports" / "report.txt"

6. JSON	Python
object	dictionary
array	list
true	True
false	False
null	None
keys normally use double quotes	Python strings may use single or double quotes

7. Function            	Direction	     Source/destination
json.load(file)	       JSON → Python	file object
json.loads(text)	   JSON → Python	string
json.dump(data, file)	Python → JSON	file object
json.dumps(data)	    Python → JSON	string

8. serialization = saving Python data into JSON form
deserialization = reading JSON back into Python form

9. When a traceback appears:
    #  Read the final line: exception type + message.
    #  Find the first relevant line from your own project near the bottom.
    #  Identify which function was running.
    #  Ask what values/paths entered that function.
    #  Reproduce the failure with the smallest example.
    #  Fix the actual cause.
    #  Run the original scenario again.

10. Debug Prints as Temporary Instruments
- You may temporarily inspect:
- print("Loading from:", DATA_FILE)
- print("Loaded type:", type(students))
- print("Student count:", len(students))
- print("First record:", students[0])


11. WEEK 4 PROJECT RULE:
    Use the same Week 3 training rules unless your teacher changes them:
    • student average = mean of math, English, and science;
    • Pass if average is at least 50;
    • Fail if average is below 50;
    • Needs support if average is below 50 or attendance is below 75.










### finding best_student
def find_best(students):
    best_student = students[0]
    for student in students[1:]:
        if student["average"] > best_student["average"]:
            best_student = student
            return best_student
        elif student["average"] == best_student["average"]:
            win1, win2 = best_student, student
            return win1, win2
### finding weak_student


