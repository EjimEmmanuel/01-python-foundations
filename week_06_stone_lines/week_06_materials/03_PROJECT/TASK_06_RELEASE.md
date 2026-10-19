# Task 06 — Integration, Verification and Release

**Prerequisite:** Tasks 00–05 have passed. **No new algorithms.**

## Objective
Demonstrate that the strategies written in `computer.py` work inside the existing Stone Lines application and that the old Human vs Human mode still behaves correctly.

## Required sequence
1. Rerun the entire original suite: `python -m pytest -q`. Do not change the supplied tests to make them pass.
2. Rerun all supplied strategy gates: `python -m pytest -q challenge_tests`.
3. Run `python main.py`; select Human vs Computer — Random. Play through a placement game. If it reaches movement, demonstrate a legal computer movement there as well.
4. Repeat with Human vs Computer — Rule-Based. Create or demonstrate an immediate winning or blocking situation and explain the chosen action.
5. Run Human vs Human to confirm the Week 5 mode remains available.
6. Confirm that a completed match stores statistics and that a cancelled match does not record a result.
7. Update your **working copy** of `README.md` with the now-completed modes and a concise description of how the two computer modes choose moves. Do not change the game rules in the README.
8. Create `tests/test_computer.py` with your own readable tests covering all five functions. Some checks may overlap the supplied gate tests; they must reflect your own understanding.
9. Explain one limitation of the rule-based strategy. It can miss a trap that appears more than one move later; that limitation motivates Week 7.
10. Walk through the teacher's viva and the final assessment checklist.

## Required demonstration evidence
- Screenshot or brief transcript of the updated menu and one full computer match.
- Test result showing original and challenge tests passing.
- A readable Git history or at least the milestone commits in your own repository.
- Updated README and brief personal reflection.

## Release naming
**Stone Lines: Arena — Rule-Based Computer Edition.** No claim of unbeatable AI, machine learning or minimax.

## What you must not add
Do not add a new interface framework, database, neural network, random level generator, different rules, new project, additional agent hierarchy or multi-turn search. Finish and explain this release instead.

**Completion gate:** Teacher checks functionality, architecture, test output, understanding and documentation. See `FINAL_ACCEPTANCE_CHECKLIST.md`.

**Commit:** `release: add week 6 rule-based computer modes`.
