# Week 6 Codebase Changes — What Changed and Why

**Source:** `01-python-foundations-master.zip` (student Week 5 submission)  
**Destination:** repository root (prepared Week 6 baseline)
**Scope:** Engineering preparation and reliability fixes only. No Week 6 AI algorithms are implemented.

## 1. Why we prepared the code

The submitted Stone Lines game already demonstrates working knowledge of Python, classes, game rules, terminal interaction, JSON, and tests. Its core issue for Week 6 was not that the student needed another OOP lesson. The issue was that a significant amount of gameplay was tied directly to input prompts and changes made in `main.py`.

A human can enter a position at a prompt. A computer player needs a way to ask which moves are legal, choose one, and submit it without using a keyboard. The prepared version makes that possible *before* the Week 6 decision-making lessons begin.

This is **not a criticism of the original work**. The changes are a normal step in growing a project beyond its initial requirements.

## 2. File-by-file change map

| Original file | New location | What changed | Why it matters |
|---|---|---|---|
| `main.py` | `main.py` + `stone_lines/app.py` | Moved match, menu and turn coordination out of the entry point; root `main.py` now only calls `run()` | One clear place to coordinate human and computer turns |
| `game.py` | `stone_lines/game.py` | Replaced the prompt-dependent `Game` design with one responsible for state, legal actions, validation, applying actions, winner detection and copying | A computer can inspect and test moves without terminal interaction |
| `player.py` | `stone_lines/player.py` | Kept a simple `Player` class; removed terminal prompting; centralized name/symbol validation | Player identity is separate from how names are collected |
| `constant.py` | `stone_lines/constants.py` | Moved board connections and winning lines to clearly named fixed constants; preserved the original geometry | Rules stay in one shared source |
| `storage.py` | `stone_lines/storage.py` | Added reliable absolute project data path, JSON validation, atomic saving, recorded results for both players, and backwards-compatible default fields | Avoid corrupted statistics and tests that depend on live records |
| `termial_ui/ui.py` + board rendering in `game.py` | `stone_lines/ui.py` | Replaced the one-line Rich demo with a complete display, menu, rules, prompts, validation feedback and replay prompts | A complete interface is ready before AI implementation |
| *(new)* | `stone_lines/computer.py` | Added five named **unfinished functions** with signatures and explanations | Defines where Week 6 decision rules will be written |
| `Tests/test_game.py` | `tests/` | Replaced input-coupled and live-file-dependent tests with isolated tests of the new engine, storage and application | Baseline correctness can be checked without prompts or modifying personal records |
| `Texts/requirements.txt` | `requirements.txt` | Replaced prose/invalid pip entries with installable requirements | `pip install -r requirements.txt` works |
| `README.md` | `README.md` + `week_06_materials/04_CODEBASE_GUIDES/` | Added correct launch commands, structure, rules, boundaries and verification guidance | The student knows how to use the new codebase |
| `Notes/*.md` | `week_06_materials/prior_notes/*.md` | Copied original learning notes **unchanged** | Preserves learning history without making it a new task |
| `data/statistics.json` | `data/statistics.json` (created after the first completed match) | Left the original player data out of the repository | Protects personal records and avoids starting the new package with someone else's match history |

## 3. The most important change — input no longer controls the game rules

### Before

The original application had functions such as `get_placement_position()` and `get_movement_position()` that prompted a person for input. The loops in `main.py` then directly changed `gameClass.board`, incremented `stone_placed`, checked wins and switched turns.

That was understandable for a first human-versus-human game, but it made computer-player integration awkward. A computer should not have to pretend to type into the terminal to make a move.

### After

Three game methods now provide the essential interface:

```python
game.get_legal_actions()         # list legal actions for current player
game.apply_action(action)        # validate and execute action
game.preview_action(action)      # return hypothetical next state
```

A fourth method, `game.copy()`, makes an independent snapshot.

The terminal interface asks humans for an action. In future tasks, `computer.py` will produce an action instead. Both routes go through the **same** `game.apply_action()` method. This prevents the two player types from interpreting the rules differently.

## 4. Game rules that were preserved

- Nine positions on the original connected 3×3 board.
- X plays first; X and O alternate.
- Exactly three stones are placed for each player if nobody wins early.
- A win is any completed row, column or diagonal from the original eight winning lines.
- A legal movement goes from one of the active player's positions to an **empty directly connected** position.
- A win immediately ends the match.
- The player can request another match with the same opponent names.

**Added defensive condition:** if movement offers the next player no legal actions, the engine records a draw instead of getting stuck waiting for input. Under the standard six-stone board configuration this is unlikely; the engine still handles the situation safely.

**Not added:** automatic draw after repeated board states, time limits, unlimited lookahead, minimax, ML, or neural networks. Repetition is relevant to later search lessons; it was intentionally left out of this foundation.

## 5. Improvements to correctness and reliability

**Invalid actions:** All inputs go through a single validation path. An illegal action raises `ValueError` without changing the board, current player, counters, phase or winner. Even boolean and floating-point position indexes are rejected.

**Legal moves:** A new `get_legal_actions()` method covers placement and movement for the active player. It has a predictable return order and never mutates the board.

**Future states:** `copy()` and `preview_action()` safely produce independent snapshots. They allow a later strategy to ask “what if I played this?” without changing the live match.

**Persistence:** A project-relative statistics path avoids failures when the game is launched from another directory. Atomic file replacement reduces the risk of an interrupted write leaving incomplete JSON. Damaged statistics now trigger a clear error instead of silently resetting data.

**Player names:** The original code accepted four-character names but told users that five characters were required. The prepared version consistently requires 4–30 characters, rejects duplicates (case-insensitive), and removes terminal prompting from `Player` itself.

**Test isolation:** Tests create their own temporary statistics files when needed. Running `pytest` does not read or overwrite a student's real statistics JSON.

**Display:** Rich is now the real terminal interface, not a placeholder. The UI is kept outside the game engine so it does not interfere with automated decision making.

## 6. Why the code looks different

The new package uses a `stone_lines/` directory with `__init__.py`. This gives the application clear module boundaries and predictable imports. The underlying object-oriented idea remains familiar: there is still a `Player` class and a `Game` class.

We did **not** add abstract base classes, strategy inheritance trees, advanced decorators, external databases, an event-driven TUI framework, or heavyweight design patterns. The goal was clarity and testability, not showing off architecture.

We also intentionally left the decision strategies as ordinary functions rather than inventing many new classes. That is sufficient for Week 6 and reduces unnecessary cognitive load.

## 7. What was deliberately *not* implemented

These five functions are present in `stone_lines/computer.py` but raise `NotImplementedError`:

```python
choose_random_action(game)
find_winning_action(game)
find_blocking_action(game)
score_action(game, action)
choose_rule_based_action(game)
```

These are not missing infrastructure or unfinished cleanup. They are the intended Week 6 educational work, after the readings and detailed implementation tasks have been delivered.

Computer modes are visible in the menu but are not functional yet. The application reports this cleanly when selected.

## 8. What the student needs to do now

1. **Read** the codebase guide; do not immediately rewrite the files.
2. **Run** Human vs Human and the baseline tests.
3. **Understand** that `app.py` coordinates turns, `game.py` owns rules, `ui.py` handles input/display, and `computer.py` will choose actions.
4. Read `week_06_materials/` and complete its reading stage before implementing strategies.

The teacher should not grade the student on whether they could have independently performed this preparation refactor. This engineering preparation is explicitly provided so the student can focus on decision-making in Week 6.
