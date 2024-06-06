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


def task4():
    m_box = randint(1, 5)
    d_box = randint(1, 2)
    m_table = randint(1, 5)
    g = 9.8

    print(f"In 2nd dimension, a box weighing {m_box}kg is sitting on a table, {d_box}m away from the center. Weight of the table at its center of mass is {m_table}. Legs of the table are 3m away from the center. What forces are the legs exerting on the table?")
    input()

    ## SOLUTION

    g_box = m_box * g
    g_table = m_table * g

    # consider the left leg the pivot. the opposing forces must be equal, therefore
    # f_r * 6 = 3 * g_table + (3 - d_box) * g_box
    f_r = ((3 * g_table) + ((3 - d_box) * g_box)) / 6
    f_l = (3 * g_table) + ((3 - d_box) * g_box) - f_r

    print(f"Left leg = {round(f_l, 2)} N")
    print(f"Right leg = {round(f_r, 2)} N")


def task5():
    d = randint(1, 10)
    a = randint(20, 40)
    f = randint(10, 50)

    print(f"A plank rotates around its center. A force of {f} N is applied to it {d}m from its center at a {a} degree angle (pointing away from the center). What is the plank's torque?")
    input()

    ## SOLUTION

    tau = f * sin(radians(a)) * d

    print(f"tau = {round(tau, 2)} N*m")


def task6():
    f = [randint(1, 100) for i in range(randint(2, 5))]
    m = [randint(1, 10) for i in range(len(f))]

    print(f"A plank rotates around its axis, being anchored to it with one side. There are {len(f)} masses applying forces on the plank, each 1 meter farther (starting at 1m from the center). What is the plank's angular acceleration?")
    print(f"\nThe masses and the forces:")

    for (i, j) in zip(m, f):
        print(f"{i:>2}kg {j:>3}N")

    input()

    ## SOLUTION

    tau =     sum([((i+1) * F) for (i, F) in enumerate(f)])
    inertia = sum([((i+1)**2 * m) for (i, m) in enumerate(m)])
    alpha = round(tau / inertia, 2)

    print(f"alpha = {alpha} rad/s^2")


def task7():
    v = randint(10, 30)
    freq = randint(1, 10)
    r = randint(3, 4) / 10
    m = randint(2, 4) / 10

    print(f"A baseball weighing {m} kg is travelling through the air at {v} m/s. Its diameter is {r*2}m and it is rotating {freq}x/s. What is its total kinetic energy?")
    input()

    ## SOLUTION

    Kt = (m * v**2) / 2
    Kr = (m * r**2 * radians(360 * freq)**2) / 2
    K = round(Kt + Kr, 2)
    breakpoint()

    print(f"K = {K} J")



# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
