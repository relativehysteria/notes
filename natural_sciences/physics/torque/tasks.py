#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi, sin, cos, radians


def task1():
    d = randint(5, 30)
    m = [randint(1, 10) for i in range(3)]

    print(f"There are three apples on a horizontally placed branch. The branch is {d}cm long, the first apple is at the beginning, the second apple is in the perfect middle and the third apple is at the very end. Respectively, the weights of these apples are: {m}. Where is the center of mass of this branch?")
    input()

    ## SOLUTION

    center  = (m[1] * (d / 2)) + (m[2] * d)
    center /= sum(m)

    print(f"the center is at {round(center, 2)}cm")


def task2():
    m1, m2 = [randint(1, 20) for i in range(2)]
    d1 = randint(1, 10)
    g = 9.8

    print(f"Two objects are placed on a seesaw. The first one of mass {m1}kg is placed {d1}m from the center. How far to the other side do we have to place the second object (m = {m2}kg) to balance the seesaw?")
    input()

    ## SOLUTION

    tau1 = (m1 * g) * d1
    d2   = tau1 / (m2 * g)

    print(f"d = {round(d2, 2)} m")


def task3():
    f_left, f_right = [[randint(-50, 50) for i in range(randint(1, 3))] for i in range(2)]
    d_left  = sorted([randint(1, 10) for i in range(len(f_left))])
    d_right = sorted([randint(1, 10) for i in range(len(f_right))])
    d_quest = randint(1, 10)

    print(f"{len(f_left) + len(f_right)} forces are applied to a seesaw, {len(f_left)} on the left side and {len(f_right)} on the right side.")

    print(f"\nHere are the forces and their distances to the LEFT of the seesaw:")
    for (f, d) in zip(f_left, d_left):
        print(f"  {f:>3}N, {d}m")

    print(f"\nHere are the forces and their distances to the RIGHT of the seesaw:")
    for (f, d) in zip(f_right, d_right):
        print(f"  {f:>3}N, {d}m")

    print(f"\nIf you wanted to balance the seesaw and were to apply a force {d_quest}m from the center, what should its magnitude be on a) the left side, b) the right side?")
    input()

    ## SOLUTION

    # first, get the net torque on each side
    net_tau_left  = sum([f * d for (f, d) in zip(f_left, d_left)])
    net_tau_right = sum([f * d for (f, d) in zip(f_right, d_right)])

    # then find the torque that would have to be applied {d_quest}m from the
    # center. on what side it is applied is just a question of changing the sign
    # because the distance asked for is the same on both sides.
    req_f_right = round((net_tau_right - net_tau_left) / d, 3)

    print(f"force required on the left side is:  {req_f_right:>8} N")
    print(f"force required on the right side is: {-req_f_right:>8} N")


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
