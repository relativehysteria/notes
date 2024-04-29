#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi


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


# choose a random task and execute it
task = choice([t for t in locals().keys() if t.startswith('task')])
locals()[task]()
