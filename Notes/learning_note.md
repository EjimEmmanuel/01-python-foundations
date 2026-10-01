source .venv/bin/activate

Your finished project will include:

- an object-oriented Stone Lines game engine;
- placement and movement phases;
- winner detection;Placemen_loop
- graph-based movement rules;
- strong input validation;
- a polished terminal interface using Rich;
- player names and session scores;
- JSON-backed all-time statistics;
- automated tests using pytest;
- a virtual environment and dependency file;
- Git commits showing the development history;
- a professional project README.



```text
week-05-stone-lines-arena/
├── README.md
├── PACKAGE_MANIFEST.md
├── project_spec/
├── student/
├── teacher/
└── reference_solution/
```



Read this before Mission 1.

Return to it whenever you are unsure about:

- board positions;
- winning lines;
- placement rules;
- movement rules;
- which positions are connected;
- when the phase changes;
- replay behaviour;
- required game commands.
Do not change the game rules because another design seems interesting. Buildunderlying this version first.
                                                                                            

### `project_spec/ARCHITECTURE_AND_SCOPE.md`

This explains where different responsibilities should eventually live and which features are outside Week 5.

Read it once after `GAME_RULES.md` and revisit it during Mission 5, when you refactor the project into clearer modules.

Do not try to create the final architecture immediately. The project will grow toward it.

---


# 4. Read `WEEK_05_STUDENT_GUIDE.md` before Mission 0

After finishing this file, read:

```text
student/WEEK_05_STUDENT_GUIDE.md
```

### Missions 


## Mission 7 — `07_PERSISTENCE_AND_REPLAY.md`

### Purpose

Reuse your Week 4 JSON knowledge inside a real application.

### Main ideas

- persistence;
- loading JSON;
- saving JSON;
- defensive file handling;
- session versus all-time statistics;
- replay without restarting Python.

### Success means

Completed match results survive after the application closes and reopens.

A missing or malformed statistics file must not crash the whole game.

---

# 3. The `student/` folder is your main learning area

Most of your work this week is guided from the `student/` folder.

It contains:

```text
student/
├── START_HERE.md
├── WEEK_05_STUDENT_GUIDE.md
├── missions/
├── resources/
└── starter/
```

### MAP

```text
week-05-stone-lines-arena/
├── README.md
├── PACKAGE_MANIFEST.md
├── project_spec/
├── student/
├── teacher/
└── reference_solution/
```


```text
student/missions/
├── 00_ENGINEERING_SETUP.md
├── 01_BOARD_AND_STATE.md
├── 02_PLACEMENT_ENGINE.md
├── 03_WINNER_DETECTION.md
├── 04_MOVEMENT_GRAPH.md
├── 05_ARCHITECTURE_REFACTOR.md
├── 06_RICH_UI.md
├── 07_PERSISTENCE_AND_REPLAY.md
└── 08_TEST_BREAK_RELEASE.md
```


# 8. Folders you should not use as normal student material

You may be able to see the following folders in the package:

```text
teacher/
reference_solution/
```

They are intentionally separate from your learning path.



## `reference_solution/`

This contains a complete known-good version of Stone Lines: Arena v1.0.

Do **not** use it while building the project.

Do not open it because you are stuck.

Use the normal help path instead:

```text
think
  ↓
read your code
  ↓
read the current mission
  ↓
check the specification
  ↓
use your notes/resources
  ↓
ask for a teacher hint
  ↓
use AI for coaching if allowed
```



The exact reading and working order

If you are unsure what to do next, follow this sequence.

## Before coding anything

Read, in this order:

```text
1. student/START_HERE.md
2. student/WEEK_05_STUDENT_GUIDE.md
3. project_spec/GAME_RULES.md
4. project_spec/ARCHITECTURE_AND_SCOPE.md
5. student/starter/README.md
6. student/missions/00_ENGINEERING_SETUP.md
```
# 10. How to work through every mission

For every mission, use the same engineering routine.

## Step 1 — Read the mission completely

Do not start typing code after reading only the first paragraph.

Understand:

- the goal;
- the required behaviour;
- the constraints;
- the checkpoint.

## Step 2 — Read the relevant specification

If the mission changes game behaviour, check `GAME_RULES.md`.

If the mission changes structure, check `ARCHITECTURE_AND_SCOPE.md`.

If you are unsure what counts as finished, check the relevant section of `ACCEPTANCE_CRITERIA.md`.

## Step 3 — Design before coding

Before changing the program, answer questions such as:

- What data must change?
- What should stay unchanged?
- Which object or file owns this responsibility?
- What should happen when the action is invalid?
- How will I prove this works?

For larger changes, write brief pseudocode first.

## Step 4 — Build the smallest working version

Do not try to solve the whole remaining project at once.

Implement only the current requirement.

## Step 5 — Test the happy path

Try the normal expected behaviour.

## Step 6 — Test bad input and edge cases

Try to break your own code.

Examples:

- occupied position;
- position 0;
- position 10;
- text where a number is expected;
- moving another player's stone;
- moving to an unconnected position.

## Step 7 — Run automated tests when available

Use pytest once the project reaches the testing stage.

Do not ignore a failing test because the game "seems to work" when played manually.

## Step 8 — Explain the result

Before moving on, make sure you can explain:

- what you changed;
- why you changed it;
- what data changed;
- what rule is being enforced;
- how you tested it.


## Step 9 — Commit the milestone

When a meaningful checkpoint works, commit it to Git with a useful message.

For example:

```text
feat: add placement validation

test: add winner detection tests

refactor: separate game engine from terminal UI
```


## Step 10 — Pass the mission checkpoint

Do not move to the next mission because you are bored with the current one.

Move on when the checkpoint works and you can explain it.

---

# 11. How to use hints without giving away the learning

When you are stuck, do not immediately ask for finished code.

Use this order:

### Hint Level 1 — Question

Ask for a question that helps you think about the problem.

Example:

> What condition am I forgetting to check before moving the stone?

### Hint Level 2 — Direction

Ask which concept, file, or data structure you should inspect.

Example:

> Should this rule be checked in the game engine or the UI?

### Hint Level 3 — Pseudocode

Ask for the logic without finished Python code.

Example:

```text
if destination is not connected to source:
    reject the move
```

Only after serious effort should you review a complete implementation with the teacher.





# 14. Your progress map

Use this as a simple map of the whole week.

```text
START
  │
  ▼
Read START_HERE
  │
  ▼
Read STUDENT_GUIDE + GAME_RULES
  │
  ▼
Mission 0: Engineering setup
  │
  ▼
Mission 1: Board and state
  │
  ▼
Mission 2: Placement engine
  │
  ▼
Mission 3: Winner detection + first pytest tests
  │
  ▼
Mission 4: Movement graph
  │
  ▼
You now have a complete plain game
  │
  ▼
Mission 5: Architecture refactor
  │
  ▼
Mission 6: Rich terminal UI
  │
  ▼
Mission 7: JSON persistence + replay
  │
  ▼
Mission 8: Break it, test it, document it, release it
  │
  ▼
Teacher sign-off + modification challenge
  │
  ▼
Stone Lines: Arena v1.0
  │
  ▼
Old-vs-new reflection
  │
  ▼
DONE
```


# 15. What to do right now

Do these steps now, in order:

1. Finish reading this file.
2. Open `WEEK_05_STUDENT_GUIDE.md` and read it once.
3. Open `../project_spec/GAME_RULES.md` and study the fixed game rules.
4. Open `../project_spec/ARCHITECTURE_AND_SCOPE.md` and understand the boundaries, without trying to build the final structure yet.
5. Open `starter/README.md`.
6. Create your own `stone-lines-arena` working directory from the starter files.
7. Open `missions/00_ENGINEERING_SETUP.md`.
8. Complete Mission 0.
9. Show the checkpoint to your teacher.
10. Only then open Mission 1.

From that point onward, progress through the missions **one at a time and in numerical order**.




## 4. Why a game class is appropriate

One match has values that belong together:

- the board;
- current player;
- current phase;
- count of placed stones;
- winner.

And behaviours operate on those values:

- place a stone;
- move a stone;
- check a winner;
- switch player;
- calculate valid destinations.

A class is useful because it groups one match's state with the behaviours that maintain that state.

This is applied OOP review. The goal is not to make everything a class.

## 5. Invariants

An invariant is something that must remain true while the program runs.

Examples for this game:

- board always has nine cells;
- only X, O, or empty can occupy a cell;
- no player has more than three stones;
- a rejected action leaves important state unchanged;
- movement cannot happen before six stones are placed;
- only the current player's stone can move;
- one legal action changes the turn unless it ends the game.

Thinking in invariants helps you design both validation and tests.



## 8. Separation of concerns

The final project should separate responsibilities.

```text
game.py       → what moves are legal and how state changes
ui.py         → what the player sees and types
storage.py    → how statistics are loaded and saved
constants.py  → fixed rules/data
main.py       → coordinates the application
```


### After coding a feature

Test:

- normal valid case;
- boundary case;
- obvious invalid case;
- state after rejection.

### Before committing

Run:

```bash
pytest -q
```

Then play the affected path manually.


## 15. Recommended Git story

Your commit history should describe progress, for example:

```text
chore: create week 5 project environment
feat: model board and game state
feat: implement placement rules
feat: detect winning lines
feat: add movement graph and legal moves
refactor: separate game engine from terminal ui
style: add rich terminal interface
feat: persist player statistics in json
test: cover placement and movement rules
docs: finish setup and gameplay guide
release: Stone Lines Arena v1.0
```
 winning lines detection, movement graph and legal moves has been added


## 16. Completion standard

You are finished when:

- all required behaviour works;
- tests pass;
- the teacher acceptance check passes;
- README is usable by another person;
- you can explain the major design decisions;
- you can complete the final modification challenge independently.

Proceed through the mission files in order. Do not skip gates because a later feature looks more exciting.






### RULES

## Players-rule

- Two human players play one another.
- One uses `X`.
- One uses `O`.
- Each player owns exactly three stones.
- `X` takes the first turn.


## Phase-rules 1 - Placement
A placement is invalid if:

- the value is not a valid position;
- the chosen position is already occupied;
- placement has already ended;
- the match is already over.

If no player wins during placement, the phase changes to movement immediately after the sixth valid stone is placed. Because turns alternate `X O X O X O` during placement, `X` takes the first movement turn.

## Phase-rules 2 — Movement

A movement is invalid if:

- source or destination is outside 1–9;
- source does not contain the current player's stone;
- destination is occupied;
- source and destination are not directly connected;
- movement has not started;
- the match is already over.


The UI should clearly show:

- the board;
- player names and symbols;
- whose turn it is;
- the current phase;
- session wins;
- useful validation errors;
- valid destinations after a movable source stone is selected.

## Replay and statistics

After a completed match, players may play again without restarting Python.

The application keeps:

- session wins in memory;
- all-time games, wins, and losses in JSON.

A quit before a winner exists does not count as a completed match.
