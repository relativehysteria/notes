#!/usr/bin/env python

from random import uniform, randint, choice
from math import *


def task_conceptual1():
    angle = randint(10, 40)
    distance = randint(10, 300)

    print(f"In vacuum, the range of a ball shot at the {angle} degree angle is {distance}m. The same range can be achieved if the ball is shot at what other angle?")
    input()

    ## SOLUTION
    # If you shoot it below 45 at some angle, you will achieve the same by
    # shooting it above 45 at the same angle, such that both angles always
    # add up to 90 degrees.

    print(f"{90 - angle} degrees")


def task1():
    x = randint(30, 35)
    g = 9.8

    print(f"The cannon on a battleship can fire a shell a maximum distance of {x} km.")
    print(f"a) Calculate the initial velocity of the shell")
    print(f"b) What maximum height does it reach?")
    input()

    ## SOLUTION

    x *= 1000

    # x = (v_0^2 * sin(2 * theta)) / g
    # maximum range is achieved at 45 degrees and sin(2 * 45) is 1, therefore
    # x = v_0^2 / g
    theta = radians(45)
    v0 = sqrt(x * g)

    # vfy = v0y + a t
    v0y = v0 * sin(theta)
    t = v0y / g

    # (vfy + v0y) / 2 = y / t
    y = (v0y / 2) * t

    print(f"a) {round(v0, 2)} m/s")
    print(f"b) {round(y, 2)} m")


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
