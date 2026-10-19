# Task 04 — Score Promising Actions

**Required reading:** Chapter 5. **Prerequisite:** Tasks 01–03 passed.

**Only implementation file:** `stone_lines/computer.py`.

**Required function:** `score_action(game, action)`.

## Fixed input/output contract
Input is a `Game` and one action tuple. Return a **Python integer** representing the action's heuristic value. Raise `ValueError` if the action is not in `game.get_legal_actions()`. Do not modify the original game. Do not choose an action in this function—score only the one provided.

## Mandatory implementation sequence
1. Import `WINNING_LINES` from `stone_lines.constants` using a relative import (`from .constants import WINNING_LINES`). Do not duplicate the constant.
2. Check whether `action` is in `game.get_legal_actions()`. If it is not, raise `ValueError` immediately.
3. Save the current player's symbol and opponent's symbol.
4. Build `after = game.preview_action(action)`.
5. If `after` represents a win for the active player, return integer `100` immediately.
6. Initialize `score = 0`.
7. For **each** winning line from `WINNING_LINES`, inspect its three entries in `after.board`.
8. If any entry is the opponent's symbol, add zero for that line and move to the next.
9. Otherwise: if exactly two entries belong to the current player, add `4`; if exactly one belongs to the current player, add `1`; otherwise add zero.
10. If `after.board[4]` belongs to the current player, add `2` **once**, not for each line.
11. Return `score` as an integer.
12. Create tests for the empty-board centre, empty-board corner, illegal action and immediate win.

## Example 1 — Empty board
On an empty board with X to play:
- `('place', 4)` scores **6**: four unblocked one-X lines and +2 centre bonus.
- `('place', 0)` scores **3**: three unblocked one-X lines and no centre bonus.

## Example 2 — Immediate win
With `X X . / O O . / . . .`, the action `('place', 2)` scores exactly **100**. Do not add +4 and +2 to this terminal score.

## Prohibited shortcuts
Do not return a fixed score based only on destination; do not alter `WINNING_LINES`, skip movement actions, change board formats or import UI. Evaluate the full resulting board every time.

**Tests:**
```bash
python -m pytest -q challenge_tests/test_gate4_heuristic.py
python -m pytest -q
```

**Completion gate:** Scores match exact examples; illegal actions raise; real state is unchanged; student can calculate at least one score on paper.

**Commit:** `feat: score legal actions with a simple heuristic`.
