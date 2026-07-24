import random

from pacman_world import ACTIONS, PacmanWorld, play

world = PacmanWorld()


def random_move(world):
    return random.choice(ACTIONS)


play(world, random_move)
