# Implementation Rules — Read Before Editing Code

This file is part of the assessment contract, not optional advice.

## Where the code goes
- **Exactly one strategy module:** `stone_lines/computer.py`.
- **Required function signatures:** do not rename them or change parameters.
- **Testing file:** create or extend `tests/test_computer.py` for your own readable tests; the supplied gate tests already live in `challenge_tests/`.
- **Other files:** do not modify unless your teacher has explicitly authorized a compatibility correction.

## Action format and indexes
- Screen positions: 1–9. Internal indexes: 0–8.
- Placement: `('place', target_index)`.
- Movement: `('move', source_index, target_index)`.
- Preserve tuple types, not lists/dictionaries.
- Return only an existing legal action or `None` where specified.

## What the engine owns
- `game.get_legal_actions()` — stable ordered list of allowed actions.
- `game.preview_action(action)` — returns independent state after one action.
- `game.copy()` — returns independent state before any action.
- `game.apply_action(action)` — mutates the **real** game and enforces rules. **Do not call from a strategy.**

## What a strategy is forbidden to do
Do not prompt with `input()`, print, import/use Rich, save files, alter the original `game.board`/`current_player`, bypass legality checks, or build a second rules engine. You may change a copied/simulated game snapshot where the task calls for it.

## Deterministic choice rules
- First matching win in `get_legal_actions()` order.
- First safe block in the same order.
- First tied highest positive heuristic score.
- Random fallback only when no positive heuristic exists.
- `None` if no legal action exists.

## Exact heuristic
For a legal candidate, preview it. If it wins, return **100**. Otherwise sum **+4** per unblocked line with two active stones and one empty position; **+1** per unblocked line with one active stone and two empties; add **+2 once** if the active player occupies index 4 after the action. Any line containing opponent stone contributes zero. Illegal actions raise `ValueError`. Values are integers.

## Exact threat definition
The blocking helper acts only if the opponent **could win in one legal action if given a turn before our move**. It should return the first action that removes **every immediate winning reply** available after it. If there is no existing threat, or no complete defensive action exists, return `None`.

A copied game may temporarily set `current_player` to the opponent to inspect hypothetical replies; the original must not change. This is a bounded one-action analysis—not recursion.

## Testing workflow
From **your working copy's project root**:

```bash
python -m pytest -q
python -m pytest -q challenge_tests/test_gate1_random.py
```

After subsequent tasks, run the corresponding named gate test; then rerun all completed stage tests. The default test suite intentionally excludes `challenge_tests/` because unfinished tasks should not fail the infrastructure baseline before you reach them.

Do not modify supplied tests to turn a failure into a pass. Fix the implementation or ask your teacher to review an unclear requirement.

## Help rule
Try reasoning, notes and official Python documentation first. Then request questions/hints, not completed code. Record the difficulty and your eventual explanation in your notebook.
