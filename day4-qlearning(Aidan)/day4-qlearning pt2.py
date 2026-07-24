import random


def run_gridworld(size, goal, trap, episodes):
    """Trains a Q-learning agent on a size-by-size grid; returns its path."""
    actions = ["up", "down", "left", "right"]

    def step(state, action):
        row = state // size  # size, not 3
        col = state % size
        if action == "up" and row > 0:
            row = row - 1
        elif action == "down" and row < size - 1:  # size - 1, not 2
            row = row + 1
        elif ____ or ____:  # HINT: "left" - unchanged from your section-7 step
            ____
        return ____  # HINT: rebuild with size where the 3 used to be

    def result(new_state):
        if new_state == goal:  # the goal you passed in, not a hard-coded 8
            return 10, True
        elif ____:  # HINT: the trap you passed in
            return ____
        else:
            return ____

    Q = {}
    for state in range(size * size):  # size*size cells now
        Q[state] = ____  # HINT: same two lines as your section-8 setup
        for a in actions:
            ____

    def best_value(state):
        return max(
            Q[state][a] for a in actions
        )  # a one-line shortcut for your whole scan!

    # ...and paste your own best_action from section 8 here, unchanged.

    learning_rate = 0.5
    discount = 0.9
    epsilon = 0.1
    for episode in range(episodes):
        state = 0
        done = False
        steps = 0
        while not done and steps < 200:  # 200-move safety cap
            if random.random() < epsilon:
                action = (
                    ____  # HINT: this whole body is your section-8 loop, line for line
                )
            else:
                action = ____
            new_state = ____
            reward, done = ____
            old = Q[state][action]
            if done:
                target = ____
            else:
                target = ____
            Q[state][action] = ____
            state = new_state
            steps = steps + 1  # the only new line: count moves for the cap

    # follow the finished policy from the start corner
    state = 0
    path = [0]
    done = False
    steps = 0
    while not done and steps < 200:
        state = step(state, best_action(state))
        reward, done = result(state)
        path.append(state)
        steps = steps + 1
    return path
