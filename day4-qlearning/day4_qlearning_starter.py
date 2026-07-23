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
    # TODO: turn the cell number into a row and a column using the
    # integer-division-and-remainder trick from page 7. Then change
    # the row or the column for the chosen action, but ONLY when the
    # move stays on the grid (check the edges!). Finally rebuild the
    # single cell number from the row and column and return it.
    pass


def result(new_state):
    """Judges a landing spot: what reward, and is the episode over?

    Args:
        new_state: The cell number the agent just landed on.

    Returns:
        Two values: (reward, done). reward is the number the world
        pays for this landing; done is True only when the episode
        ends (goal or trap).
    """
    # TODO: return TWO things separated by a comma: (reward, done).
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
# TODO: fill Q so every cell 0-8 has an inner dictionary with all
# four actions starting at 0.0 - a loop inside a loop.


def best_value(state):
    """Finds the agent's highest quality estimate for a state.

    Args:
        state: A cell number, 0 through 8.

    Returns:
        The largest number among Q[state]'s four action values.
        The update rule uses this as "best next estimate".
    """
    # TODO: return the HIGHEST Q[state][action] across the four actions
    # ("best so far" pattern - start with Q[state]["up"])
    pass


def best_action(state):
    """Finds which action the agent currently believes is best.

    Args:
        state: A cell number, 0 through 8.

    Returns:
        The action string ("up", "down", "left", or "right") with
        the highest Q-value in this state.
    """
    # TODO: same scan, but return the NAME of the best action
    pass


# --- Section 8: the training loop ----------------------------------------
learning_rate = 0.5
discount = 0.9
epsilon = 0.1

# TODO: for 2000 episodes, starting each one at cell 0:
#   keep moving until the episode is done. Each move:
#     1. choose the action with the epsilon-greedy rule (page 6):
#        usually the best known action, occasionally a random one
#     2. take the step and judge the landing (your two functions)
#     3. nudge Q[state][action] toward the target with the update
#        rule from page 5 - and remember the terminal-move special
#        case where there is no next state to look ahead into
#     4. move on to the new state

# --- Section 9: watch what it learned ------------------------------------
# for state in range(9):
#     print("cell", state, "->", best_action(state))

# state = 0
# path = [state]
# done = False
# steps = 0
# while not done and steps < 20:   # cap: a lost agent prints evidence instead of freezing
#     action = best_action(state)
#     state = step(state, action)
#     reward, done = result(state)
#     path.append(state)
#     steps = steps + 1
# print("path:", path)     # hoping for: [0, 1, 2, 5, 8] (mirror [0, 3, 6, 7, 8] is just as good)


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
#
# s = 0
# done = False
# steps = 0
# while not done and steps < 20:
#     s = step(s, best_action(s))
#     reward, done = result(s)
#     steps = steps + 1
# check("trained policy reaches the goal (cell 8)", s, 8)
