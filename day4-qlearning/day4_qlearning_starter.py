# Days 4-5 - Q-Learning starter file
# Build the world first, test it, then the Q-table, then the training
# loop. Keep everything in this one file, top to bottom.
#
# The grid:
#     0  1  2
#     3  4  5      start = 0, goal = 8 (+10), trap = 4 (-10),
#     6  7  8      every ordinary step costs -1

import random


# --- Section 7: the environment ---------------------------------------
def step(state, action):
    """Moves the agent one cell in the grid, respecting the edges.

    Args:
        state: The current cell number, 0 through 8.
        action: One of "up", "down", "left", or "right".

    Returns:
        The cell number the agent lands on. Moving into a wall
        returns the SAME cell (the agent bumps and stays put).
    """

    # Turn the cell number into a row and a column using the
    # integer-division-and-remainder trick from page 7. Then change
    # the row or the column for the chosen action, but ONLY when the
    # move stays on the grid (check the edges!). Finally rebuild the
    # single cell number from the row and column and return it.

    row = state // 3  # // is integer division: it divides and throws away the remainder
    col = state % 3  # % is modulo: it gives ONLY the remainder

    if action == "up" and row > 0:  # top-edge guard: only move if not in row 0
        row = row - 1
    elif action == "down" and row < 2:  # bottom-edge guard
        row = row + 1
    elif action == "left" and col > 0:  # "left", but only when col is not already 0
        col -= 1  # one column less
    elif action == "right" and col < 2:  # "right", but only when col is not already 2
        col += 1  # one column more

    return (
        row * 3
    ) + col  # rebuild the single cell number from row and col - the grid is 3 wide


def result(new_state):
    """Judges a landing spot: what reward, and is the episode over?

    Args:
        new_state: The cell number the agent just landed on.

    Returns:
        Two values: (reward, done). reward is the number the world
        pays for this landing; done is True only when the episode
        ends (goal or trap).
    """

    # Return TWO things separated by a comma: (reward, done).
    # The goal and the trap end the episode with their big rewards;
    # every ordinary step costs a little (the map on page 3 has the
    # exact numbers).

    if new_state == 8:
        return 10, True
    elif new_state == 4:
        return -10, True
    else:
        return -1, False


# ---- TESTS for section 7 -----------------------------------------------
# WHEN TO RUN: right after you finish step() and result(), before you
# build the agent. Un-comment this block and re-run the file; every line
# should print PASS. (The check() helper is defined near the bottom.)
#
# check("step 0 right -> 1", step(0, "right"), 1)
# check("step 0 down -> 3",  step(0, "down"),  3)
# check("step 0 up stays 0 (edge guard)", step(0, "up"), 0)
# check("step 3 right -> 4 (the trap)",   step(3, "right"), 4)
# check("result(8) is goal",  result(8), (10, True))
# check("result(4) is trap",  result(4), (-10, True))
# check("result(1) is a step", result(1), (-1, False))

# --- Section 8: the Q-table and helpers ---------------------------------
actions = ["up", "down", "left", "right"]

Q = {}
for state in range(9):  # cells 0 through 8
    Q[state] = {}  # HINT: file a fresh EMPTY inner dictionary under this cell
    for a in actions:
        Q[state][a] = (
            0.0  # HINT: inside that inner dictionary, start action a at quality 0.0
        )

# print(Q[0])  # peek at cell 0's inner dictionary: all four actions at 0.0


def best_value(state):
    """Finds the agent's highest quality estimate for a state.

    Args:
        state: A cell number, 0 through 8.

    Returns:
        The largest number among Q[state]'s four action values.
        The update rule uses this as "best next estimate".
    """

    best = Q[state]["up"]  # start by assuming "up" is best
    for a in actions:
        if (
            Q[state][a] > best
        ):  # HINT: is this action's quality higher than the best so far?
            best = Q[state][a]  # HINT: remember the VALUE
    return best


def best_action(state):
    """Finds which action the agent currently believes is best.

    Args:
        state: A cell number, 0 through 8.

    Returns:
        The action string ("up", "down", "left", or "right") with
        the highest Q-value in this state.
    """
    best_a = "up"  # start by assuming "up" is best
    best = Q[state]["up"]
    for a in actions:
        if Q[state][a] > best:  # found a better one?
            best = Q[state][a]  # remember its value
            best_a = a  # HINT: AND remember which action owned it
    return best_a  # HINT: hand back the NAME, not the number


# --- Section 8: the training loop ----------------------------------------
learning_rate = 0.5
discount = 0.9
epsilon = 0.1

for episode in range(2000):  # live through 2000 full episodes
    state = 0  # every episode starts at the top-left corner
    done = False
    while not done:  # keep moving until this episode ends
        # choose an action with the epsilon-greedy rule from page 6
        if random.random() < epsilon:
            action = random.choice(
                actions
            )  # HINT: explore - a random choice from the actions list
        else:
            action = best_action(state)  # HINT: exploit - this state's best known move

        new_state = step(
            state, action
        )  # HINT: where does this action land us? (your step function)
        reward, done = result(
            new_state
        )  # HINT: judge the landing - your result function returns both at once

        # the update rule from page 5, in code
        old = Q[state][action]
        if done:
            target = (
                reward  # HINT: terminal move - no future to look at, just the reward
            )
        else:
            target = reward + (
                discount * best_value(new_state)
            )  # HINT: reward, plus discount times the best value of the NEW state
        Q[state][action] += (
            learning_rate * target - old
        )  # HINT: nudge old toward target by the learning rate - page 5's rule, one line

        state = new_state  # step onto the new cell and loop again

# print(Q[0])

# --- Section 9: watch what it learned ------------------------------------
for state in range(9):
    print("cell", state, "->", best_action(state))

state = 0
path = [state]
done = False
steps = 0
while not done and steps < 20:  # cap: a lost agent prints evidence instead of freezing
    action = best_action(state)
    state = step(state, action)
    reward, done = result(state)
    path.append(state)
    steps = steps + 1
print(
    "path:", path
)  # hoping for: [0, 1, 2, 5, 8] (mirror [0, 3, 6, 7, 8] is just as good)


# ======================================================================
# TESTS - check your own work, no peeking at the solution needed.
# Un-comment each block ABOVE as you reach that section and re-run the
# file: section 7's tests after step()/result(), section 8's after the
# Q-table and training loop. Each line prints PASS or FAIL.
# ======================================================================


def check(label, got, expected):
    """Prints PASS/FAIL for one test (provided - you don't edit this)."""
    mark = "PASS" if got == expected else "FAIL"
    extra = "" if got == expected else "   (got " + repr(got) + ")"
    print(mark, label, extra)


# ---- TESTS for section 8 -----------------------------------------------
# WHEN TO RUN: after the Q-table is filled and best_value/best_action
# are written (you can run these before training). Un-comment and re-run.
#
# Q[0] = {"up": 1.0, "down": 5.0, "left": 2.0, "right": 3.0}   # a known state
# check("best_value picks the max value", best_value(0), 5.0)
# check("best_action picks the max's name", best_action(0), "down")
# Q[0] = {a: 0.0 for a in actions}   # reset so training starts clean

# ---- TEST for the trained agent (section 8, after training) ------------
# WHEN TO RUN: after your training loop has run. Following the greedy
# policy from the start should walk all the way to the goal (cell 8).
# The exact route can vary, so we only check that it arrives.

s = 0
done = False
steps = 0
while not done and steps < 20:
    s = step(s, best_action(s))
    reward, done = result(s)
    steps = steps + 1
check("trained policy reaches the goal (cell 8)", s, 8)

print("value map:")
for row in range(3):
    line = ""
    for col in range(3):
        state = row * 3 + col
        line = line + str(round(best_value(state), 1)) + "\t"
    print(line)


def train_and_track(episodes, start_epsilon, decay=False):
    """Trains from scratch and returns a list of per-episode returns."""

    global Q
    Q = {}
    for state in range(9):  # cells 0 through 8
        Q[state] = {}  # HINT: file a fresh EMPTY inner dictionary under this cell
        for a in actions:
            Q[state][a] = (
                0.0  # HINT: inside that inner dictionary, start action a at quality 0.0
            )

    returns = []
    for episode in range(episodes):  # live through 2000 full episodes
        if decay:  # EDIT: insert these four lines
            # shrink from start_epsilon down toward 0 across the episodes
            epsilon = start_epsilon * (1 - episode / episodes)
        else:
            epsilon = start_epsilon

        state = 0  # every episode starts at the top-left corner
        done = False
        total_reward = 0
        while not done:  # keep moving until this episode ends
            # choose an action with the epsilon-greedy rule from page 6
            if random.random() < epsilon:
                action = random.choice(
                    actions
                )  # HINT: explore - a random choice from the actions list
            else:
                action = best_action(
                    state
                )  # HINT: exploit - this state's best known move

            new_state = step(state, action)  # HINT: where does this action land us? (your step function)
            reward, done = result(new_state)  # HINT: judge the landing - your result function returns both at once
            total_reward += reward

            # the update rule from page 5, in code
            old = Q[state][action]
            if done:
                target = reward  # HINT: terminal move - no future to look at, just the reward
            else:
                target = reward + (discount * best_value(new_state))  # HINT: reward, plus discount times the best value of the NEW state
            Q[state][action] += (learning_rate * target - old)  # HINT: nudge old toward target by the learning rate - page 5's rule, one line

            state = new_state
        returns.append(total_reward)  # NEW: record the finished episode's return
    return returns

def run_gridworld(size, goal, trap, episodes):
    """Trains a Q-learning agent on a size-by-size grid; returns its path."""
    actions = ["up", "down", "left", "right"]

    def step(state, action):
        row = state // size              # size, not 3
        col = state % size
        if action == "up" and row > 0:
            row = row - 1
        elif action == "down" and row < size - 1:   # size - 1, not 2
            row = row + 1
        elif action == "left" and col > 0:                       # HINT: "left" - unchanged from your section-7 step
            col -= 1
        elif action == "right" and col < size - 1:                       # HINT: "right" - but the far edge is now size - 1
            col += 1
        return (row * size) + col                      # HINT: rebuild with size where the 3 used to be

    def result(new_state):
        if new_state == goal:            # the goal you passed in, not a hard-coded 8
            return 10, True
        elif new_state == trap:                       # HINT: the trap you passed in
            return -10, True
        else:
            return -1, False

    Q = {}
    for state in range(size * size):     # size*size cells now
        Q[state] = {}                  # HINT: same two lines as your section-8 setup
        for a in actions:
            Q[state][a] = 0.0

    def best_value(state):
        return max(Q[state][a] for a in actions)   # a one-line shortcut for your whole scan!

    # ...and paste your own best_action from section 8 here, unchanged.

    def best_action(state):
        """Finds which action the agent currently believes is best.

        Args:
            state: A cell number, 0 through 8.

        Returns:
            The action string ("up", "down", "left", or "right") with
            the highest Q-value in this state.
        """
        best_a = "up"  # start by assuming "up" is best
        best = Q[state]["up"]
        for a in actions:
            if Q[state][a] > best:  # found a better one?
                best = Q[state][a]  # remember its value
                best_a = a  # HINT: AND remember which action owned it
        return best_a  # HINT: hand back the NAME, not the number

    learning_rate = 0.5
    discount = 0.9
    epsilon = 0.1
    for episode in range(episodes):  # live through 2000 full episodes
        state = 0  # every episode starts at the top-left corner
        done = False
        steps = 0
        while not done:  # keep moving until this episode ends
            # choose an action with the epsilon-greedy rule from page 6
            # print("in this loop")
            if random.random() < epsilon:
                action = random.choice(actions)  # HINT: explore - a random choice from the actions list
            else:
                action = best_action(state)  # HINT: exploit - this state's best known move

            new_state = step(state, action)  # HINT: where does this action land us? (your step function)
            reward, done = result(new_state)  # HINT: judge the landing - your result function returns both at once
            # the update rule from page 5, in code
            old = Q[state][action]
            if done:
                target = reward  # HINT: terminal move - no future to look at, just the reward
                
            else:
                target = reward + discount * best_value(new_state) - old  # HINT: reward, plus discount times the best value of the NEW state

            Q[state][action] += learning_rate * target # HINT: nudge old toward target by the learning rate - page 5's rule, one line

            state = new_state  # step onto the new cell and loop again
            steps +=1
        # print("out of this loop")
    # follow the finished policy from the start corner
    state = 0
    path = [0]
    done = False
    steps = 0
    while not done and steps < 200:
        state = step(state, best_action(state))
        reward, done = result(state)
        path.append(state)
        steps += 1
    return path


# random.seed(0)                         # so you get the same numbers as below

# returns = train_and_track(2000, 0.1)
# print("first 15 returns:", returns[:15])

# random.seed(0)
# fixed = train_and_track(2000, 0.1)  # fixed epsilon = 0.1
# random.seed(0)
# decayed = train_and_track(2000, 0.3, decay=True)  # starts at 0.3, fades to 0

# print("fixed   epsilon, last-100 average return:", sum(fixed[-100:]) / 100)
# print("decayed epsilon, last-100 average return:", sum(decayed[-100:]) / 100)

random.seed(0)
print(run_gridworld(5, 24, 12, 200))