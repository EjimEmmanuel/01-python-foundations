# Project Name
- Student score analyser.

## What the Project Does
- it analyzes the student score and statictics prints it out on the terminal 

## What Week 4 Concepts It Demonstrates
- Concept: it showed that the students data can be stored in a file as an input data rather than hardcoding it
- Concept 2: it showed that the student output report can also be stored on a report file  as an output data and be printed out in the terminal
- Concept 3: it showed again that helper functions is good to be imported through a module than having a side effect like profoerming other work other than returning a value.
## Project Structure
- `main.py` - main program logic
- `utils.py` - helper functions
- `data/` - input files
- `reports/` - output files

## Requirements
- Python 3.x
- Any other needed libraries or tools

## How to Run It
1. Open the project folder.
2. Run the program --- "python3 main.py"
3. Check the output report.

## Expected Input Data Format
the JSON data format is like the python list of dictionaries but JSON is described as the array of objects.

- JSON	  Python
  object  dictionary
  array	  list
  true	  True
  false	  False
  null	  None
  
## Example Output
==================================================

================== STUDENT SCORE ANALYZER =================

==================================================
1. Ada        Average: 78.00  PASS  
2. David      Average: 61.00  PASS  
3. Zainab     Average: 91.33  PASS  
4. Emeka      Average: 48.67  FAIL  
5. Mariam     Average: 84.00  PASS  
6. Tobi       Average: 43.67  FAIL  
7. Grace      Average: 72.67  PASS  
8. Ibrahim    Average: 57.67  PASS  
9. Chiamaka   Average: 90.67  PASS  
10. Samuel     Average: 66.67  PASS  

## Known Limitations
- Limitation 1
- Limitation 2

## Errors Handled
- JSONDECODERROR
- FileNotFoundError
- Invalid JSON
- keyerror

## What I Learned
- Do not confuse None with:
    • 0;
    • False;
    • "";
    • an empty list.
They are all different values.

- A function can return a value.
A side effect is something extra the function does outside of returning a value.
Printing, writing files, changing variables, and changing lists are side effects.
Side effects are not bad, but they should be used clearly and carefully

- Do not copy Python literals directly into JSON without understanding the syntax.

-  persistent storage includes:
    • text files;
    • JSON files;
    • CSV files;
    • databases;
    • object storage.
