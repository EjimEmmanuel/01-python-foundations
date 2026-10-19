# Task 05 — Combine the Rule-Based Strategy

**Required reading:** Chapters 1, 4–7. **Prerequisite:** Tasks 01–04 passed.

**Only implementation file:** `stone_lines/computer.py`.

**Required function:** `choose_rule_based_action(game)`.

## Contract
Return a legal action or `None`. Combine the existing helpers in the **exact required order**; do not rewrite their algorithms inside this coordinator.

## Mandatory implementation sequence
1. Call `game.get_legal_actions()`. If empty, return `None` immediately.
2. Call `find_winning_action(game)`. If it returns a non-`None` action, return that action immediately.
3. Call `find_blocking_action(game)`. If it returns a non-`None` action, return it immediately.
4. For each legal action, call `score_action(game, action)`. Record the score with its action, preserving the legal-action order.
5. Find the **highest** score.
6. If the highest score is **strictly greater than zero**, return the **first** action having that score (stable tie-break).
7. Otherwise call and return `choose_random_action(game)` as the fallback.
8. Verify that the function only returns and never calls `apply_action()`.

## Exact priority

```text
legal actions empty? -> None
else immediate winning move? -> choose it
else effective immediate defence? -> choose it
else highest heuristic > 0? -> first maximum
else -> random legal action
```

No other ordering is accepted. Do not prioritize centre over a win or a block. Do not pick a negative-scoring action when the fallback contract applies.

## Worked examples
- `X X . / O O . / . . .`, X to move: `('place', 2)` because win outranks the other rules.
- `X X . / O X . / . . O`, O to move: `('place', 2)` because defensive action takes precedence.
- Entirely empty board, X to move: `('place', 4)` because the centre scores 6, higher than all other legal placements.
- Finished match: `None`.

**Tests:**
```bash
python -m pytest -q challenge_tests/test_gate5_strategy.py
python -m pytest -q challenge_tests
python -m pytest -q
```

**Completion gate:** All five gate files pass, original application tests pass, priorities are explainable and decision functions do not change the game state.

**Commit:** `feat: combine winning defensive and heuristic rules`.
