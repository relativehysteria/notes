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

    # is equal to the momentum of the system post-crash
    v_post = round(p_pre / (m1 + m2), 2)

    print(f"v = {v_post} m/s")


def task2():
    m  = randint(1, 10) / 10
    t  = randint(1, 2) / 100
    v1 = randint(6, 10)
    v2 = randint(2, 5)

    print(f"A ball of mass {m}kg flies at the speed {v1}m/s and crashes into an object, touching it for {t}s. It then flies in the opposite direction at the speed {v2}m/s. What was the impulse on the ball from the object? What was the average force on the object from the ball? What was the ball on the ball from the object?")
    input()

    ## SOLUTION
    # impulse is the change in momentum
    i = abs(round((m * v2) - (m * v1), 2))

    # momentum = F * t
    # impulse  = F * delta t
    f = i / t

    print(f"impulse = {i} kg m/s")
    print(f"average force on the object = {f} N")
    print(f"forces on the object and the ball are equal.")


def task3():
    m1 = 500
    m2 = 2
    v2 = 200
    alpha = randint(20, 50)

    print(f"Consider a wheeled, {m1}kg cannon firing a {m2}kg ball horizontally from a ship. The ball leaves the cannon at {v2}m/s. At what speed does the cannon recoil as a result? What would its speed be, if the ball was fired at a {alpha} degree angle?")
    input()

    ## SOLUTION

    alpha = radians(alpha)

    # m1*v1 = m2*v2
    v1 = (m2 * v2) / m1
    v1alpha = round((m2 * (v2 * cos(alpha))) / m1, 2)

    print(f"v = {v1} m/s")
    print(f"tilted v = {v1alpha} m/s")


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
