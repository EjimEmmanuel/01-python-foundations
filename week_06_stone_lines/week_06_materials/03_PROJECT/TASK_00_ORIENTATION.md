# Task 00 — Codebase Orientation (No Coding)

**Prerequisites:** Read the Reading Map and Chapters 1–2; teacher authorizes codebase orientation. You do not need to finish all seven chapters or the full knowledge check first. Read the other chapters as the later tasks assign them, and return to them whenever useful.

**Objective:** Understand the engineering foundation prepared from your Week 5 project. **No refactoring and no implementation yet.**

1. Open the `week_06_stone_lines/` folder in the course repository. The prepared Week 6 codebase is already at this folder's root; do not make a second copy.
2. Read `README.md`, `week_06_materials/04_CODEBASE_GUIDES/CODEBASE_CHANGES.md` and `week_06_materials/04_CODEBASE_GUIDES/ARCHITECTURE_AND_API.md` in that order. `CODEBASE_CHANGES.md` explains what the teacher changed or prepared from the earlier project; `ARCHITECTURE_AND_API.md` explains the code structure and contracts. Read `VERIFICATION.md` when checking the prepared baseline.
3. Find `get_legal_actions`, `apply_action`, `copy` and `preview_action` in `stone_lines/game.py`. Explain what each returns or changes.
4. Find the application mode selection in `stone_lines/app.py`. Observe where the future computer decisions are requested.
5. Find the five unfinished functions in `stone_lines/computer.py`. Do not modify them yet.
6. Install dependencies into a virtual environment using the README in `week_06_stone_lines/`. Run `python -m pytest -q` from that folder. The prepared infrastructure tests should pass.
7. Run `python main.py`; complete or demonstrate Human vs Human. Computer modes will say their strategy is not yet implemented. This is expected.
8. Draw the flow: game state → legal actions → strategy → selected tuple → engine execution → UI.

**Do not edit:** files, class architecture, board rules or menu flow.

**Teacher checkpoint:** Point to each file, show the baseline tests and explain why a strategy must *return* actions rather than *apply* them. Distinguish display labels 1–9 from indexes 0–8. Proceed only when this is clear.

**Suggested commit:** `chore: begin week 6 from prepared baseline`.
