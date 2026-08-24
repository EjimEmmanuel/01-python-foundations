"""This is test one"""
def read(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def count_words(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    words = text.split()
    return len(words)


def main():
    text = read("./reports/test.txt")
    character = 0
    for i in text:
        character += 1
    print(f"Total number of characters in the file: {character}")
    lines = text.splitlines()
    print(f"Total number of lines in the file: {len(lines)}")
    print(f"Total number of words in the file: {count_words('./reports/test.txt')}")

if __name__ == "__main__":
    main()



"""This is test two"""

import json



def count_words(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    words = text.split()
    return len(words)


def load_contact(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    try:
        phonebook = load_contact("./data/contacts.json")
    except FileNotFoundError:
        print("Could not find the file data")
        return
    except json.JSONDecodeError as error:
        print(f"could not decode the file due to {error}")
        return
    
    for contact in phonebook:
        print(f"This is {contact["name"]}'s phone number -- {contact["Phone number"]}")

if __name__ == "__main__":
    main()