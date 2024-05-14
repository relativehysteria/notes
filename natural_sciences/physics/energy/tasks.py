#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi, sin, cos, radians


def task1():
    task_text = "what is the work done by each force when a {m}kg trashcan is being pulled for {d}m? what will be the speed of the trashcan after {d}m? pull force = {fp}N and friciton force = {ff}N"

    m = randint(4, 10)
    d = randint(5, 20)
    fp = randint(40, 100)
    ff = randint(20, 35)

    print(task_text.format(m=m, d=d, fp=fp, ff=ff))
    input()

    ## SOLUTION

    wp = d * fp * int(cos(radians(0)))
    wf = d * ff * int(cos(radians(180)))

    wsum = wp + wf
    speed = round(sqrt(wsum / (1/2 * m)), 2)

    print(f"pull work = {wp} Joule")
    print(f"friction work = {wf} Joule")
    print(f"speed after {d} meters = {speed} m/s")


def task2():
    task_text = "how much work has to be done to lift a {m}kg object {h}m in the air? what is the object's gravitational potential energy at the top?"

    m, h = [randint(1, 10) for i in range(2)]
    g = 9.8

    print(task_text.format(m=m, h=h))
    input()

    ## SOLUTION

    w = int(round(g * m * h * cos(radians(0)), 0))

    print(f"w = {w} Joule")


# choose a random task and execute it
task = choice([t for t in locals().keys() if t.startswith('task')])
locals()[task]()
