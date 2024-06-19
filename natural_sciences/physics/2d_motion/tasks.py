#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi


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


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
