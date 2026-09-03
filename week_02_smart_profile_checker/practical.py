while True:
    name = input("Enter your name: ").strip()
    if not name:
        print("Please enter a valid name")
        continue
    else:
        print(name)
        break
while True:
    age_text = input("Enter a valid age: ")
    ## keep asking for age until the user enters a valid whole number;
    try:
        age = int(age_text)
    except ValueError:
        print("Please Enter a valid digit number")
        continue
    ## reject ages below 5 or above 100;
    else:
        if not 5 <= age <= 100:
            print("Please enter age between 5 and 100")
    ## 11. classify the learner as `Child learner` for age below 13, `Teen learner` for 13–19 inclusive, and `Adult learner` for 20 or above;
        else:
            break
##  ask for daily study hours as a decimal number;
while True:
    daily_study_text = input("Enter your daily study hours: ")
    try:
        daily_hours = float(daily_study_text)
    except ValueError:
        print("Please Enter a valid decimal number")
        continue
    else:
        if not 0.5 <= daily_hours <= 12:
            print("Please enter study hours between 0.5 and 12")
            continue
        else:
            print(daily_hours)
            break
## ask for a learning goal and reject an empty goal;
learning_goal = input("What's your learning goal: ")
if not learning_goal:
    print("Please enter a valid learning goal")

print("--- LEARNER PROFILE ---")
print(f"Name: {name}")
print(f"Age: {age}")
if age < 13:
    print("Category: Child learner")
elif 13 <= age <= 19:
    print("Category: Teen learner")
else:
    print("Category: Adult learner")
print(f"Daily study hours: {daily_hours}")
print(f"Goal: {learning_goal}")
print("Status: Profile accepted")


