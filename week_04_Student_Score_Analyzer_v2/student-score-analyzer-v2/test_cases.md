    ## normal 10-student valid JSON;
    2. empty JSON list [];
    3. missing students.json;
    4. malformed JSON;
    5. record missing the math key;
    6. record with a score stored as a string;
    7. all students passing;
    8. all students failing;
    9. tie for best score;
    10. report folder missing before run.





# Test Cases

## 1. Normal 10-student valid JSON
Setup: `students.json` contains 10 valid student records, and each record has all required marks.
Expected: The program loads the data successfully, calculates the averages, generates the report, and saves it to `reports/report.txt`.

## 2. Empty JSON list
Setup: `students.json` contains an empty list: `[]`
Expected: The program detects that there are no students, shows an empty-data message `."Student data is really empty."`., and stops safely.

## 3. Missing `students.json`
Setup: The file `data/students.json` does not exist.
Expected: The program shows a clear file-not-found message "Could not find student data at `/home/kachy/Desktop/Nwachukwu_file/Python_project/Ai-engineering/week04/student-score-analyzer-v2/data/students.json"`. and exits without crashing.

## 4. Malformed JSON
Setup: `students.json` contains invalid JSON syntax.
Expected: The program shows a JSON decode error message and stops safely.

## 5. Record missing the `math` key
Setup: One student record does not have the `math` field.
Expected: The program handles it by identifying the exact error `KeyError: 'math'`

## 6. Record with a score stored as a string
Setup: One score is written as a string, such as `"85"` instead of `85`.
Expected: The program reports invalid input and typerror indicated "`TypeError: can only concatenate str (not "int") to s"`

## 7. All students passing
Setup: All students have averages above the passing threshold.
Expected: The report shows every student as passing and still includes the class average, best student, and weakest student.

## 8. All students failing
Setup: All students have averages below the passing threshold.
Expected: The report shows every student as failing and still generates the summary correctly.

## 9. Tie for best score
Setup: Two or more students have the same highest average.
Expected: The program handles the tie in a consistent vague way

## 10. Report folder missing before run
Setup: The `reports/` folder does not exist before the program runs.
Expected: The program shows a clear error indicating `"FileNotFoundError`: [Errno 2] No such file or directory: `'/home/kachy/Desktop/Nwachukwu_file/Python_project/Ai-engineering/week04/student-score-analyzer-v2/reports/report.txt'`

