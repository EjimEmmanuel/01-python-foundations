# Stone Lines: Arena — Week 6 Prepared Edition

A two-player terminal strategy game based on the student's Week 5 Stone Lines application. The game is preserved while its engineering foundation has been prepared for Week 6's study of **decision-making and rule-based AI**.

**Current status:** Human vs Human works. Random Computer and Rule-Based Computer options are intentionally unfinished until the student completes the upcoming Week 6 assignments.

## 1. Start with the reading guide — do this before coding

Week 6 has two guides. Follow them in this order:

1. **Reading guide:** [`week_06_materials/START_HERE.md`](week_06_materials/START_HERE.md). Complete the seven readings, worked examples, and knowledge check. Discuss the check with your teacher and stop until they approve the project stage.
2. **Project guide:** [`week_06_materials/03_PROJECT/PROJECT_GUIDE.md`](week_06_materials/03_PROJECT/PROJECT_GUIDE.md). Open this only after approval. It explains the project scope and leads through Tasks 00–06 in order.

Do not start the project tasks or edit the code before completing the reading stage and receiving approval. The codebase walkthroughs are in `week_06_materials/04_CODEBASE_GUIDES/`; the project guide tells you when to read them. Your earlier Stone Lines notes are in `week_06_materials/prior_notes/` as optional background.

## 2. Requirements

- Python **3.11 or newer**.
- A terminal.
- `rich` and `pytest`, installed from `requirements.txt`.

## 3. After approval: install, run, and test

Do these setup and baseline-check steps only after you have completed the readings and knowledge check and your teacher has approved the project stage. The game code is at the root of this Week 6 folder. Open a terminal in `week_06_stone_lines/`:

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

Run tests from the Week 6 folder; the `pytest.ini` file defines the `tests/` location.

### Run using an absolute path

```bash
python /full/path/to/01-python-foundations/week_06_stone_lines/main.py
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
week_06_stone_lines/
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
├── data/                     Local statistics, created after a completed match
├── week_06_materials/        All readings, project guides and assessment
├── requirements.txt          Installable package requirements
├── pytest.ini                Test configuration
└── .gitignore                Excludes virtual environments, caches, stats
```

## 6. What you are not expected to redo

You do **not** need to rewrite the game engine, redesign the terminal UI, move classes to new files, repair JSON file paths, or clean up the old project before starting Week 6. Those preparations have been completed for you. The Week 5 project remains in its own weekly folder; this folder contains the Week 6 starter project.

After completing the readings and getting teacher approval, implement the decision-making strategies described in `week_06_materials/03_PROJECT/`.

## 7. Original work and statistics

This codebase is derived from the submitted `01-python-foundations-master.zip`. The original ZIP remains the source-of-truth historical copy. Its personal player statistics have **not** been bundled. Statistics are created locally after a completed match and are ignored by Git.

To preserve the old records, keep the original ZIP. If you later import records into the new schema, make a backup first; old records may not have the new `draws` field, which is supported automatically when players are updated.

## Week 6 guides and materials

All readings, practice, project tasks, codebase guides, prior notes, and assessment instructions are grouped in [`week_06_materials/`](week_06_materials/). Begin with the [reading start guide](week_06_materials/START_HERE.md); after the reading gate and teacher approval, use the [project guide](week_06_materials/03_PROJECT/PROJECT_GUIDE.md). The project code is at this folder's root. The assigned strategy work is in `stone_lines/computer.py`, with student tests added under `tests/`.
