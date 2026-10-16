# Stone Lines: Arena — Week 6 Prepared Edition

A two-player terminal strategy game based on the student's Week 5 Stone Lines application. The game is preserved while its engineering foundation has been prepared for Week 6's study of **decision-making and rule-based AI**.

**Current status:** Human vs Human works. Random Computer and Rule-Based Computer options are intentionally unfinished until the student completes the upcoming Week 6 assignments.

## 1. Before you start

Read these documents in order:

1. [`docs/CODEBASE_CHANGES.md`](docs/CODEBASE_CHANGES.md) — what was changed from your original Week 5 version and why.
2. [`docs/ARCHITECTURE_AND_API.md`](docs/ARCHITECTURE_AND_API.md) — what each file does, how actions work, and where Week 6 strategies belong.
3. [`docs/VERIFICATION.md`](docs/VERIFICATION.md) — what has been tested and what is intentionally unfinished.

Your original learning notes are copied unchanged under `prior_notes/`. They are optional background, not new assignments.

## 2. Requirements

- Python **3.11 or newer**.
- A terminal (Fedora terminal is suitable).
- `rich` and `pytest`, installed from `requirements.txt`.

## 3. Install and run on Fedora/Linux

Open a terminal inside this `stone-lines-arena/` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

If `venv` is unavailable, install the appropriate Python virtual-environment support from your distribution.

### Run the tests

```bash
python -m pytest -q
```

Run tests from the project root; the `pytest.ini` file defines the `tests/` location.

### Run using an absolute path

```bash
python /full/path/to/stone-lines-arena/main.py
```

Statistics are resolved from the project folder, not from the terminal's current working directory.

## 4. Gameplay

Stone Lines has nine positions. Each player has three stones.

- **Placement:** X begins. Players alternate placing one stone at an empty position. A player wins on forming a full row, column, or diagonal.
- **Movement:** If six legal placements finish without a winner, players move one of their own stones into an empty directly connected position. Three in a line wins.
- During a match, type `help` to see the rules or `quit` to cancel without recording statistics.
- After a completed match you may play again; statistics are stored locally.

### Modes available on the menu

| Mode | At Stage 1 | Why |
|---|---|---|
| Human vs Human | **Complete** | Original gameplay preserved and improved |
| Human vs Computer — Random | Prepared but **not implemented** | Week 6 strategy task |
| Human vs Computer — Rule-Based | Prepared but **not implemented** | Week 6 strategy task |

The menu exposes future options so their integration points are ready. If selected, the program allows the human's first move, then reports that the computer strategy has not yet been implemented. This is expected until the relevant tasks are completed.

## 5. Folder guide

```text
stone-lines-arena/
├── main.py                   Application entry point
├── stone_lines/
│   ├── __init__.py            Python package definition
│   ├── app.py                 Menus, turns, match coordination
│   ├── game.py                Board state, legal actions, rules
│   ├── player.py              Player identity
│   ├── constants.py           Winning lines and connections
│   ├── ui.py                  Rich presentation and human input
│   ├── storage.py             Statistics JSON persistence
│   └── computer.py            UNFINISHED Week 6 strategy tasks
├── tests/                    Tests of prepared infrastructure
├── data/statistics.json      Fresh, empty statistics file
├── docs/                     Detailed technical explanations
├── prior_notes/              Original student's notes (unaltered)
├── requirements.txt          Installable package requirements
├── pytest.ini                Test configuration
└── .gitignore                Excludes virtual environments, caches, stats
```

## 6. What you are not expected to redo

You do **not** need to rewrite the game engine, redesign the terminal UI, move classes to new files, repair JSON file paths, or clean up the old project before starting Week 6. Those preparations have been completed for you.

You **will** implement the actual decision-making strategies after the readings and project instructions are provided. The exact task-by-task implementation contract is now in `student/03_PROJECT/` of the supplied learning package.

## 7. Original work and statistics

This codebase is derived from the submitted `01-python-foundations-master.zip`. The original ZIP remains the source-of-truth historical copy. Its personal player statistics have **not** been bundled into the prepared distribution; the provided statistics file begins with `{}`.

To preserve the old records, keep the original ZIP. If you later import records into the new schema, make a backup first; old records may not have the new `draws` field, which is supported automatically when players are updated.

## Week 6 teaching package

For the exact reading order, tasks and milestone checks, begin at `../../START_HERE.md` in the **student distribution folder**. Do not edit the distributed starter itself; copy it into your own working directory at Task 00.
