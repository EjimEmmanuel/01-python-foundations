learners = [
    {"name": "Ada", "python": 78, "logic": 82, "project": 74, "attendance": 92},
    {"name": "Tobi", "python": 44, "logic": 39, "project": 46, "attendance": 81},
    {"name": "Mariam", "python": 88, "logic": 84, "project": 91, "attendance": 96},
    {"name": "Emeka", "python": 61, "logic": 58, "project": 63, "attendance": 74},
    {"name": "Zainab", "python": 53, "logic": 57, "project": 55, "attendance": 85},
    {"name": "Chinedu", "python": 35, "logic": 49, "project": 43, "attendance": 69},
    {"name": "Ngozi", "python": 92, "logic": 89, "project": 94, "attendance": 98},
    {"name": "Samuel", "python": 50, "logic": 50, "project": 50, "attendance": 73},
]


""" calculating the learner's average"""
for learner in learners:
    average = (learner["python"] + learner["logic"] + learner["project"]) / 3
    learner["average"] = average

""" assigning `"Pass"` to a learner when average is **50 or above**, otherwise assign `"Fail"`;
"""
for learner in learners:
    if learner["average"] >= 50:
        learner["status"] = "PASS"
    else:
        learner["status"] = "FAIL"
""" Calculating the overall cohort average using an accumulator;
"""

cohort_total = 0

for learner in learners:
    cohort_total += learner["average"]
cohort_average = (cohort_total / 8)

"""find the best learner using a **best-so-far** pattern;
"""
Best_learner = learners[0]
for learner in learners:
    if learner["average"] > Best_learner["average"]:
        Best_learner = learner


"""find the weakest learner using a **weakest-so-far** pattern;
"""
Weak_learner = learners[0]
for learner in learners:
    if learner["average"] < Weak_learner["average"]:
        Weak_learner = learner

""" count how many learners pass and how many fail;
"""
above_pass = 0
below_pass = 0


for learner in learners:
    if learner["average"] > 50:
        above_pass =+ 1
    below_pass =+ 1

""" create a list containing every learner below the pass threshold;
"""
below_pass_threshold = []

for learner in learners:
    if learner["average"] < 50:
        below_pass_threshold.append(learner)

""" create a list containing every learner needing support using this project rule:
"""
needing_support = []
for learner in learners:
    if learner["average"] < 50 or learner["attendance"] < 75:
        needing_support.append(learner)


""" print a clean numbered report using a loop;
"""

print("=" * 50)
print( )    
print("COHORT SCORES ANALYSER")
print()
print("=" * 50)

print(f"Cohort average: {cohort_average:.2f}")
"""best"""
print("The best student is: ")
print(f"{Best_learner["name"]} -- {Best_learner['average']:.2f}")

"""Weak"""
print("The weakeest student is: ")
print(f"{Weak_learner["name"]} -- {Weak_learner['average']:.2f}")
print(f"Pass count: {above_pass}")
print(f"Fail count: {below_pass}")

"""Below  pass threshold"""
print("The students below pass thresshold are: ")
for learner in below_pass_threshold:
    if len(below_pass_threshold) == 0:
        print("There's no student below the pass threshold: ")
    print(f"{learner["name"]} --- {learner["average"]:.2f}")

"""Needing support."""
print("The students needing support are: ")
for learner in needing_support:
    if len(needing_support) == 0:
        print("There's No Student Below The Pass Threshold: ")
    print(f"{learner["name"]} - {learner["average"]:.2f} - {learner["attendance"]}")