"""numbers = [3, 6, 9]

for number in numbers:
    print(number + 1)
"""
"""student = {"name": "Ada", "score": 80}
student["score"] = student["score"] + 5
print(student["score"])
"""

"""students = [
    {"name": "Ada", "score": 80},
    {"name": "Tobi", "score": 45},
]

for student in students:
    if student["score"] >= 50:
        print(student["name"], "Pass")
    else:
        print(student["name"], "Fail")"""
"""
count = 0

while count < 3:
    print(count)
    count = count + 1"""
"""
total = 0
scores = [10, 20, 30]

for score in scores:
    total = total + score

print(total)
"""
"""
DRILL 1
items = ["bread", "milk", "rice", "eggs"]
print(f"first item: {items[0]}")
print(f"last item: {items[3]}")
items.append("beans")
print(items)
print(f"number of items: {len(items)}")
for item in items:
    print(f"- {item}")"""


"""
DRILL 2
student = {"name": "Ada", "age": 20, "city": "New York", "learning_goal": "Data Science"}
print(f"{student['name']} is {student['age']} years old. He lives in {student['city']} and wants to achieve his learning goal of {student['learning_goal']}.")
"""

from more_itertools import only

"""
DRILL 3
scores = [44, 72, 58, 91, 39, 65]
count = 0
for _ in scores:
    if _ >= 50:
        print("score:", _)
        count += 1
print("Passed:", count)
"""

"""
DRIll 4
students = [
    {"name": "Ada", "age": 20, "city": "New York", "learning_goal": "Data Science"},
    {"name": "emmanuel", "age": 22, "city": "New Orlean", "learning_goal": "physical Science"},
    {"name": "chidera", "age": 18, "city": "Goshen Estate", "learning_goal": "Medical Science"}
]

search_name = input("Enter student's name: ")
for student in students:
    if student["name"] == search_name:
        print(f"Name: {student['name']} Age: {student['age']} City: {student['city']} learning Goal: {student['learning_goal']}")
        break
else:
    print(f"Student {search_name} not found.")
"""


"""scores = [44, 72, 58, 91, 39, 65]
highest_value = scores[0]
for _ in scores:
    if _ > highest_value:
        highest_value = _
print(highest_value)"""


number = 1

while number <= 5:
    print(number)
    number += 1