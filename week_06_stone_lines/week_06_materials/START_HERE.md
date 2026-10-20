# START HERE — Week 6 Student Navigation

**Week 6: Decision-Making and Rule-Based AI**

Read [`GIT_WORKFLOW.md`](GIT_WORKFLOW.md) for the branch setup. The prepared Week 6 codebase is at the root of `week_06_stone_lines/`, and all Week 6 learning materials are together in this folder. Start with Chapters 1–2, then use the project tasks to guide the rest of your reading. You do not have to finish every chapter before the project begins; read, explain, and revisit material as each stage needs it. Teacher checkpoints still apply before you move from one project task to the next.

This folder contains the complete Week 6 reading path, exercises, fixed project tasks, prior learning notes and assessment instructions. No teacher answers or finished strategies are included here.

## First: know what is inside the folder

| Folder/file | Contents | When to use it |
|---|---|---|
| `START_HERE.md` | The complete navigation map you are reading | First; return when unsure |
| `01_READINGS/READING_MAP.md` | Reading order and study method | Before chapter 1 |
| `01_READINGS/01_...` through `07_...` | Seven self-contained lessons on decisions, states, random strategies, rule systems, heuristics, agents and ML distinction | Start with Chapters 1–2; read the chapters named by each task and return as needed |
| `01_READINGS/REFERENCES.md` | Official references and optional follow-up study | During the readings; focus on specified sections |
| `02_PRACTICE/PREPROJECT_WORKED_EXAMPLES.md` | Non-game examples and independent exercises | Use after related chapters or when a concept needs another example |
| `02_PRACTICE/KNOWLEDGE_CHECK.md` | Diagnostic questions to check and revisit understanding | Work through it as you read; review the full check before Tasks 05–06 |
| `03_PROJECT/PROJECT_OVERVIEW.md` | What the Stone Lines update must deliver | With the Project Guide after Chapters 1–2 and teacher kickoff |
| `03_PROJECT/PROJECT_GUIDE.md` | The project entry point, task order, checkpoints and code boundaries | After the initial reading and teacher kickoff; keep using it during the project |
| `03_PROJECT/IMPLEMENTATION_RULES.md` | Mandatory architecture, action representation, scoring, tie-breaks and restrictions | Read before Task 00 and keep open during coding |
| `03_PROJECT/TASK_00...TASK_06` | Seven ordered tasks with exact file/function requirements | Complete **one at a time** |
| `03_PROJECT/FINAL_ACCEPTANCE_CHECKLIST.md` | Final functionality and structure checks | After Task 06; preview before project work |
| `04_CODEBASE_GUIDES/` | Code changes, architecture/API and verification guides | During Task 00: changes guide first, then architecture/API; use verification when checking the baseline |
| [`../README.md`](../README.md) (Week 6 folder root) | Prepared working application; AI strategies intentionally unfinished | Read during Task 00 before the codebase guides; edit only as the project tasks allow |
| `prior_notes/` | Your earlier Stone Lines learning notes | Optional Week 5 background; follow this Week 6 guide and task files for current instructions |
| `05_ASSESSMENT/REFLECTION.md` | Final explanation of what you learned and built | After final demonstration |

## Stage A — Start reading and orient yourself

1. Open `01_READINGS/READING_MAP.md`.
2. Read Chapters **01 and 02** first. Keep notes, answer their questions, and explain the ideas in your own words.
3. With your teacher's kickoff, continue to the Project Guide and Task 00. Task 00 is codebase orientation, not strategy coding.
4. During Task 00, read the Week 6 README, then `04_CODEBASE_GUIDES/CODEBASE_CHANGES.md`, then `ARCHITECTURE_AND_API.md`. The changes guide tells you what the teacher prepared or changed; the architecture guide explains the code and its contracts. Use `VERIFICATION.md` for the baseline check.

## Stage B — Read alongside the project

5. Before each task, read its **Required reading** chapters and explain the relevant ideas. Task 01 calls for Chapters 2–3; Tasks 02–03 call for Chapter 4; Task 04 calls for Chapter 5; Task 05 calls for Chapters 1 and 4–7.
6. Use the worked examples and knowledge check as practice while learning. You may return to a chapter, example, or question whenever you need to strengthen your understanding. The full knowledge check is a review before Tasks 05–06, not a requirement to finish every reading before Task 00 or Task 01.
7. Open `03_PROJECT/PROJECT_GUIDE.md`, `PROJECT_OVERVIEW.md`, and `IMPLEMENTATION_RULES.md` as you begin Task 00; keep them available throughout the work.
8. Keep all Week 6 code in this repository. Do not change the game engine, UI, storage, constants or supplied tests.

## Stage C — Implement in order, returning to the readings

9. Task 01: random chooser → run Gate 1 tests → get teacher sign-off.
10. Task 02: immediate win → run Gate 2 tests → sign-off.
11. Task 03: immediate defence → run Gate 3 tests → sign-off.
12. Task 04: heuristic score → run Gate 4 tests → sign-off.
13. Task 05: combine priority strategy → review the full knowledge check, run all five gate test files → sign-off.
14. Task 06: full application demonstration, own tests, README, Git history → final sign-off.
15. Complete `05_ASSESSMENT/REFLECTION.md`.

**Do not skip ahead or write all five functions at once.** There is a reason each task builds on the previous one.

## What the project folders inside the codebase mean

At the root of `week_06_stone_lines/`:

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
| `04_CODEBASE_GUIDES/CODEBASE_CHANGES.md` | What the teacher prepared and why | Read, do not edit |
| `04_CODEBASE_GUIDES/ARCHITECTURE_AND_API.md` | Exact game/strategy contracts | Read, do not edit |
| `data/statistics.json` | Local match data created by the application | Let application manage |
| `README.md` | Install instructions and application overview | Update after Task 06 |
| `requirements.txt`, `pytest.ini`, `.gitignore` | Dependencies, tests, ignored local files | No |

## How to run tests
After setting up your `.venv`, from the **Week 6 folder root**:

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
