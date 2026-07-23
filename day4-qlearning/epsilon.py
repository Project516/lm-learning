import random

epsilon = 0.1
actions = ["up", "down", "left", "right"]
state = 0

if random.random() < epsilon:
    action = random.choice(actions)  # explore: try a random move
else:
    action = "up"  # exploit: (later, the best known move)

print("this turn the agent chose to", action)
