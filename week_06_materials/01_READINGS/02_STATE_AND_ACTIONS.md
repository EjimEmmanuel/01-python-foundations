# Reading 2 — States, Actions and Legal Choices

**Week 6 · Required reading · Read before project work**

## Learning goals
Explain what constitutes a state; distinguish possible actions from legal actions; understand why selecting and executing are separate; and describe a game's placement and movement choices using stable data.

## 1. What is state?
A **state** is the information needed to describe the current situation for the decision at hand. A delivery robot might need its location, its battery, whether a door is open and the intended destination. A music player might need the current song, whether playback is paused and the current volume.

For Stone Lines, useful state includes the current board, player whose turn it is, placement or movement phase, and whether the match has ended. The state must be sufficient to interpret what the next legal action means. Knowing only the board is not enough if the set of allowed actions changes between phases.

A **state snapshot** is a record of that situation at a particular moment. It lets us reason about “what is true now” without confusing it with “what might happen next.”

## 2. Actions and legal actions
An **action** is a possible operation, such as putting a stone in a position or moving a stone from one position to another. A **legal action** is one that obeys all relevant rules in the current state.

```text
All imaginable actions
        |
        | Apply the rules of the environment
        v
Legal actions (subset)
        |
        | Decision strategy selects one
        v
Selected action
```

For example, a human can type screen position 50, but it is not a legal Stone Lines position. Screen position 5 may be within the board but already occupied, so a placement there is still illegal. During movement, the destination must be empty and connected to a source that belongs to the active player.

The rule checker is the **authority**. The strategy should not invent its own version of the rules.

## 3. A fixed action representation
In our project, actions are tuples with a common format:

```python
("place", 4)        # screen position 5
("move", 4, 7)      # screen positions 5 -> 8
```

The display uses positions **1–9**. Python indexes are **0–8**. Screen position 5 maps to index 4. This is a fixed convention, not a student's design choice.

Why is a fixed format useful? Because the UI, game engine, strategies and tests can exchange one familiar kind of value. Without a shared contract, one module might return strings and another expect tuples; both components might appear correct independently but fail when combined.

## 4. Asking for legal actions is different from validating one action
Week 5 validated an action supplied by a human. The question was: **“Is this proposed move allowed?”**

Week 6 asks: **“Which moves are allowed right now?”** That is why the engine provides:

```python
actions = game.get_legal_actions()
```

This method returns an ordered list of legal action tuples, without changing the real game. During placement, it lists empty positions; during movement it lists valid `(source, target)` combinations. An empty list means no legal action is currently available, including after a finished match.

For an example beginning of a match:

```python
[("place", 0), ("place", 1), ..., ("place", 8)]
```

Later in the game, the list will be smaller and may contain movement tuples. Never assume a hard-coded number of actions.

## 5. Decisions should not mutate the real game
There is an important boundary:

```python
selected = choose_strategy(game)  # returns an action; state unchanged
game.apply_action(selected)       # checks and executes the action
```

`apply_action()` is responsible for executing a legal move, switching the player when appropriate, checking wins and changing the phase. If we let strategies write directly to `game.board`, we could accidentally bypass validation, turn order, victory detection or statistics workflows.

This also improves testing: it is easy to verify that a chooser returned an expected tuple **and** left the input game unchanged.

## 6. Safe hypothetical actions
Sometimes a decision depends on the result of making a move. We need to **preview** the result without taking the move in the real match.

```python
future = game.preview_action(("place", 4))
```

This returns a separate `Game` object containing the state after that move. The actual `game` remains unchanged. If the move is illegal, `preview_action()` raises `ValueError`; it does not repair or execute it.

The engine also supplies `game.copy()` for creating an independent snapshot. In Week 6, a strategy may work with copied state, but it must not change the real match object.

This is a single-move preview. Looking many moves ahead belongs to the next reading phase of the course, not to this week's project.

## 7. Empty choices and finished states
Do not assume every call produces an action. A finished game has no legal actions; an agent's decision function should then return `None`. The application should not silently make up a move or call `random.choice()` on an empty list.

For programming, an empty list is not an exception by itself. It is useful information about the current state. Our decision strategy must translate that information into a safe result.

## 8. State and action examples outside games
**Robot:** state = `(room, battery, obstacle)`; legal actions = move into a clear adjacent room, wait, recharge at a charger.

**File manager:** state = `(current folder, selected file, permissions)`; legal actions = open a readable file, rename a writable file, navigate to an accessible directory.

**Elevator:** state = `(floor, door status, travel direction)`; legal actions = open door when stopped, travel toward a requested floor when doors are closed.

The key ideas generalize well beyond games.

## Check your understanding
1. Why is knowing the Stone Lines board alone insufficient to determine every legal move?
2. In your own words, distinguish “possible” from “legal.”
3. What is the Python action tuple for placing at screen position 9?
4. Why must a strategy return an action rather than edit `game.board`?
5. What does `preview_action()` return, and what should it not change?
6. What should a decision function return if no actions are available?
7. Draw a short diagram describing **state → legal actions → selected action → updated state** for a non-game system.

**Exit check:** You can correctly describe the project action format, produce example legal actions, and explain the game engine's authority over the rules.
