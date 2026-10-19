# Pre-Project Exercises and Worked Examples

These examples are **independent of Stone Lines**. Read them before the knowledge check. Predict answers before reading the explanations.

## Example 1 — A temperature controller

```python
def decide(battery, temperature):
    if battery < 15:
        return "save_power"
    if temperature > 30:
        return "cool"
    return "wait"
```

**Question:** What does `decide(8, 35)` return? **Explanation:** `"save_power"` because the first condition is satisfied and its return ends the function. The temperature condition is not used.

**Try:** Change the inputs to `(50, 35)`, `(50, 24)` and `(15, 35)`. Explain why the boundary 15 is not “below 15.”

## Example 2 — A valid random chooser

```python
import random

def pick_job(jobs):
    if not jobs:
        return None
    return random.choice(jobs)
```

**Question:** Can the return be a job not present in `jobs`? **Explanation:** No. `random.choice()` selects a member of its supplied non-empty sequence.

**Try:** What change would make the function unsafe when `jobs=[]`?

## Example 3 — Priority versus a tempting preference
A delivery driver has two candidate actions: deliver an urgent medical item now, or choose the nearest normal order. A naive heuristic prefers the nearest order. A properly designed priority system first handles the critical urgent item, then scores ordinary orders.

**Lesson:** A heuristic should not override an urgent higher-priority rule.

## Example 4 — How a heuristic can mislead
A robot navigates towards a destination. The shortest straight-line distance appears to lead through a blocked corridor. Choosing only “distance decreases” can create a poor decision.

**Lesson:** Heuristics estimate promise; they do not prove the future result will be good.

## Example 5 — Decide versus perform

```python
def decide_lamp(brightness):
    return "on" if brightness < 25 else "off"

choice = decide_lamp(10)
# A separate controller validates and carries out choice.
```

**Question:** Why not perform all lamp IO within `decide_lamp()`? **Explanation:** Returning a decision makes the logic reusable and easier to test without attaching a real lamp.

## Independent exercises (do not look up solutions first)
1. Write a three-priority decision policy for a bicycle with a low battery, rain sensor and delivery deadline.
2. List state and legal actions for a file manager where a selected file is read-only.
3. Given tasks `['test', 'review', 'deploy']`, write a selector that chooses at random but safely handles an empty list.
4. Create a policy for a study assistant that prioritizes tomorrow's exam over non-urgent reading, but never schedules work during a medical emergency.
5. Explain why a system that chooses between three hardcoded actions is not automatically a machine-learning system.
