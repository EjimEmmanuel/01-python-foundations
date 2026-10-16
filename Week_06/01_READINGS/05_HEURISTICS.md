# Reading 5 — Heuristics and Action Scoring

**Week 6 · Required reading · Read before project work**

## Learning goals
Explain a heuristic, build simple scoring criteria, distinguish exact wins from estimates, and evaluate competing actions without changing the actual environment.

## 1. When no urgent rule applies
Suppose a computer cannot win immediately, and there is no immediate threat to block. It still needs to choose one of its legal moves. Picking randomly is valid but might ignore obvious preferences.

A **heuristic** is a practical rule or estimate that helps us select a promising action without proving that the action is globally best. Heuristics are useful in games, navigation, scheduling and many other problems where perfect evaluation may be costly or unavailable.

A heuristic differs from a strict rule. “Placing at position 5 is legal because it is empty” is a rule. “Owning the centre may be useful” is a heuristic. The first can be checked exactly; the second is a strategic preference that may be wrong in some positions.

## 2. Scoring makes preferences explicit
Rather than returning a vague judgment like “good move,” we can assign a numeric score.

Example for a work-planning program:

| Condition | Score |
|---|---:|
| Unblocks a teammate | +4 |
| Due today | +3 |
| Matches current skill | +1 |

A decision procedure evaluates each available task, sums applicable weights and selects the highest-scoring task. Those weights are a *design choice*, not evidence that the strategy is optimal.

The number itself is less important than the meaning and consistency of the scheme.

## 3. Our exact Stone Lines scoring scheme
The Week 6 project uses the **resulting board after a candidate action**. These scores are fixed so different students and tests agree.

- If the action immediately wins for the active player, **return 100** without adding other points.
- For each winning line containing **two current-player stones, one empty position, and no opponent stone**, add **4**.
- For each winning line containing **one current-player stone, two empty positions, and no opponent stone**, add **1**.
- For a line containing any opponent stone, add **0** for that line.
- If the current player occupies board **index 4 (screen position 5)** after the move, add **2** once.

The result must be an integer. Illegal actions are **not scored**; the function should raise `ValueError` when given an action outside `game.get_legal_actions()`.

A crucial distinction: a line containing three of your stones is a win, so the function returns 100; it does not get an ordinary +4 score.

## 4. Worked example on an empty board
Consider an entirely empty board with X to play.

If X places at screen position 5 (index 4), the resulting X occupies the centre. That square lies on four winning lines: middle row, middle column and both diagonals. Each is an open one-stone line worth +1, and centre occupancy adds +2:

```text
Four open one-stone lines: 4 × 1 = 4
Centre bonus:             + 2
Total:                      6
```

By contrast, placing at screen position 1 (index 0) participates in three winning lines, with no centre bonus, giving **3**. Under this simple heuristic, centre placement is preferred from an empty board. This preference is not a proof that centre is always the best move.

## 5. Count lines carefully
The eight fixed winning lines are available in `stone_lines/constants.py` as `WINNING_LINES`. The evaluator can loop through them.

A line such as `(0, 1, 2)` might contain `['X', 'X', '3']`: two X stones and one empty screen-number cell. It contributes +4 for X if O is absent. Another line containing `['X', 'O', '3']` contributes zero because it is blocked by the opponent.

Remember that empty board cells are stored as strings of their screen numbers, not a single fixed empty symbol. To decide whether a line is open, count occurrences of `X` and `O` and ensure the opponent symbol is not present.

## 6. Preview before you score
`game.preview_action(action)` creates the resulting state without modifying the real match. You must inspect that resulting board, not the original board, because the point is to evaluate **what changes if you select this action**.

```text
current board
    |
    +-- preview action A --> score A
    +-- preview action B --> score B
    +-- preview action C --> score C
    |
actual board stays unchanged
```

Verify the candidate is in the legal-action list before previewing it.

## 7. Heuristic limitations
A move can earn open-line points but still allow an opponent to win two turns later. Our Week 6 priority rules reduce obvious mistakes by checking wins and threats *before* heuristic scoring. They do not guarantee perfect play.

Exploring multiple future moves is the subject of Weeks 7–8; do not introduce that search here.

## 8. Comparing equal scores
If two actions tie for the highest **positive** score, choose the first in the list from `get_legal_actions()`. If the highest score is zero or negative, the final strategy uses a random legal fallback.

Scoring is different from choosing: a score is a number; a choice is an action tuple. Keep them as separate functions.

## Check your understanding
1. What makes a heuristic different from a guaranteed rule?
2. Why do we evaluate the board after a candidate action?
3. Why does placing X at screen position 5 score 6 on an empty board?
4. Does a line containing X and O contribute to X's heuristic score?
5. How should an illegal action be handled by `score_action()`?
6. What is the difference between `score_action()` and `choose_rule_based_action()`?
7. Give a case where a promising heuristic may still select a poor action.

**Exit check:** You can calculate a simple action score by hand without claiming it predicts the entire game.
