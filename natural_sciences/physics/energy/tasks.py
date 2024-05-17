#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi, sin, cos, radians


def task1():
    m = randint(4, 10)
    d = randint(5, 20)
    fp = randint(40, 100)
    ff = randint(20, 35)

    print(f"what is the work done by each force when a {m}kg trashcan is being pulled for {d}m? what will be the speed of the trashcan after {d}m? pull force = {fp}N and friciton force = {ff}N")
    input()

    ## SOLUTION

    wp = d * fp * int(cos(radians(0)))
    wf = d * ff * int(cos(radians(180)))

    wsum = wp + wf
    speed = round(sqrt(wsum / (1/2 * m)), 2)

    print(f"pull work = {wp} J")
    print(f"friction work = {wf} J")
    print(f"speed after {d} meters = {speed} m/s")


def task2():
    m, h = [randint(1, 10) for i in range(2)]
    g = 9.8

    print(f"how much work has to be done to lift a {m}kg object {h}m in the air? what is the object's gravitational potential energy at the top?")
    input()

    ## SOLUTION

    w = int(round(g * m * h * cos(radians(0)), 0))

    print(f"w = {w} J")


def task3():
    me = randint(5, 6)
    ve = randint(6, 10)
    mc = 1

    print(f"An African elephant is charging (m = {me}t, v = {ve}m/s). How fast would a {mc}kg cannon ball travel if it had the same kinetic energy as the elephant?")
    input()

    ## SOLUTION

    me *= 1000

    # Kc = Ke
    # (mc * v**2) / 2 = (m * v**2) / 2
    v = round(sqrt((me * ve**2) / mc), 2)

    print(f"v = {v} m/s")


def task4():
    Ed = round(uniform(1, 2), 3)
    mr = randint(50, 200)
    mp = randint(800, 1200)

    print(f"Hydrazine rocket propellant has an energy density Ed = {Ed} MJ/kg. Suppose a {mr} kg rocket is loaded with {mp} kg of hydrazine. What velocity could it achieve? To keep things simple, let's assume that the propellant is burned up very quickly and that the rocket is not subject to any external forces.")
    input()

    ## SOLUTION

    Ed *= 1000000

    # ((mr * v**2) / 2) = Ed * mp
    v = round(sqrt((2 * Ed * mp) / mr), 2)

    print(f"v = {v} m/s")


def task5():
    m = randint(10, 20)
    d = randint(5, 20)
    angle = randint(2, 4) * 10
    friction = round(uniform(0.1, 0.5), 1)
    g = 9.8

    print(f"Jakou práci vykonáme, posuneme-li rovnoměrným pohybem těleso o hmotnosti {m} kg do vzdálenosti {d} m vzhůru po nakloněné rovině, která svírá s vodorovnou rovinou úhel {angle} stupňů? Součinitel smykového tření mezi tělesem a rovinou je {friction}.")
    input()

    ## SOLUTION

    # There is no acceleration and the velocity should be constant -- no matter
    # what it is. We have to have enough force to go against gravity AND to go
    # against friction. So the force needed should be equal to the force of
    # gravity + the force of friction.

    Fg = m * g * sin(radians(angle))
    Ff = m * g * cos(radians(angle)) * friction
    W  = int(round((Fg + Ff) * d, 0))

    print(f"W = {W} J")


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
