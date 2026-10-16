# Verification Notes — Week 6 Prepared Foundation

## Scope

This stage tests the **prepared game engine and application foundation**, not the AI decision algorithms. The computer strategies in `computer.py` intentionally raise `NotImplementedError`.

## Reproduction

Run these commands from the `stone-lines-arena/` root in a fresh virtual environment:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python main.py
```

Check the following manually:

1. Human vs Human can place stones and ends when a line of three is formed.
2. Six non-winning placements enter movement mode.
3. The active player can move only their own stone to an empty connected position.
4. Invalid choices do not consume a turn.
5. `help` displays rules and `quit` cancels without recording a match.
6. After a completed match, statistics are saved.
7. Selecting a computer mode displays a clear “not implemented” message after the human's opening move rather than crashing.

## Baseline tests

The included tests cover:

- New game state, player validation and turn switching.
- Legal placement/movement enumeration and stable board connections.
- All eight winning lines and win after placement/movement.
- Rejection of illegal actions without changing state.
- Copying and previewing without mutating the original.
- JSON loading, saving, invalid-file handling and result recording.
- Application coordination and safe cancellation.

## Explicit limitations of Stage 1

- Random and rule-based computer strategies are **not** implemented.
- Full Week 6 educational readings, exercises, task instructions and final reference strategy implementation are **not** included.
- Repeated movement positions are not yet automatically treated as a draw. Use `quit` to cancel a looping game; repetition policy can be discussed before game-tree search in later lessons.
- A normal game has six stones and only limited move combinations; this is a teaching project, not a rated competitive-game engine.
- This package starts with a blank statistics file to protect the student's original data.

## QA status

The following values are filled after the final validation and ZIP test. See `QA_RESULTS.txt` in the archive root for machine-checked counts and checksum.
