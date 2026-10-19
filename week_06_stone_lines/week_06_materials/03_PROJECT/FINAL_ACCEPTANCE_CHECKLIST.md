# Final Week 6 Project Acceptance Checklist

Use this checklist *before* requesting final assessment. Teacher signs off after verification.

## Contract and organization
- [ ] Five required functions have their original names and parameters.
- [ ] Required private opponent-threat helper is implemented in `computer.py`.
- [ ] Decision logic lives only in `stone_lines/computer.py`.
- [ ] Game, UI, storage, constants and package structure are not needlessly changed.
- [ ] Actions are tuples with zero-based indexes.
- [ ] Original game state is unchanged by all decision and scoring functions.

## Behaviour
- [ ] Random mode chooses only legal actions in placement and movement.
- [ ] Empty legal-action lists return `None` in selecting functions.
- [ ] Immediate wins are preferred over all other decisions.
- [ ] Effective blocks are chosen for existing immediate threats.
- [ ] No preventable action or no threat means blocking helper returns `None`.
- [ ] Heuristic scores use the exact 100, +4, +1 and +2 rules.
- [ ] Illegal actions passed for scoring raise `ValueError`.
- [ ] Equal positive heuristic scores use first-in-list tie-break.
- [ ] Random fallback is used only when no positive heuristic preference exists.

## Tests and demonstration
- [ ] Baseline tests pass.
- [ ] All five supplied gate files pass.
- [ ] Student-created `tests/test_computer.py` passes.
- [ ] Human vs Human still works.
- [ ] Human vs Random works in both phases.
- [ ] Human vs Rule-Based works in both phases.
- [ ] Completed match statistics work; cancelled matches do not record.
- [ ] Student can explain a strategy step-by-step without reading the implementation aloud.
- [ ] README and Git history reflect the Week 6 release.

**Not required:** minimax, BFS, DFS, recursion, machine learning, more gameplay features, or UI redesign.
