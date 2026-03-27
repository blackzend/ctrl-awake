import random
from pynput.mouse import Controller

mouse = Controller()

MAX_MOVE = 150  # px


def jiggle_mouse():
    x, y = mouse.position
    dx = random.randint(-MAX_MOVE, MAX_MOVE)
    dy = random.randint(-MAX_MOVE, MAX_MOVE)
    mouse.position = (x + dx, y + dy)