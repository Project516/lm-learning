# Day 5 - The ethics labs: audit a biased model, red-team a reward.
#
# The BEST home for these labs is your own files: add Lab 1 to your
# day2_knn_starter.py and Lab 2 to your day4_qlearning_starter.py,
# where you built every piece yourself. This file exists as a backup:
# if a file from earlier in the week is missing or broken, everything
# both labs need is provided below, ready to run.
#
# The building was the fun part, and you already did it. Today you are
# not building a model. You are auditing one, and breaking one.

# ======================================================================
# LAB 1: AUDIT A BIASED MODEL (ethics section 4)
# ======================================================================
# Provided: the Day 2 classifier, exactly as you built it on Tuesday.
import math
import random


def distance(row_a, row_b):
    """Straight-line distance between two flowers' features (PROVIDED)."""
    total = 0
    for i in range(2):
        diff = row_a[i] - row_b[i]
        total = total + diff * diff
    return math.sqrt(total)


def knn_predict(training, query, k):
    """Predicts a species by letting the k closest flowers vote (PROVIDED)."""
    scored = []
    for row in training:
        scored.append([distance(row, query), row[2]])
    scored.sort()
    nearest_labels = []
    for i in range(k):
        nearest_labels.append(scored[i][1])
    best_label = nearest_labels[0]
    best_count = 0
    for label in nearest_labels:
        c = nearest_labels.count(label)
        if c > best_count:
            best_count = c
            best_label = label
    return best_label


def accuracy(training, test, k):
    """Fraction of test rows predicted correctly (PROVIDED)."""
    correct = 0
    for row in test:
        if knn_predict(training, row, k) == row[2]:
            correct = correct + 1
    return correct / len(test)


# The model under audit: trained on a world where versicolor barely
# exists (the skewed data from Day 2, section 10).
skewed_training = [
    [1.4, 0.2, "setosa"],
    [1.3, 0.2, "setosa"],
    [1.5, 0.2, "setosa"],
    [1.7, 0.4, "setosa"],
    [1.4, 0.3, "setosa"],
    [6.0, 2.5, "virginica"],
    [5.8, 1.8, "virginica"],
    [6.3, 1.8, "virginica"],
    [5.5, 2.1, "virginica"],
    [5.1, 1.9, "virginica"],
    [4.5, 1.5, "versicolor"],  # the only versicolor left
]

# The honest audit set: versicolor still exists in the WORLD, even if
# it barely exists in the model's training data.
audit_set = [
    [1.5, 0.2, "setosa"],
    [1.6, 0.3, "setosa"],
    [4.2, 1.3, "versicolor"],
    [4.4, 1.4, "versicolor"],
    [4.6, 1.4, "versicolor"],
    [6.1, 2.3, "virginica"],
    [5.7, 2.0, "virginica"],
]

# The headline number every press release would quote:
print("overall accuracy:", accuracy(skewed_training, audit_set, 3))

# TODO (Lab 1): the audit. One accuracy per group, not one for the
# whole model. For each species in ["setosa", "versicolor", "virginica"]:
#   - count how many audit_set rows truly belong to that species (total)
#   - count how many of THOSE knn_predict(skewed_training, row, 3)
#     predicted correctly (right)
#   - print(species, ":", right, "/", total)
# The lab page (ethics section 4) has the skeleton with hints.

# TODO (Lab 1, deliverable): fill in your model card.
# MODEL CARD - skewed flower classifier, audited by: ___
# Overall accuracy:  ___
# Setosa:     _ / _
# Versicolor: _ / _
# Virginica:  _ / _
# Safe to use for:      ___
# NOT safe to use for:  ___
# To fix it, we would need: ___


# ======================================================================
# LAB 2: RED-TEAM THE REWARD (ethics section 5)
# ======================================================================
# Provided: the Day 4 GridWorld and Q-learning loop, exactly as you
# built them yesterday, already pointed at the package world.


def step(state, action):
    """Moves the agent one cell, respecting the edges (PROVIDED)."""
    row = state // 3
    col = state % 3
    if action == "up" and row > 0:
        row = row - 1
    elif action == "down" and row < 2:
        row = row + 1
    elif action == "left" and col > 0:
        col = col - 1
    elif action == "right" and col < 2:
        col = col + 1
    return row * 3 + col


# THE CLIENT'S SPEC: "pick up the package at cell 6, then deliver
# yourself to the goal at cell 8." Your pricing decision is `bonus`.
bonus = 5  # <-- TODO (Lab 2): this is the number you red-team.
# Start at 5 and run the file: watch the agent find the
# infinite money glitch. Then hunt for the honest price.


def result_package(new_state):
    """Judges a landing in the package world (PROVIDED)."""
    if new_state == 8:
        return 10, True
    elif new_state == 4:
        return -10, True
    elif new_state == 6:
        return -1 + bonus, False  # the pickup pays on EVERY visit...
    else:
        return -1, False


actions = ["up", "down", "left", "right"]

Q = {}
for state in range(9):
    Q[state] = {}
    for a in actions:
        Q[state][a] = 0.0


def best_value(state):
    """Highest quality estimate in a state (PROVIDED)."""
    best = Q[state]["up"]
    for a in actions:
        best = max(best, Q[state][a])
    return best


def best_action(state):
    """The action the agent currently believes is best (PROVIDED)."""
    best_a = "up"
    best = Q[state]["up"]
    for a in actions:
        if Q[state][a] > best:
            best = Q[state][a]
            best_a = a
    return best_a


# Training (PROVIDED): the Day 4 loop, pointed at result_package.
learning_rate = 0.5
discount = 0.9
epsilon = 0.1

for episode in range(2000):
    state = 0
    done = False
    while not done:
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = best_action(state)
        new_state = step(state, action)
        reward, done = result_package(new_state)
        old = Q[state][action]
        if done:
            target = reward
        else:
            target = reward + discount * best_value(new_state)
        Q[state][action] = old + learning_rate * (target - old)
        state = new_state

# The path follower (PROVIDED), with its safety cap.
state = 0
path = [state]
done = False
steps = 0
while not done and steps < 20:
    action = best_action(state)
    state = step(state, action)
    reward, done = result_package(state)
    path.append(state)
    steps = steps + 1

print("package world, bonus +" + str(bonus) + ":", path)

# TODO (Lab 2): red-team the price. Change `bonus` at the top of this
# section, rerun, and read the path each time. Run each candidate a few
# times: near the edges, luck decides. Then write your finding:
#
# RED-TEAM REPORT - package delivery reward, tested by: ___
# bonus +5:   what happened? ___
# bonus +0.5: what happened (run it several times)? ___
# safe bonus corridor: ___ to ___
# why no bonus can ever mean "pay once": ___
