#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi, sin, radians


def task1():
    task_text = "Jak velkou silou působí lokomotiva na vagón hmotnosti {m} t, který jede po vodorovné rovině, jestliže se jeho rychlost zvýší za {t} minuty z {v1} km/h na {v2} km/h?"

    m  = randint(300, 500)
    t  = randint(1, 5)
    v1 = randint(10, 30)
    v2 = randint(40, 80)

    print(task_text.format(m=m, t=t, v1=v1, v2=v2))
    input()

    ## SOLUTION

    m  *= 1000
    t  *= 60
    v1 *= 10 / 36
    v2 *= 10 / 36

    a = (v2 - v1) / t
    F = round(m * a, 2)
    print(f"F = {F} N")


def task2():
    task_text = "A {m} kg package of kiwi flavored bubble gum is being delivered to the top floor of an office building. The box sits on the floor of an elevator which accelerates upward with an acceleration of magnitude a = {a} m/s^2. The delivery person is also resting one foot on the package exerting a downward force on the package of magnitude {Ff} N. What is the normal force on the package exerted by the floor of the elevator?"

    m  = round(uniform(3, 5), 1)
    a  = round(uniform(1, 5), 1)
    g  = 9.8
    Ff = randint(2, 10)

    print(task_text.format(m=m, a=a, Ff=Ff))
    input()

    ## SOLUTION

    F = round(a * m + m * g + Ff, 2)
    print(f"F = {F} N")


def task3():
    task_text = "A person is pushing a {m} kg box of mint chocolate chip cookies across a frictionless table with a downward diagonal force Fa = {Fa} N at an angle of {angle} degrees. What is the normal force exerted on the box of cookies by the table?"

    m     = round(uniform(1, 2), 1)
    Fa    = randint(1, 20)
    angle = randint(10, 50)
    g     = 9.8
    a     = 0

    print(task_text.format(m=m, Fa=Fa, angle=angle))
    input()

    ## SOLUTION

    F = round(a * m + g + Fa * sin(radians(angle)), 2)
    print(f"F = {F} N")


# choose a random task and execute it
task = choice([t for t in locals().keys() if t.startswith('task')])
#locals()[task]()
task3()
