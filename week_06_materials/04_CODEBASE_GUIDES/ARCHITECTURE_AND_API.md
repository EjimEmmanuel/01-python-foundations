# Architecture and Week 6 Extension Interfaces

This document describes the **prepared application**, not a step-by-step Week 6 assignment. Its purpose is to remove ambiguity about module ownership and function interfaces before the detailed tasks are released.

## 1. Module responsibilities

```text
main.py ──► stone_lines/app.py (menu, turns, match orchestration)
                          │
          ┌───────────────┼──────────────────────┐
          ▼               ▼                      ▼
   stone_lines/ui.py   stone_lines/game.py   stone_lines/storage.py
   Rich + input        state + rules         JSON statistics
                          ▲
                          │ legal actions / apply action
                          │
                  stone_lines/computer.py
                  Week 6 strategy functions
```

**Firm rule:** Only `game.py` decides whether an action is legal or updates the board. A strategy function may inspect a game and return an action. It must not prompt, print, write statistics or directly mutate the board.

## 2. Board indexes and action data

The display labels positions **1–9** for humans. Python internally uses indexes **0–8**.

```text
Screen position:      Python index:
1 --- 2 --- 3         0 --- 1 --- 2
4 --- 5 --- 6         3 --- 4 --- 5
7 --- 8 --- 9         6 --- 7 --- 8
```

Two action representations are supported:

```python
("place", 4)        # Place at screen position 5
("move", 4, 7)      # Move from screen position 5 to 8
```

Actions are ordinary **tuples**; not strings, dictionaries or class instances. This format is a fixed shared contract throughout the project. The UI converts the player's 1–9 input to 0–8 before constructing an action.

## 3. Game API

### `game.get_legal_actions()`

- **Arguments:** none.
- **Returns:** list of action tuples available to the player whose turn it is.
- **Effects:** none; it does not change the game.
- **Placement example:** `[('place', 0), ('place', 3)]`.
- **Movement example:** `[('move', 0, 3), ('move', 4, 7)]`.
- Returns an empty list when the game is already finished or no action is legal.

### `game.apply_action(action)`

- **Input:** one action tuple from the agreed format.
- **Returns:** `None`.
- **Effects:** updates the board, phase, turns and result **when the action is legal**.
- **Failure:** raises `ValueError` for an illegal/malformed action; state remains unchanged.
- Checks victory immediately after a legal action. If the sixth stone was placed without a winner, switches to movement.

### `game.copy()`

- **Input:** none.
- **Output:** separate `Game` object with the same board, players, phase and other state.
- Changes to the copy do not change the original game.

### `game.preview_action(action)`

- **Input:** legal action tuple.
- **Output:** separate `Game` object representing the result of that action.
- **Effects:** none on the original game.
- Raises `ValueError` for invalid actions, without modifying the original.

### Public state fields

```python
game.board            # list of nine display strings or X/O
game.current_player   # 'X' or 'O'
game.phase            # 'placement' or 'movement'
game.stones_placed    # 0..6
game.winner           # 'X', 'O', or None
game.finished         # True or False
game.result           # 'X', 'O', 'draw', or None
game.turns_taken      # number of legal actions applied
```

The AI strategies should **read** these values, not assign to them on the actual match object.

## 4. Computer strategy module — unfinished on purpose

`stone_lines/computer.py` defines the intended Week 6 functions:

| Function | Intended responsibility | Return |
|---|---|---|
| `choose_random_action(game)` | Random legal choice | legal action or `None` |
| `find_winning_action(game)` | Identify an immediate winning choice | legal action or `None` |
| `find_blocking_action(game)` | Prevent a legal immediate opposing win when possible | legal action or `None` |
| `score_action(game, action)` | Assign a heuristic numeric score to a legal action | number |
| `choose_rule_based_action(game)` | Combine priority rules and fallback | legal action or `None` |

In the **student starter**, these functions raise `NotImplementedError`. The complete algorithmic steps, tie-break rules and acceptance examples are in `week_06_materials/03_PROJECT/`. Do not invent extra strategy classes or rewrite the engine.

### Important distinction

A strategy chooses the **action**. `game.apply_action()` applies the action. Keeping those steps separate is necessary to test decisions without playing an entire match.

## 5. UI and application contracts

- `ui.TerminalUI.ask_human_action(game)` returns a valid action but does not execute it.
- `app.select_action(game, mode, ui)` obtains a move from the human or the appropriate computer function.
- `app.play_match(...)` coordinates one match, updates statistics only after a completed game, and handles cancellation.
- `app.run()` controls menu navigation and rematches.

There is no reason for a strategy to import `rich`, `input`, or `storage`.

## 6. What is fixed vs flexible

**Fixed for the course:** file locations, class/method names, function names, signatures, action tuples, player symbols, game rules, and strategy return types.

**Left to the student:** implementing the actual strategy internals as directed by future tasks, writing useful tests, and explaining why actions are selected.

**Not permitted in the Week 6 core:** rebuilding the application, creating a new UI framework, changing game rules, database migration, recursion-based minimax, or ML libraries.
