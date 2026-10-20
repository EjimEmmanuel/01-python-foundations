# Reading 6 — Agents and the Observe–Decide–Act Cycle

**Week 6 · Required reading · Read before the tasks that use these ideas; revisit as needed**

## Learning goals
Define an agent, environment, observation, action, goal and policy; describe agent-environment interaction; and recognize that agents can use rules without ML.

## 1. What is an agent?
An **agent** is a system that receives information about an environment and selects actions toward an objective. AI courses study how to design agents that make appropriate decisions given their goals and available observations.

An agent does not have to be a robot, a neural network or an LLM. A program selecting moves in a board game is a simple agent. A thermostat implementing a temperature-control policy is another example.

## 2. Environment, observations, goals and actions
**Environment:** The world in which the agent acts. For Stone Lines, this is the game and its rules.

**Observation:** Information the agent receives. In our full-information game, the computer can inspect the board, turn, phase and legal actions.

**Action:** A choice the agent makes, such as a placement or movement tuple.

**Goal:** What the agent tries to achieve. For our computer player, the competitive goal is to win while making legal actions.

**Policy / strategy:** The method for choosing actions based on observations or states. A random policy selects from legal actions; a rule-based policy uses priorities and preferences.

## 3. The observe–decide–act loop

```text
Environment supplies state / observations
                    |
                    v
            AGENT chooses an action
                    |
                    v
         Environment validates and acts
                    |
                    v
              Updated environment
                    |
                    +----> Next observation
```

Week 6 focuses on the **choose** part. The Week 5 game engine already handles validating and applying actions. The agent should not duplicate that responsibility.

## 4. Example: battery controller
Imagine an electric delivery bike with a simple controller:

- Environment: bike and route.
- Observation: current battery and remaining distance.
- Legal actions: continue, slow down, stop at a safe charger.
- Goal: finish the journey without unsafe battery depletion.
- Policy: apply the low-battery priority rule before preferring normal speed.

Different policies can produce different outcomes with identical sensor readings. This system can be useful without learning from examples: the developer supplies the thresholds and rules.

## 5. Fully versus partially observed (intuition only)
In Stone Lines, the entire board is visible and there are no hidden pieces, so it is fully observed for the information needed to choose a move. In robotics, sensors may not reveal what is behind a wall or whether a road ahead is blocked. The agent must then act on incomplete information.

We only need this intuition for now. Probability models and uncertainty can wait.

## 6. Different policies, one game

```text
Game state -> Random policy -> legal action
Game state -> Rule policy   -> legal action
```

The game engine does not need to know *why* the agent selected an action. It accepts a correctly formatted action and validates it. This makes strategy comparison possible without rewriting the game.

This design generalizes to other systems: the interface remains fixed while decision policies change.

## 7. Rationality versus success
An AI text may describe a rational agent as selecting actions that achieve the best expected outcome given its knowledge and goals. That is a design ideal, not a guarantee that every concrete agent succeeds. Our Week 6 agent uses deliberately simple rules. It is neither optimal nor unbeatable.

Later, we will examine how an agent can consider future moves and an opponent's responses. Understanding the agent concept comes first.

## 8. Common misconceptions
- “Every agent uses an LLM.” False.
- “If it acts automatically, it must be learning.” False.
- “Agents should execute actions inside the choice function.” Not in this project.
- “More complexity always makes a better strategy.” False.

## Check your understanding
1. Define environment, observation, action and policy for automatic watering.
2. What is the agent's goal in Stone Lines?
3. Why must the game's validator stay separate from the strategy?
4. Can a simple thermostat count as an agent under this broad definition? Explain.
5. What changes when an agent cannot observe the full environment?
6. How can Random and Rule-Based Computer modes use the same game engine?

**Exit check:** Draw an observe–decide–act cycle and label it for two different systems.
