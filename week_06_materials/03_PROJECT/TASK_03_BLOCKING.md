# Task 03 — Recognize and Prevent Immediate Threats

**Required reading:** Chapter 4 carefully. **Prerequisite:** Tasks 01–02 passed.

**Only implementation file:** `stone_lines/computer.py`.

**Required public function:** `find_blocking_action(game)`.

**Required private helper:** `_opponent_can_win_immediately(state, opponent)` (in the same module).

## Contract (read twice)
A threat means the opponent, **if allowed to act in the current position**, has a legal one-action win. Return the **first current-player legal action that removes all immediate winning replies**. Return `None` if there is no existing immediate threat, or if no available action removes all such replies. Do not choose a merely partially effective block.

## Mandatory implementation order
1. Define the private helper. It must call `state.copy()` to obtain an independent snapshot.
2. If the copied snapshot is already finished, return `False`.
3. Set `current_player` on **the copy only** to the `opponent` symbol passed in.
4. Iterate the copied game's legal actions. Preview each on the copied game; if any preview's `winner` equals `opponent`, return `True`. Otherwise return `False`.
5. In `find_blocking_action(game)`, obtain the real game's legal actions. If there are none, return `None`.
6. Determine the opponent via `game.opponent(game.current_player)`.
7. Use the helper on the original *input* state (which the helper copies). If no threat exists before our move, return `None`.
8. Otherwise preview each current-player legal action, in the existing list order. If the helper finds **no** immediate opponent-winning reply after that action, return it immediately.
9. If no candidate completely removes the threat, return `None`.
10. Write at least one test proving that the real game state remains unchanged.

## Worked acceptance board

```text
X X .
O X .
. . O
Turn: O; Placement
```

X threatens the top row at screen position 3. Expected defensive action: `('place', 2)`.

## Important edge cases
- **No threat before action:** return `None` even if some moves look sensible.
- **Multiple immediate threats:** if no action neutralizes all of them, return `None`.
- **Sixth placement:** the game may transition to movement, so check resulting replies with the *actual* preview rules; do not assume the next player can still place.
- **A current-player win:** the full strategy checks wins before blocking, so this helper does not control top-level priority.

**Tests:**
```bash
python -m pytest -q challenge_tests/test_gate3_blocking.py
python -m pytest -q challenge_tests/test_gate1_random.py challenge_tests/test_gate2_wins.py challenge_tests/test_gate3_blocking.py
```

**Restrictions:** Do not mutate the real game; do not recursively look ahead or add minimax. Only one opponent response is examined.

**Completion gate:** Teacher can describe two different situations and student correctly says when the helper returns an action versus `None`, without claiming that every threat can be blocked.

**Commit:** `feat: defend against immediate opponent threats`.
