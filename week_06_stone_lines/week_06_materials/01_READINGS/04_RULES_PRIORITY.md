# Reading 4 — Rule-Based Decisions and Priorities

**Week 6 · Required reading · Read before project work**

## Learning goals
Write ordered rule systems, identify priority conflicts, recognize immediate opportunities and threats, and distinguish a helper rule from the complete decision strategy.

## 1. A rule-based system
A rule-based system evaluates facts about the current situation and applies developer-written instructions to select a response. The rules do not appear automatically from data. Someone has to design, implement and test them.

A basic example is a delivery dispatch program:

```text
IF vehicle has a safety warning:
    stop and request inspection
ELSE IF fuel is low:
    route to refuelling
ELSE IF package is urgent:
    deliver urgent package
ELSE:
    continue scheduled route
```

Notice that the safety rule has a higher priority than the delivery deadline. A program can be syntactically correct while the priority order is wrong. That is why rules should be designed in plain language before coding.

## 2. Separate rules into helpers
Each decision rule can have a clear purpose:

```python
def identify_urgent_task(tasks):
    # Select a task that must be handled first, if one exists.
    ...

def identify_blocking_issue(tasks):
    # Find work that prevents other work from proceeding.
    ...
```

A coordinator can call those helpers in the appropriate order. This is preferable to a very large function that mixes every detail. A helper should answer one precise question, return a documented result and avoid unintended side effects.

For Stone Lines, this suggests helpers such as “find an action that wins immediately” and “find an action that prevents an immediate opposing win.” The full strategy decides which helper's result takes priority.

## 3. Immediate winning opportunities
An immediate winning move is a **legal action whose direct result is a win**. The word immediate matters: it means one action, not a sequence of future moves.

To recognize one, you can inspect legal actions and preview each one. In pseudocode:

```text
for each legal action in the engine's stable order:
    preview the action
    if the resulting position is a win for this player:
        return that action
return no action
```

This is still a one-step evaluation, not the recursive search taught in Week 7. If several winning actions exist, choosing the first in stable legal-action order makes the rule easy to test.

## 4. Immediate opposing threats
A threat exists when an opposing player would have a legal one-action win **if given the move in the current position**. A rule-based player should often try to remove such a threat before choosing an unrelated action.

There are two different questions:

1. **Is there a threat before we act?**
2. **Which legal action, if any, leaves the opponent without an immediate winning reply?**

A threat is not always preventable. Some positions contain multiple threats and one move cannot neutralize all of them. Do not confuse “detect a threat” with “guarantee a block.”

Example placement board, with O to move:

```text
X X .
O X .
. . O
```

X threatens the top-row completion at screen position 3. O can place in that position to prevent this particular immediate win. The correct answer must obey the placement rules and should be verified on a snapshot, not by changing the live match.

## 5. Exact Week 6 blocking interpretation
For this course we need a precise, testable definition. The blocking helper returns a legal action only when an **immediate opponent-winning threat exists before the current player's action**, and that chosen action leaves the opponent with **no legal immediate winning reply**. If there is no present threat, or no action can remove all immediate threats, the helper returns `None`.

If several actions completely neutralize the threat, return the first one in the order supplied by `get_legal_actions()`. This makes expected outcomes predictable. It also avoids vaguely choosing a “good block” that still permits another immediate win.

How can we test “if the opponent moved now?” A safe approach is to create a **copy** of the game, make the opponent the active player on that copy, and inspect the opponent's legal one-step wins there. This must never change the real game. The developer's reference guide covers why this is only a limited immediate-threat analysis, not an attempt to reconstruct a complete alternate game history.

## 6. Priority: win before block
What if the computer can win immediately while the opponent also has an immediate threat? Winning immediately ends the game. Therefore:

```text
IF I can win now:
    choose the win
ELSE IF I can remove an immediate opponent threat:
    choose that defensive action
ELSE:
    consider normal preferences
```

Each helper answers a narrow question. The final strategy combines them in priority order. The blocking helper itself does **not** decide that blocking outranks an available win.

## 7. Deterministic tie-breaking
When multiple actions satisfy a rule, our course uses the game's pre-existing stable legal-action order. The first legal winning action is selected; the first effective defensive action is selected. For equally scored heuristic actions, the first highest-scoring one is selected.

This rule matters for reproducibility. A test can expect one action when two are equally valid, rather than fail unpredictably depending on dictionary ordering or hidden random choice.

## 8. Cases to think about
- A game that has already finished: no action should be chosen.
- A placement board with only one empty space: the legal-action list may have one item.
- A movement position where the first potential block is illegal: it must never be returned.
- A position with two independent immediate opponent wins: a single defensive action might not exist.
- The computer already has a winning action: the final strategy must select it ahead of blocking.

## Check your understanding
1. Why should a winning move take priority over a defensive move?
2. What is the difference between “there is a threat” and “there is a legal block”?
3. Why is it important to evaluate opponent replies on a copy?
4. What should the blocking helper return when there is no immediate threat?
5. Explain why selecting the first legal matching action improves tests.
6. Draw a flowchart with win, block and fallback rules.

**Exit check:** You can describe a rule-based action chooser precisely enough that another programmer could implement it without guessing the priority order.
