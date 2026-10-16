# Reading 3 — Random Choices and Baseline Strategies

**Week 6 · Required reading · Read before project work**

## Learning goals
Use `random.choice()` safely, understand what randomness can and cannot do, describe a baseline strategy, and make small randomized programs reproducible for debugging.

## 1. Random is a decision method
A random strategy selects from available options without ranking them according to strategic benefit.

```python
import random

options = ["north", "south", "east"]
selected = random.choice(options)
```

Each option can be selected. If we repeat this call, the result may change. **Random does not mean illegal**, and **unpredictable does not mean intelligent**.

Consider a game opponent. If it randomly chooses from all board positions, it might choose an occupied or unreachable position. The correct approach is to give it **only legal actions** to begin with.

```python
legal_actions = [("place", 2), ("place", 5), ("place", 8)]
selected = random.choice(legal_actions)
```

The strategy does not need to know how placement legality is calculated. It trusts the game engine's list.

## 2. The empty-list problem
Python raises `IndexError` if you call `random.choice([])`. A robust function handles the empty case explicitly:

```python
def pick_option(options):
    if not options:
        return None
    return random.choice(options)
```

Returning `None` is a documented convention in our project when there are no legal actions. It is not an excuse to use `None` for ordinary legal actions.

## 3. Why baselines matter
Suppose you later build a more complicated strategy. How do you know whether it is actually better? You need a baseline—a straightforward method with which to compare it. A random legal strategy is often a convenient starting point.

A random baseline helps with several questions:

- Does the game allow programmatic decisions at all?
- Are the legal-action rules implemented correctly?
- Does the supposedly smarter strategy consistently perform better in comparable situations?
- Can automated matches run without human input?

A baseline is not necessarily “bad software.” It is a tool for understanding improvements. If a complicated strategy loses more often than a random one, we have a reason to investigate.

## 4. Reproducibility
Python's pseudo-random generator can produce repeatable results when initialized with a seed. For a standalone experiment:

```python
import random
random.seed(42)
print(random.choice(["A", "B", "C"]))
```

The purpose of a seed is not to make a strategy smarter. It allows you to reproduce certain sequences of selections when investigating a problem.

In library code and general applications, repeatedly calling `random.seed()` inside a strategy is usually a bad idea. It modifies global generator state and can make other uses of randomness surprising. For the Week 6 function, use `random.choice()` directly and let test code control reproducibility where necessary.

## 5. Independence and fairness
If a collection contains repeated elements, `random.choice()` selects among list entries, not conceptual categories. For example:

```python
choices = ["red", "red", "blue"]
```

Here red is more likely than blue because it appears twice. Our game engine returns each distinct legal action once in a defined order, so using that list does not intentionally weight one action more than another.

Randomness alone also says nothing about fairness across an entire tournament. You would need enough trials and a careful comparison setup to draw conclusions. We will learn formal data analysis later in the course.

## 6. A baseline is a design decision
A random strategy is useful where there are no strong preferences or when a fallback is needed. It is less appropriate when the cost of a poor action is high. A medical device or emergency shutdown controller should not randomly choose a safety-critical operation.

The correct strategy depends on the problem's goals and constraints. That judgment—choosing the right level of automation—is part of engineering.

## 7. Trace exercise
Study this function without running it:

```python
import random

def pick_task(tasks):
    if not tasks:
        return None
    return random.choice(tasks)
```

What will it return if `tasks=[]`? What **kind** of value will it return when `tasks=["review", "test"]`? Can you predict which exact value on every call? Why not?

Next, consider why `random.choice(game.get_legal_actions())` would not be safe without first handling an empty list.

## 8. Scope for Week 6
We will create a random *action selector*, not a new rules engine or a simulation platform. It will return an action; the existing `Game` instance will execute it. No machine learning is involved.

## Check your understanding
1. Why should randomness operate on a list of legal actions?
2. What error occurs with `random.choice([])`?
3. What is a baseline and what can it help you discover?
4. What does a random seed change? What does it not change?
5. Why should the decision function not call `game.apply_action()` itself?
6. Name one context where random selection is useful and another where it would be unsafe.

**Exit check:** You can design a safe random selector with a documented `None` case and explain its role as a baseline.
