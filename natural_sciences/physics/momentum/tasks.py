#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi, sin, cos, radians


def task1():
    m1 = randint(1, 3) * 1000
    m2 = randint(4, 5) * 1000
    v1 = randint(7, 20)

    print(f"A {m1}kg car crashes into a {m2}kg car at the speed of {v1}m/s. The cars then move together in the same direction at the same speed. What speed do they move at?")
    input()

    ## SOLUTION

    # momentum of the system pre-crash
    # p = m1v1 + m2v2
    p_pre  = (m1 * v1) + (m2 * 0)
    v_post = round(p_pre / (m1 + m2), 2)

    print(f"{v_post} m/s")


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
