# Week 6 Git Workflow

The `week-6-work` branch is the working branch for this project. The prepared Stone Lines application is at the repository root, and all Week 6 lessons and assessment materials are in `week_06_materials/`.

## Start

Clone the repository, then switch to the Week 6 work branch:

```bash
git clone https://github.com/EjimEmmanuel/01-python-foundations.git
cd 01-python-foundations
git switch --track origin/week-6-work
```

If the repository is already cloned:

```bash
git fetch origin
git switch week-6-work
git pull --ff-only
```

Begin with `week_06_materials/START_HERE.md`. Complete all readings and the knowledge check, then wait for teacher approval before editing code.

## Work and commit

The game code is at the repository root. Implement the Week 6 strategies in `stone_lines/computer.py`, add student tests in `tests/test_computer.py`, and update the root `README.md` at release. Keep the prepared engine, UI, storage, constants and supplied tests unchanged.

Commit each completed task and push the same branch:

```bash
git add stone_lines/computer.py
git commit -m "feat: add random legal move strategy"
git push
```

At Task 06, include your own tests, the README update and your reflection at `week_06_materials/05_ASSESSMENT/REFLECTION.md`. Keep the course readings and supplied gate tests unchanged.
