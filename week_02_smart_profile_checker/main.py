"""
name = input("Enter your name: ").strip()
while True:
    age_text = input("Enter your age: ")
    if not name:
        print("Name cannot be empty")
    try:
        age = int(age_text)
    except ValueError:
        print("Age must be a whole number.")
        continue
    else:
        if not 5 <= age <= 100:
            print("Enter a realistic age from 5 to 100.")
            continue
        else:
            print(f"Age accepted: {age}")
            break
"""


def read_input_text(prompt, field_name):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print(f"{field_name} cannot be empty")
        continue


def read_input_int(prompt, field_name, minimum, maximum):
    while True:
        raw_int = input(prompt)
        try:
            int_value = int(raw_int)
        except ValueError:
            print(f"{field_name} must be a whole number")
            continue
        else:
            if not minimum <= int_value <= maximum:
                print(f"Please enter number between {minimum} and {maximum}")
                continue
            return int_value


def validate_score(score):
    while True:
        try:
            score = int(input(score))
        except ValueError:
            print("please score must be a whole number")
            continue
        else:
            if score < 0 or score > 100:
                print("please enter score between 1 and 100")
                continue
        return score


""" recheck the return value"""


def classified_age(age):
    if age <= 13:
        return "Child learner"
    if 13 < age < 19:
        return "Teen learner"
    else:
        return "Adult learner"


def classified_studiness(study_hours):
    if study_hours >= 3:
        return "Strong study availability"
    elif study_hours == 2:
        return "Strong study availability"
    else:
        return "Start small stay consistent"


def main():
    print("=" * 54)
    print("SMART AGE AND PROFILE CHECKER")
    print("=" * 54)
    name = read_input_text("What's your name: ", "Name")
    age = read_input_int("What's your age: ", "Age", 5, 100)
    score = validate_score("What's your total score: ")
    test = read_input_int("number of tests: ", "Test score", 0, 10)
    level = read_input_text("What's your level: ", "class or level")
    interest = read_input_text("What's your interest: ", "Interest")
    goal = read_input_text("What's your goal: ", "Goal")
    study_hours = read_input_int(
        "How many hours do you read a day: ", "Daily study time", 1, 14
    )
    age_group = classified_age(age)
    readiness = classified_studiness(study_hours)
    weekly_readiness = classified_studiness(study_hours * 7)

    print("=" * 54)
    print("STUDENT PROFILE")
    print("=" * 54)
    print(f"Name: {name}")
    print(f"Age: {age}")
    try:
        average = score / test
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Average: {average}")
    finally:
        print("Average calculation attempt completed.")
    print(f"Age Group: {age_group}")
    print(f"Class or Level: {level}")
    print(f"Interest: {interest}")
    print(f"AI Goal: {goal}")
    print(f"Daily Study Time: {study_hours}")
    print(f"Estimated weekly study time: {weekly_readiness}")
    print(f"Readness: {readiness}")
    print("=" * 54)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProfile creation cancelled by the user")
    except EOFError:
        print("\nInput ended before the profile was completed.")
