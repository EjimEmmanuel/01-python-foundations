# Knowledge Check — Complete Before the Project

**Suggested time:** 35–50 minutes. Answer without AI-generated solutions. Notes may be allowed for the first review, but the teacher should include an oral closed-note check.

## Part A — Concepts (20 points; 4 each)
1. Define state, action and legal action, using an example *not* taken from Stone Lines.
2. Explain the difference between deciding an action and executing it. Why does the distinction matter for testing?
3. Explain why rule order matters in a decision strategy. Provide a priority conflict.
4. What is a random baseline? What can comparing it against a rule-based strategy reveal?
5. State one difference between rule-based AI and supervised machine learning.

## Part B — Trace and reason (20 points; 5 each)
6. A battery manager uses: **if battery below 15%, save power; else if temperature above 30°C, cool; else wait**. Which action is selected for battery=10, temperature=38? Explain.
7. Why is `random.choice([])` unsafe? Give the correct high-level safeguard.
8. Explain what is wrong with a strategy that modifies the original game board to check a possible move, then tries to undo the change.
9. What does the tuple `('move', 4, 7)` mean on a board displaying positions 1–9?

## Part C — Design (30 points; 10 each)
10. Write pseudocode for a random action chooser with an empty-choice case.
11. Write pseudocode for the order **win → effective block → heuristic → fallback** without using recursion.
12. Explain how you would detect an immediate win safely using a one-action preview and a result check. What does the function return if no win exists?

## Part D — Heuristics and explanation (30 points; 10 each)
13. On an empty board with X to place, calculate the Week 6 score for choosing the centre and explain every point.
14. A board position already contains an opponent stone in a particular potential winning line. What does that line contribute to the active player's heuristic score? Why?
15. Describe the observe–decide–act cycle for a device or service outside games, and identify its policy.

**Pass expectation:** At least 70/100 overall, and teacher confirms that you understand legal actions, state preservation, rule priority and the distinction from ML. If these foundational items are weak, revisit their readings before coding.
