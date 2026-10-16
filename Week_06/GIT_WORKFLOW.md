# Week 6 Git Workflow

Week 6 builds on the Stone Lines game from Week 5. The existing `main` branch ends at Week 4, so use the prepared Week 6 branches below.

## Branches

- `master` contains the Week 5 game submitted before Week 6 preparation.
- `week-6` adds the student-only Week 6 lessons and the prepared starter. Treat it as the clean course baseline.
- `week-6-work` starts from that baseline and contains a separate, ready-to-edit copy of the starter at `Week_06/work/stone-lines-arena/`.

The distributed starter at `Week_06/04_STARTER_CODE/stone-lines-arena/` stays unchanged. Make all Week 6 code and test changes in `Week_06/work/stone-lines-arena/`.

## Start

Clone the repository, then switch to the prepared work branch:

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

Read `Week_06/START_HERE.md` and complete the readings and knowledge check first. Begin coding only after the teacher approves the reading stage. The working copy is already placed in `Week_06/work/stone-lines-arena/`; Task 00 still asks you to understand the codebase and run the baseline checks before editing.

## Record progress

Work only in `Week_06/work/stone-lines-arena/`. Keep the prepared starter, teacher materials and supplied gate tests unchanged. Make a small commit at each completed task, for example:

```bash
git add Week_06/work/stone-lines-arena/stone_lines/computer.py
git commit -m "feat: add random legal move strategy"
git push
```

At Task 06, include your own tests, the project README update and your reflection in commits. After teacher review, the `week-6-work` branch can be merged into `week-6`; the earlier course branches remain available as history.
