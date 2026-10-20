# Project Brief — Stone Lines Computer Opponent

Begin after reading Chapters 1–2 and receiving the teacher's kickoff for Task 00. You do not need to finish all seven readings before starting: each task assigns the chapters to read before that stage, and you should return to them whenever you need to strengthen your understanding. Review the full knowledge check with your teacher before Tasks 05–06.

## Outcome
Extend the **provided** Stone Lines application, not the old Week 5 ZIP. The engine, Rich UI, persistence, menu modes, basic tests and Python package structure are already prepared. Your work is to implement five small decision functions in the existing `stone_lines/computer.py`. The result must support:

- Human vs Human (existing)
- Human vs Random Computer (new)
- Human vs Rule-Based Computer (new)

**The learning focus:** Choose actions using randomness, immediate-win rules, immediate-threat prevention and simple heuristic scoring. You are not writing a new game or training an ML model.

## What you receive
The prepared application is already at the root of `week_06_stone_lines/`. Its strategy functions deliberately raise `NotImplementedError` at the beginning. This is expected.

The original 48 infrastructure tests should pass before you implement anything. The additional gate tests live under `challenge_tests/`; they intentionally do not run during the default baseline test command.

## Your scope
**Edit:** `stone_lines/computer.py`, with student-authored tests in `tests/test_computer.py` and a brief update to `README.md` at release.

**Do not edit without teacher approval:** `game.py`, `app.py`, `ui.py`, `constants.py`, `storage.py`, `player.py`, action formats, tests supplied to you, package folders or build configuration.

**Fixed public functions:** `choose_random_action(game)`, `find_winning_action(game)`, `find_blocking_action(game)`, `score_action(game, action)`, `choose_rule_based_action(game)`.

An internal helper named `_opponent_can_win_immediately(state, opponent)` is specified in Task 3. This is the only additional helper required by the teaching plan; do not create a new framework or agent hierarchy.

## Gates
| Task | Outcome | How you verify |
|---|---|---|
| 00 | Understand prepared code | Default baseline tests + teacher orientation |
| 01 | Random legal decisions | `challenge_tests/test_gate1_random.py` |
| 02 | Immediate winning decisions | `challenge_tests/test_gate2_wins.py` |
| 03 | Preventable immediate threats | `challenge_tests/test_gate3_blocking.py` |
| 04 | Heuristic scoring | `challenge_tests/test_gate4_heuristic.py` |
| 05 | Complete rule-based decision | `challenge_tests/test_gate5_strategy.py` |
| 06 | Verify integration and release | All tests, both computer modes, viva |

Complete tasks **in order**. A gate passes when its tests and teacher checks pass and you can explain the function's behaviour. Do not move forward because a date has arrived.

## Success standard
A strategy must: return the correct action or `None`; preserve real game state; follow fixed priority and tie-break rules; obey the required file/function contract; pass placement and movement checks; and remain understandable to you.

## Technical contract summary
Screen positions are 1–9; Python action indexes are 0–8. Example tuples: `('place', 4)` means screen position 5; `('move', 4, 7)` means move screen 5 to 8. Return a tuple from `game.get_legal_actions()`; do not directly modify `game.board` or prompt for input.

## Explicitly excluded
Recursion, BFS, DFS, search trees, minimax, neural networks, ML training, databases, Textual, new game modes, different scoring rules and unrelated UI upgrades.
