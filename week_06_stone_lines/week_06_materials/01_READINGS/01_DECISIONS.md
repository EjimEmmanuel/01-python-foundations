# Reading 1 — How Software Makes Decisions

**Week 6 · Required reading · Read before the tasks that use these ideas; revisit as needed**

## Learning goals
By the end of this chapter, you should explain a **condition**, **decision**, **action**, **strategy**, **priority** and **fallback**; trace the order in which rules run; and design a small decision system without writing code first.

## 1. From instructions to choices
Previously, you wrote programs that print information, check inputs, calculate values and store records. These programs already contain decisions. For example:

```python
temperature = 34
if temperature > 30:
    action = "turn_on_fan"
else:
    action = "leave_fan_off"
```

The program has two possible actions. A condition determines which one is selected. This is a **decision point**. The computer does not feel hot or prefer cool rooms; a developer supplied a rule and the computer applies it.

As programs grow, several conditions can matter at once. Imagine a solar-powered fan: a hot room suggests turning it on, but a critically low battery may require saving electricity. We therefore need an **ordered decision strategy**:

```text
IF battery is critically low:
    choose power-saving mode
ELSE IF room is too hot:
    turn on fan
ELSE:
    leave fan off
```

The first rule is evaluated before the second. The decision would change if we reversed the priority. We are not simply writing several unrelated `if` statements; we are defining which concern matters most.

## 2. Facts, decisions, actions and policies
A **fact about the current situation** might be “battery is 9%.” A **decision** is the selection “enter power-saving mode.” An **action** is the operation taken after the decision. A **strategy** is the general procedure used to select actions. The word **policy** also refers to a method for mapping observations or states to actions; you will see it again in later AI topics.

Keep two operations distinct:

```python
def choose_action(battery, temperature):
    if battery < 15:
        return "save_power"
    if temperature > 30:
        return "cool"
    return "wait"

selected = choose_action(9, 34)
# A different part of the program executes selected.
```

Returning an action is not the same as carrying it out. In a larger system, one module chooses and another validates or executes. This distinction is essential for our Week 6 project.

## 3. Deterministic decisions
A **deterministic** decision strategy produces the same result for the same inputs and state, assuming no other changing external factors. The battery example is deterministic. If battery is 9% and temperature is 34°C, the selected action is always `"save_power"`.

Determinism makes a strategy easier to explain, debug and test. It does not guarantee the strategy is good. A consistent decision can be consistently wrong if the rules or priorities are poor.

A computer strategy in Week 6 will initially use explicit rules. Later, one strategy will sometimes choose randomly; that is a deliberately different decision method.

## 4. Rule order and conflicts
Suppose an automated warehouse door follows these rules:

- Open when a worker approaches.
- Stay closed during a fire-safety lockdown.
- Stay closed when power is unavailable.

If the first rule always runs first, the door might open during a lockdown. We must define the priority of safety rules above convenience rules. A decision table can expose such conflicts:

| Lockdown | Worker near door | Selected action |
|---|---|---|
| Yes | Yes | Keep closed |
| Yes | No | Keep closed |
| No | Yes | Open |
| No | No | Keep closed |

The important question is not just “Does each rule work?” but “Do the rules work together in the right order?”

## 5. Fallback actions
Sometimes no preferred rule applies. A **fallback** tells the program what to do then. Without a fallback, a function may accidentally return `None`, or a later part of the program may fail.

A fallback might be to wait, request help, choose a default option, or select randomly from valid options. A fallback must still obey the environment's rules. An illegal action is not an acceptable fallback.

For Stone Lines, an ordered strategy could eventually mean: win if possible; otherwise prevent an immediate loss; otherwise prefer a promising move; otherwise choose any legal move. This is a conceptual preview—not yet a coding task.

## 6. Read a program before running it
Study this example:

```python
def choose_charging_mode(battery, solar_available):
    if battery < 20:
        return "priority_charge"
    if solar_available:
        return "solar_charge"
    return "normal_operation"
```

Predict the output for `(12, True)`, `(65, True)` and `(65, False)`. Explain **which condition decided the result**, not just which string was returned.

Next, consider whether changing the order of the conditions would change the outcome when the battery is low and solar power is available.

## 7. Common mistakes
1. Treating several independent `if` statements as though only one can run. Use `elif` or explicit returns where only one action should be selected.
2. Putting a low-priority rule before an urgent one.
3. Confusing deciding with performing: a chooser that prints, prompts and mutates state is harder to test.
4. Assuming a rule-based program is necessarily intelligent or optimal. It only implements the rules you wrote.
5. Forgetting the “nothing matches” case.

## Check your understanding
Write answers in your learning notebook before moving forward.

1. What is the difference between a condition and an action?
2. Why does rule order matter in the fan example?
3. What makes a strategy deterministic?
4. Give a real-world example where a fallback is needed.
5. Why might `choose_action()` return a value instead of directly changing a device or a game board?
6. Design three rules for a library book-return reminder. Put them in priority order and state the fallback.

**Exit check:** You can take a plain-English decision requirement and express it as ordered pseudocode with a valid fallback.
