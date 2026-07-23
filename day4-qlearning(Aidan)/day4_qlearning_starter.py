# Days 4-5 - Q-Learning starter file
# Build the world first, test it, then the Q-table, then the training
# loop. Keep everything in this one file, top to bottom.
#
# The grid:
#     0  1  2
#     3  4  5      start = 0, goal = 8 (+10), trap = 4 (-10),
#     6  7  8      every ordinary step costs -1




import random
grid = [
   [0,1,2],
   [3,4,5],
   [6,7,8]
]


# --- Section 7: the environment ---------------------------------------
def step(state, action):
   row = state // 3      # // is integer division: it divides and throws away the remainder
   col = state % 3       # % is modulo: it gives ONLY the remainder


   if action == "up" and row > 0:        # top-edge guard: only move if not in row 0
       row = row - 1
   elif action == "down" and row < 2:    # bottom-edge guard
       row = row + 1
   elif action=="left" and col>0:                            # HINT: "left", but only when col is not already 0
       col-=1                              # HINT: one column less
   elif action =="right" and col<2:                            # HINT: "right", but only when col is not already 2
       col+=1                              # HINT: one column more


   return grid[row][col]          # HINT: rebuild the single cell number from row and col - the grid is 3 wide


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
   if new_state == 8:          # reached the goal
       return 10, True         # big reward, and the episode ends
   elif new_state==4:                  # HINT: the trap cell
       return -10, True             # HINT: big penalty, and the episode also ends
   else:
       return -1, False             # HINT: an ordinary step - small cost, episode continues


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


# the shape of the Q-table, one inner dictionary per cell
Q = {}
for state in range(9):        # cells 0 through 8
   Q[state] = {}           # HINT: file a fresh EMPTY inner dictionary under this cell
   for a in actions:
       Q[state][a] = 0.0                  # HINT: inside that inner dictionary, start action a at quality 0.0

# print(Q[0])   # peek at cell 0's inner dictionary: all four actions at 0.0


# print(step(0, "right"))   # from cell 0, moving right -> should be 1
# print(step(0, "down"))    # from cell 0, moving down  -> should be 3
# print(step(0, "up"))      # tries to leave the top edge -> should STAY at 0
# print(step(3, "right"))   # from cell 3, moving right  -> should be 4 (the trap!)
# print(result(8))          # should print (10, True)
# print(result(4))          # should print (-10, True)
# print(result(1))          # should print (-1, False)
# # TODO: fill Q so every cell 0-8 has an inner dictionary with all
# # four actions starting at 0.0 - a loop inside a loop.


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
   best = Q[state]["up"]          # start by assuming "up" is best
   for a in actions:
       if best<Q[state][a]:                   # HINT: is this action's quality higher than the best so far?
           best = Q[state][a]           # HINT: remember the VALUE
   return best


def best_action(state):
   """Finds which action the agent currently believes is best.


   Args:
       state: A cell number, 0 through 8.


   Returns:
       The action string ("up", "down", "left", or "right") with
       the highest Q-value in this state.
   """
   # TODO: same scan, but return the NAME of the best action
   best_a = "up"                  # start by assuming "up" is best
   best = Q[state]["up"]
   for a in actions:
       if Q[state][a] > best:     # found a better one?
           best = Q[state][a]     # remember its value
           best_a = a         # HINT: AND remember which action owned it
   return best_a


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
for episode in range(2000):        # live through 2000 full episodes
   state = 0                      # every episode starts at the top-left corner
   done = False
   while not done:                # keep moving until this episode ends
       # choose an action with the epsilon-greedy rule from page 6
       if random.random() < epsilon:
           action = actions[random.randrange(0,4)]                      # HINT: explore - a random choice from the actions list
       else:
           action = best_action(state)                      # HINT: exploit - this state's best known move


       new_state = step(state,action)                      # HINT: where does this action land us? (your step function)
       reward, done = result(new_state)                   # HINT: judge the landing - your result function returns both at once


       # the update rule from page 5, in code
       old = Q[state][action]
       if done:
           target = reward                      # HINT: terminal move - no future to look at, just the reward
       else:
           target = reward+discount*best_value(new_state)                      # HINT: reward, plus discount times the best value of the NEW state
       Q[state][action] = old+learning_rate*(target-old)                # HINT: nudge old toward target by the learning rate - page 5's rule, one line


       state = new_state          # step onto the new cell and loop again
# --- Section 9: watch what it learned ------------------------------------
# for state in range(9):
#    print("cell", state, "->", best_action(state))


state = 0
path = [state]
done = False
steps = 0
while not done and steps < 20:   # cap: a lost agent prints evidence instead of freezing
    action = best_action(state)
    state = step(state, action)
    reward, done = result(state)
    path.append(state)
    steps = steps + 1
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


# print("value map:")
# for row in range(3):
#     line = ""
#     for col in range(3):
#         state = row * 3 + col
#         line = line + str(round(best_value(state), 1)) + "\t"
#     print(line)

def train_and_track(episodes, start_epsilon, decay = False):
    """Trains from scratch and returns a list of per-episode returns."""
    global Q
    Q = {}
    for state in range(9):                 # rebuild a fresh, zeroed Q-table
        Q[state] = {}                    # HINT: same two lines as your section-8 setup
        for a in actions:
            Q[state][a] = 0.0

    returns = []
    for episode in range(episodes):
        if decay:                                             # EDIT: insert these four lines
            # shrink from start_epsilon down toward 0 across the episodes
            epsilon = start_epsilon * (1 - episode / episodes)
        else:
            epsilon = start_epsilon

        state = 0
        state = 0
        done = False
        total_reward = 0                             # NEW: this episode's running tally
        while not done:
            if random.random() < epsilon:
                action = actions[random.randrange(1,4)]                       # HINT: same line as your section-8 loop
            else:
                action = best_action(state)                        # HINT: same as section 8
            new_state = step(state, action)                         # HINT: same as section 8
            reward, done =  result(new_state)                     # HINT: same as section 8
            total_reward = total_reward + reward     # NEW: tally this episode's reward

            old = Q[state][action]
            if done:
                target = reward                        # HINT: same as section 8
            else:
                target = reward+discount*best_value(new_state)                      # HINT: reward, plus discount times the best value of the NEW state
            Q[state][action] = old+learning_rate*(target-old)                 # HINT: same as section 8
            state = new_state
        returns.append(total_reward)                 # NEW: record the finished episode's return
    return returns

# random.seed(0)                         # so you get the same numbers as below

# returns = train_and_track(2000, 0.1)
# print("first 15 returns:", returns[:15])

random.seed(0)
fixed = train_and_track(2000, 0.1)               # fixed epsilon = 0.1
random.seed(0)
decayed = train_and_track(2000, 0.3, decay=True) # starts at 0.3, fades to 0

print("fixed   epsilon, last-100 average return:", sum(fixed[-100:]) / 100)
print("decayed epsilon, last-100 average return:", sum(decayed[-100:]) / 100)
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



