# Week 6 Git Workflow

Week 6 is part of the course's `main` branch, alongside the earlier weekly folders. The project lives in `week_06_stone_lines/`; its code is at that folder's root and all lessons and assessment materials are grouped in `week_06_stone_lines/week_06_materials/`.

## Start

Clone the repository and update the course branch:

```bash
git clone https://github.com/EjimEmmanuel/01-python-foundations.git
cd 01-python-foundations
git switch main
git pull --ff-only
cd week_06_stone_lines
```

If the repository is already cloned:

```bash
git fetch origin
git switch main
git pull --ff-only
cd week_06_stone_lines
```

Begin with `week_06_materials/START_HERE.md`. Complete all readings and the knowledge check, then wait for teacher approval before editing code.

## Work and commit

The application is at the root of the `week_06_stone_lines/` folder. From there, implement the Week 6 strategies in `stone_lines/computer.py`, add student tests in `tests/test_computer.py`, and update `README.md` at release. Keep the prepared engine, UI, storage, constants and supplied tests unchanged.

Commit each completed task and push the same branch:

```bash
git add stone_lines/computer.py
git commit -m "feat: add random legal move strategy"
git push origin main
```

At Task 06, include your own tests, the README update and your reflection at `week_06_materials/05_ASSESSMENT/REFLECTION.md`. Keep the course readings and supplied gate tests unchanged.
