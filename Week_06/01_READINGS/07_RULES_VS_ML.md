# Reading 7 — Rule-Based AI Is Not Machine Learning

**Week 6 · Required reading · Read before project work**

## Learning goals
Explain explicit rules versus learned models; choose a reasonable technique for a simple problem; and explain why Week 6's computer agent is not an ML model.

## 1. Why the distinction matters
This course builds toward ML, deep learning and modern AI engineering. Before training models, understand that **AI includes techniques that do not learn from data**. Decision rules, search, planning and learned models are different approaches to problems.

A program that plays Stone Lines using handwritten rules may behave purposefully. But unless it learns a decision function or parameters from experience or examples, it is **not machine learning**.

## 2. Explicit rules
In a rule-based system, the developer supplies the conditions and actions.

```python
def label_temperature(value):
    if value >= 35:
        return "very_hot"
    if value >= 25:
        return "warm"
    return "cool"
```

The thresholds come from the developer. Running the function many times does not automatically change them. You must edit the rules or implement another learning mechanism.

In Week 6, you explicitly implement priorities for immediate wins, opponent threats, heuristic scores and random fallback.

## 3. Learning from examples
In supervised learning, a program is given examples containing features and target outputs. A learning algorithm adjusts model parameters to improve predictions on new examples.

```text
Training examples (features + targets)
             |
             v
       Learning algorithm
             |
             v
        Trained model
             |
             v
New input -> Prediction
```

For example, a model might learn relationships between house features and prices from historic transactions. The developer designs training and evaluation, but does not write a rule for every possible feature combination.

A model must be evaluated on suitable test data. Producing predictions does not prove learning is useful or reliable.

## 4. Compare the approaches

| Question | Rule-based software | Supervised ML |
|---|---|---|
| Where does behaviour come from? | Explicit developer rules | Parameters learned from examples |
| Is training data required? | Not generally | Usually |
| Can choices be explained? | Often through rule priority | Depends on the model |
| Is performance guaranteed? | No | No |
| Can they coexist? | Yes | Yes |

This comparison describes common patterns rather than every possible system.

## 5. Where exact rules are better
When exact requirements are already available—valid board positions, file access permissions, input validation—ordinary programming is often the right choice. A probabilistic model should not guess a legal move when the game rules are explicit.

ML may be appropriate where useful patterns are hard to handwrite, relevant examples are available, and improved predictive performance justifies complexity. Even then, a larger system may combine learned predictions with exact validation rules.

## 6. Not all decision-makers learn
A random player can act but has no strategic assessment. A rule-based player can make sensible immediate decisions yet lose because it cannot look ahead. An ML model may recognize patterns but fail on unfamiliar inputs. Each method has limitations.

Describe a system by answering: **What information does it use? How does it choose? How have we verified its decisions?** Avoid claiming it is intelligent merely because it acts automatically.

## 7. Connections to the roadmap
- Week 6: programmed decisions and simple heuristics.
- Week 7: explore possible future states.
- Week 8: account for an opponent using minimax.
- Weeks 9–12: investigate data.
- Weeks 13 onward: learn predictive models from examples.

These approaches complement each other. Good engineers know when not to use ML.

## 8. Thought experiment
A delivery vehicle should stop when its battery falls below a certified safety threshold. Would you use a clear safety rule or a model guessing a safe threshold? Why?

The same vehicle needs to *predict* remaining range under changing traffic conditions from historical data. Which technique might be suitable now? Why?

## Check your understanding
1. Why does Week 6 not count as ML?
2. Can a system choose actions without using neural networks?
3. Why are exact rules preferable for move legality?
4. What information does a supervised learning algorithm train on?
5. Can a full AI application combine rules and ML?
6. Give one problem suited to fixed rules and another worth investigating with ML.

**Exit check:** You can explain the Week 6 agent without calling it a trained model.
