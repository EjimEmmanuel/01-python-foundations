# START HERE — Week 6 Student Navigation

**Week 6: Decision-Making and Rule-Based AI**

Read [`GIT_WORKFLOW.md`](GIT_WORKFLOW.md) for the branch setup. The prepared Week 6 codebase is at the repository root, and all Week 6 learning materials are together in this folder. Complete the reading stage and receive teacher approval before editing code.

This folder contains the complete Week 6 reading path, exercises, fixed project tasks, prior learning notes and assessment instructions. No teacher answers or finished strategies are included here.

## First: know what is inside the folder

| Folder/file | Contents | When to use it |
|---|---|---|
| `START_HERE.md` | The complete navigation map you are reading | First; return when unsure |
| `01_READINGS/READING_MAP.md` | Reading order and study method | Before chapter 1 |
| `01_READINGS/01_...` through `07_...` | Seven self-contained lessons on decisions, states, random strategies, rule systems, heuristics, agents and ML distinction | Read in numeric order |
| `01_READINGS/REFERENCES.md` | Official references and optional follow-up study | During the readings; focus on specified sections |
| `02_PRACTICE/PREPROJECT_WORKED_EXAMPLES.md` | Non-game examples and independent exercises | After readings 1–7; before knowledge check |
| `02_PRACTICE/KNOWLEDGE_CHECK.md` | Assessment of concepts before programming | After all readings and examples |
| `03_PROJECT/PROJECT_OVERVIEW.md` | What the Stone Lines update must deliver | **Only after teacher approves knowledge check** |
| `03_PROJECT/IMPLEMENTATION_RULES.md` | Mandatory architecture, action representation, scoring, tie-breaks and restrictions | Read before Task 00 and keep open during coding |
| `03_PROJECT/TASK_00...TASK_06` | Seven ordered tasks with exact file/function requirements | Complete **one at a time** |
| `03_PROJECT/FINAL_ACCEPTANCE_CHECKLIST.md` | Final functionality and structure checks | After Task 06; preview before project work |
| `04_CODEBASE_GUIDES/` | Code changes, architecture/API and verification guides | Read during Task 00 |
| [`../README.md`](../README.md) (repository root) | Prepared working application; AI strategies intentionally unfinished | Inspect after the reading stage; edit only as the project tasks allow |
| `prior_notes/` | Your earlier Stone Lines learning notes | Optional reference |
| `05_ASSESSMENT/REFLECTION.md` | Final explanation of what you learned and built | After final demonstration |

## Stage A — Read and understand

1. Open `01_READINGS/READING_MAP.md`.
2. Read Chapters **01, 02, 03, 04, 05, 06, 07 in that exact order**. Keep a notebook; answer chapter questions.
3. Read `01_READINGS/REFERENCES.md` for focused official-source review. These links are supplementary; the provided chapters are required.
4. Work through `02_PRACTICE/PREPROJECT_WORKED_EXAMPLES.md`, including its independent exercises.
5. Complete `02_PRACTICE/KNOWLEDGE_CHECK.md` and discuss your answers with the teacher.
6. **Stop here until the teacher says the reading stage is complete.**

## Stage B — Prepare the existing project (not a rebuild)

7. Open `03_PROJECT/PROJECT_OVERVIEW.md` and `03_PROJECT/IMPLEMENTATION_RULES.md`.
8. Open `03_PROJECT/TASK_00_ORIENTATION.md`. It guides you through the codebase at the repository root, its technical documents, dependency setup and baseline checks.
9. Keep all Week 6 code in this repository. Do not change the game engine, UI, storage, constants or supplied tests.

## Stage C — Implement in order

10. Task 01: random chooser → run Gate 1 tests → get teacher sign-off.
11. Task 02: immediate win → run Gate 2 tests → sign-off.
12. Task 03: immediate defence → run Gate 3 tests → sign-off.
13. Task 04: heuristic score → run Gate 4 tests → sign-off.
14. Task 05: combine priority strategy → run all five gate test files → sign-off.
15. Task 06: full application demonstration, own tests, README, Git history → final sign-off.
16. Complete `05_ASSESSMENT/REFLECTION.md`.

**Do not skip ahead or write all five functions at once.** There is a reason each task builds on the previous one.

## What the project folders inside the codebase mean

At the repository root:

| File/folder | Purpose | Edit for Week 6? |
|---|---|---|
| `main.py` | Start the application | No |
| `stone_lines/app.py` | Match/menu integration for human and computer modes | No |
| `stone_lines/game.py` | Shared rules, legal actions, action application and preview | No |
| `stone_lines/player.py` | Player representation | No |
| `stone_lines/constants.py` | Winning lines and board connections | No |
| `stone_lines/ui.py` | Rich interface and human prompts | No |
| `stone_lines/storage.py` | JSON match statistics | No |
| **`stone_lines/computer.py`** | Five strategies and specified private helper | **YES** |
| `tests/` | Existing tests; add your own `test_computer.py` | Yes, new test file only |
| `challenge_tests/` | Provided gate-specific verification tests and helper; run them separately | No, do not edit |
| `week_06_materials/04_CODEBASE_GUIDES/CODEBASE_CHANGES.md` | What the teacher prepared and why | Read, do not edit |
| `week_06_materials/04_CODEBASE_GUIDES/ARCHITECTURE_AND_API.md` | Exact game/strategy contracts | Read, do not edit |
| `data/statistics.json` | Local match data created by the application | Let application manage |
| `README.md` | Install instructions and application overview | Update after Task 06 |
| `requirements.txt`, `pytest.ini`, `.gitignore` | Dependencies, tests, ignored local files | No |

## How to run tests
After setting up your `.venv`, from the **repository root**:

```bash
python -m pytest -q
```

That runs the existing baseline tests. After Task 01:

```bash
python -m pytest -q challenge_tests/test_gate1_random.py
```

The appropriate later test command is written in each task file. Strategy tests are kept out of the default suite until you reach that stage; this prevents unfinished tasks from appearing as baseline failures.

## Help and integrity
If you get stuck: re-read the relevant chapter; inspect the specified function's API; trace one board on paper; write a failing test; then ask the teacher for a hint. Do not copy the complete reference solution from another person or ask AI to write the whole function. Explain your own submitted code.

## What success looks like
By the end, the game still supports Human vs Human, and now supports Human vs Random and Human vs Rule-Based Computer. Your five decision functions are correct, tested and explainable. **Week 7 is where we will begin exploring future states; do not add that now.**
