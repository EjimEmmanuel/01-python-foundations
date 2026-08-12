# Test Cases

## Test 1 — Normal Dataset

|     Test       |       What you change/check      |       Expected result          |
|----------------|----------------------------------|--------------------------------|
| Normal dataset | Use all 10 valid student records | Report prints without crashing |

### Result

All 10 valid student records were used. The program successfully
processed the data and printed the student report without crashing.

**Status: PASS**

## Test 2 — Clear Top Student

|     Test       |       What you change/check      |       Expected result          |
|----------------|----------------------------------|--------------------------------|
|Clear top student| give one student very high scores | That student becomes best student |

### Result

Ada's subject scores were temporaily changged to the 100 making her to have the average of 100 and ada become the best student. 

The program runs neatly.
**Status: PASS**

## Test 3 — Clear Low Student
TEST: Clear low student
WHAT YOU CHANGE AND CHECK: give one student very low scores
EXPECTED RESULT: That student becomes weakest student and below pass 

### Result

Samuel's subject scores were temporaily changed to 30 making him to have ta very average of 100 and samuel become the weakest student and appear at the below pass. 

The program runs neatly.

**Status: PASS**


## Test 4  — boundary pass
TEST: boundary pass
WHAT YOU CHANGE AND CHECK: Average excatly 50
EXPECTED RESULT: Status should be pass 

### Result

ada's subject scores were temporaily averaged to 50% making her to be at the boundary pass, but the status reflected "pass". 

The program runs neatly.

**Status: PASS**



## Test 5  — just below pass
TEST: below pass
WHAT YOU CHANGE AND CHECK: Average below 50
EXPECTED RESULT: Status should be Fail

### Result

ada's subject scores were temporaily averaged to <50% making her to be at the just below pass, therefore the student's status reflected "Fail". 

The program runs neatly.

**Status: PASS**

## Test 6  — Attendance boundary
TEST: Attendance boundary
WHAT YOU CHANGE AND CHECK: Attendance exactly 75%
EXPECTED RESULT: Attendance alone should not trigger help
### Result

Ada attendance were temporalily changed to 75% making her to be at exactly the attendance boundary, so she didn't appear the students needing help.

The program runs neatly.

**Status: PASS**


## Test 7 — Low Attendance
TEST:  Low attendance
WHAT YOU CHANGE AND CHECK: Attendance 74 with high average
EXPECTED RESULT: Student should still need help
### Result
mariam's attendance were temporalily changed to 74% making her to be at exactly below the attendance boundary, so she did appear at students needing help.

The program runs neatly.

**Status: PASS**

## Test 8 — All pass
TEST:  All pass
WHAT YOU CHANGE AND CHECK: Make every average >= 50
EXPECTED RESULT: Below_pass should be empty
### Result
All's average were temporalily changed to >= 50 making her to be at exactly above the pass boundary, so all wil not appear at students below pass.

The program runs neatly but it does not how a signaling message to inform the user that the below pass is empty.

**Status: FAIL**


## Test 9 — Same top score
TEST:  Same Top Score
WHAT YOU CHANGE AND CHECK: Two students have equal highest average
EXPECTED RESULT: Program should remain stable; note how tie is handle empty
### Result
Program still remain stable

The program does not run neatly until i handled the tie now it is runing properly.

**Status: FAIL**

## Test 10 — Missing key experiment
TEST:  Missing key experiment
WHAT YOU CHANGE AND CHECK: Temporarily remove one science key
EXPECTED RESULT: Observe and explain the resulting KeyError
### Result
it showed a "keyerror" message which shows there is a missing dict-key 
The program runs neatly until it reached to where the erroe is been made then it crased.

**Status: PASS**
		
