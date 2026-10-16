# Task 02 — Detect an Immediate Winning Action

**Required reading:** Chapter 4. **Prerequisite:** Task 01 passed.

**Only implementation file:** `stone_lines/computer.py`.

**Required function:** `find_winning_action(game)`.

## Contract
Return the **first** legal action in stable legal-action order whose previewed outcome immediately wins for `game.current_player`. Return `None` if no such action exists. The actual game must not change.

## Required implementation sequence
1. Save the original current-player symbol from `game.current_player`.
2. Get actions using the engine's legal-action API.
3. Iterate through the actions in the returned order. Do not reorder the list.
4. For each action, create a resulting state using `game.preview_action(action)`.
5. Confirm that the resulting state is finished **and** its `winner` matches the original player.
6. If both hold, return that action immediately.
7. After the loop, return `None`.
8. Add student tests for a known winning board, no win, and no mutation.

## Worked acceptance board

```text
Screen positions:        Stones:
1 2 3                    X X .
4 5 6                    O O .
7 8 9                    . . .
Current player: X
```

Expected returned action: `('place', 2)` (screen position 3).

**Tests:**
```bash
python -m pytest -q challenge_tests/test_gate2_wins.py
python -m pytest -q challenge_tests/test_gate1_random.py challenge_tests/test_gate2_wins.py
python -m pytest -q
```

**Restrictions:** Do not hard-code patterns such as “two X in the top row”; trust preview's winner result. Do not update the real board or print the action.

**Completion gate:** Win and no-win scenarios pass, including a threat for the *other* player not being mistaken for your own win. Student explains why a snapshot is needed.

**Commit:** `feat: detect immediate winning computer actions`.
