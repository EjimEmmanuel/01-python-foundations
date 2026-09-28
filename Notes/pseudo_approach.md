# Mission 1 — Bring the Board to Life


1. What value represents an empty cell? : --- The value that represent an empty cell is just a text number (1 - 9)
2. What values represent the two players? --- The values the represent the two players is the aphabetical letters X and O
3. What list index represents player position 1? --- it is (0) that represent the list indexed player position 1
4. What list index represents player position 9? --- it is (8) that represent the list indexed player position 9
5. If position 5 contains X, what should the underlying list look like? --- it should look like

# Mission 2 — Placement Engine


## Phase-rules 1 - Placement
A placement is invalid if:

- the value is not a valid position;
- the chosen position is already occupied;
- placement has already ended;
- the match is already over.

## Goal

Make two players place stones legally and alternate turns.

## Rule ladder

A placement can succeed only when all of these are true:

```text
game is not over
AND phase is placement
AND position is between 1 and 9
AND position is empty
```
