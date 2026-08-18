    1. Project title — Student Score Analyzer v1.
    2. What it does — it analyzes the students' scores and give summary of the class performances
    3. Concepts practiced — lists, dictionaries, loops, search/filter/count/summaries.
    4. How data is represented — Data is represented by the list of dictionaries.
    5. How to run it —  it is run by using the terminal command "python3 main.py"
    6. Project rules — the rule has a condition that if a student has an average below the pass threshold or an attendance below the attendance boundary, that the student should be added to the list of those that needs help.
7 - example output :
Below is an example of the type of report produced by the program:

 1. Emmanuel   Average:  85.0  Pass  Attendance: 92%
 2. John       Average:  71.7  Pass  Attendance: 88%
 3. Peter      Average:  45.0  Fail  Attendance: 70%
 4. Mary       Average:  90.0  Pass  Attendance: 96%

Best Student: Mary
Weakest Student: Peter

The actual output may vary depending on the student records entered into the program.

## 8. Bugs You Faced

### Bug 1 — KeyError when accessing student data

One of the problems I encountered was a `KeyError` when trying to access a dictionary key that did not exist. For example, if the program tried to access `student["average"]` before the average had been calculated and stored, Python produced a `KeyError`.

I fixed this by making sure that the required information was calculated or added to the student dictionary before trying to display it.

### Bug 2 — Incorrect pass/fail result at the boundary

Another problem involved determining whether a student with an average of exactly 50 should pass. Using `>` instead of `>=` caused a student with an average of exactly 50 to be classified as a failure.

This correctly makes 50 a passing average while anything below 50 remains a failure.

## 9. What I Learned

Through this project, I learned how to work with lists and dictionaries to store and organize student information. I also learned how to use loops to process multiple student records without repeating the same code.

i also learn how to access the dictionary value inside a list
Overall, this project helped me understand how the Python concepts I learned can be combined to build an actual working program.

## 10. Future Improvement

One feature I would like to add in Week 4 or later is **saving and loading student records from a file**.

Currently, the student data can be stored while the program is running, but a future version could save the records to a JSON or CSV file. This would allow the program to keep the students' information even after the program is closed.

I would also like to eventually add features such as searching for a particular student, editing student records, and generating a more detailed class performance report.
