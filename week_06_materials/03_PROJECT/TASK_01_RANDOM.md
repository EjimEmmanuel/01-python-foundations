# Task 01 — Choose a Random Legal Action

**Required reading:** Chapters 2–3. **Prerequisite:** Task 00 approved.

**Only implementation file:** `stone_lines/computer.py`.

**Required function:** `choose_random_action(game)`.

## Contract
- Input: a `Game` object whose state must remain unchanged.
- Output: one tuple from `game.get_legal_actions()`; `None` if that list is empty.
- No printing, prompting, game execution or hard-coded board indexes.

## Follow this implementation order
1. Import Python's standard `random` module at the top of `computer.py`.
2. Within the required function, call `game.get_legal_actions()` **once** and store the list.
3. If the list is empty, immediately return `None`.
4. Otherwise return the result of `random.choice(actions)`.
5. Do not call `apply_action()` or edit the board.
6. Create at least one own test in `tests/test_computer.py`; check returned action is legal and the input board is unchanged.
7. Run the supplied gate test, then all original infrastructure tests.

## Acceptance examples
- Beginning of a match: a placement tuple with index 0–8.
- Movement phase: an allowed `('move', source, target)` tuple.
- Finished match: `None`.

**Commands:**
```bash
python -m pytest -q challenge_tests/test_gate1_random.py
python -m pytest -q
```

**Do not move forward until:** student test and gate test pass; teacher can ask why `random.choice([])` is unsafe and why randomness must operate only on legal choices.

**Commit:** `feat: choose random legal computer action`.
