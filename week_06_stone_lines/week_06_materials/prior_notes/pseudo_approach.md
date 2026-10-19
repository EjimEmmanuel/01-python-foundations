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


# mission 3  Tests

1. on my last test which seemed wrong is becasue of the exit keyword that is on the movement_loop(), so to work, i would need to replace it with return true keyword...




# Mission 5 — Architecture Refactor

## Goal

Separate the growing program into understandable responsibilities.

## Problem

A working one-file game can still be difficult to maintain. Before adding visual polish, examine what your code currently mixes together.

## Target responsibilities

it's remaining this "ui.py → terminal rendering and prompts"



# Mission 6 — Make It Feel Like a Product

## Goal

Use Rich to present the already-correct game clearly and professionally.

## Rule

Do not repair broken game logic with UI code. If a move is illegal, the game engine decides that. The UI only explains the result.


## Procedures:


## Required final interface

Show:

- title;
- board;
- player names and symbols;
- current phase;
- current turn;
- session wins;
- useful messages;
- available destinations after a valid movement source is selected;
- command reminder.

## Required final interface

## Error-message standard


## Required final interface

Show:

- title;
- board;
- player names and symbols;
- current phase;
- current turn;
- session wins;
- useful messages;
- available destinations after a valid movement source is selected;
- command reminder.


Avoid:

```text
Invalid input.
```

Prefer:

```text
Position 5 is already occupied.
```

or:

```text
Positions 1 and 3 are not connected.
```

A good interface teaches the user how to recover.


### syntax: "           'return "[bold magenta]O[/bold magenta]"

still wrk on this really well:

## Required final interface

Show:

- title;
- board;
- player names and symbols; *
- current phase;
- current turn;
- session wins;
- useful messages;
- available destinations after a valid movement source is selected;
- command reminder.
 and lastly:
  ###  my code is too complex, i need to shorten it quite well


 # mission 7 - Persistence and replay

### Everything is really working as it should...

1. Create `storage.py` with a small responsibility for:

- loading .json

 ;
- recording one completed result.
- creating a new player record when needed; -----> when there's a replay.
- saving JSON.
