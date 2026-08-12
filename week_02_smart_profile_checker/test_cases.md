### empty name

-Input used: empty text input
-Expected result: friendly message
-Actual result: Name cannot be empty
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: good
-What I changed if it failed: none

### Name containing spaces only

-Input used: spaces input
-Expected result: friendly message
-Actual result: Name cannot be empty
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: good
-What I changed if it failed: none

### Age entered as abc:

-Input used: "ABC" => input
-Expected result: friendly message
-Actual result: Age must be a whole number
-Pass or fail: pass
-Exception raised internally, if any: ValueError
-How the program handled it: good
-What I changed if it failed: none

### Age entered as 15.5

-Input used: "15.5" => input
-Expected result: friendly message
-Actual result: Age must be a whole number
-Pass or fail: pass
-Exception raised internally, if any: ValueError
-How the program handled it: good
-What I changed if it failed: none

### Age entered as 0

-Input used: "0" => input
-Expected result: friendly message
-Actual result: Error message: Please enter number between 5 and 100
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: good
-What I changed if it failed: none

### Age entered as -5

-Input used: "-5" => input
-Expected result: friendly message
-Actual result: Error message: Please enter number between 5 and 100
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: good
-What I changed if it failed: none

### Age entered as 5:

-Input used: "5" => input
-Expected result: friendly message
-Actual result: it proceeded to the next prompt
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: good
-What I changed if it failed: none

### Age entered as 100

-Input used: "100" => input
-Expected result: friendly message
-Actual result: it proceeded to the next prompt
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: good
-What I changed if it failed: none

### Age entered as 101

-Input used: "101" => input
-Expected result: friendly message
-Actual result: Error message: Please enter number between 5 and 100
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: good
-What I changed if it failed: none

### Study hours entered as two:

-Input used: "two" => input
-Expected result: conversion failure should be handled
-Actual result: daily study time must be a whole number
-Pass or fail: pass
-Exception raised internally, if any: valueError
-How the program handled it: Raised exection error
-What I changed if it failed: none

### Study hours entered as 0:

-Input used: "0" => input
-Expected result: a range message appears and the prompt repeats.
-Actual result: Error message: Please enter number between 1 and
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: Raised error message
-What I changed if it failed: none

### Study hours entered as 12:

-Input used: "12" => input
-Expected result: the prompt repeats.s.
-Actual result: Error message: Goal cannot be empty
-Pass or fail: pass
-Exception raised internally, if any: none
-How the program handled it: Raised error message
-What I changed if it failed: none

### Press Ctrl+C:

-Input used: " Ctrl+C" => input
-Expected result: the program exits with a cancellation message
-Actual result: Error message: Profile creation cancelled by the user
-Pass or fail: pass
-Exception raised internally, if any: KeyboardInterrupt
-How the program handled it: Raised KeyboardInterrupt execption
-What I changed if it failed: none

EXcercise 8:
For this code:
age_text = "sixteen"
age = int(age_text)

Write:
• the exception type; ValueError
• the operation that failed; it tried to convert the age_text "sixteen" string to int
• the incorrect assumption; it assumed that input text is a literal integer
• one suitable fix. re-raise a valuerror and retry the prompt.

### Exercise 9: Debug a logic error

age = 19
if age >= 13 or age <= 19:
print("Teen learner")

Explain why the condition is wrong and fix it.

it is wrong because of the conditional error (OR) on the code it should be (AND) for the condition to be true in other to serve both case and print("Teen Learner").
It can be solved by changing the conditional syntax (or) to (and).
