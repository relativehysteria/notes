#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi


def task1():
    r = randint(1, 10) * 10
    f = randint(1, 5)

    print(f"Hmotný bod koná rovnoměrný pohyb po kružnici o poloměru {r} cm s frekvencí {f} Hz. Určete periodu a velikost rychlosti hmotného bodu.")
    input()

    ## SOLUTION

    T = round(1 / f, 2)
    v = round(2 * pi * (r / 100) * f, 2)

    print(f"T = {T} s")
    print(f"v = {v} m/s")


def task2():
    t = round(uniform(1, 10), 1)

    print(f"Hmotný bod koná rovnoměrný pohyb po kružnici s oběžnou dobou {t} s. Určete jeho frekvenci a úhlovou rychlost")
    input()

    ## SOLUTION

    f = round(1 / t, 2)
    o = round((2 * pi) / t, 2)

    print(f"f = {f} Hz")
    print(f"o = {o} rad/s")


def task3():
    r = randint(1, 10)
    t, n = [randint(40, 80) for i in range(1, 3)]

    print(f"Kabina centrifugy, která je umístěna ve vzdálenosti {r}m od osy otáčení, vykoná za {t}s {n} otáček. Určete velikost její rychlosti a úhlovou rychlost")
    input()

    ## SOLUTION

    f = n / t
    v = round(2 * pi * r * f, 2)
    o = round(v / r, 2)

    print(f"v = {v} m/s")
    print(f"o = {o} rad/s")


def task4():
    n = randint(1, 4)

    print(f"Sekundová ručička hodinek je o {n}/4 delší než minutová. V jakém poměru jsou velikosti rychlostí jejich koncových bodů?")
    input()

    ## SOLUTION

    min_r = 1
    sec_r = min_r + (n/4)
    sec_T = 60
    min_T = sec_T * 60
    sec_v = (2 * pi * sec_r) / sec_T
    min_v = (2 * pi * min_r) / min_T

    print(f"s : m = {int(round(sec_v / min_v, 0))} : 1")


def task5():
    T_days = 365.25
    r_mil  = 150

    print(f"Země obíhá kolem Slunce přibližně rovnoměrným pohybem po kružnici za {T_days} dne. Jaká je oblouková rychlost Země, pokud vzdálenost Země - Slunce je přibližně {r_mil} milionů kilometrů.")
    input()

    ## SOLUTION

    T = T_days * 24 * 60 * 60
    r = 150 * 1000000 * 1000
    v = round((2 * pi * r) / T, 2)

    print(f"{v} m/s = {round(v / 1000, 2)} km/s")


def task6():
    r   = randint(5, 10)
    cog = round(uniform(0.5, 1), 1)

    print(f"Jakou nejmenší rychlost musí mít motocyklista, má-li jezdit na vnitřním povrchu duté koule o poloměru {r}m všemi směry? Těžiště motocyklu a jezdce je {cog}m od povrchu.")
    input()

    ## SOLUTION

    r = r - cog

    # a = v^2/r = g
    g = 9.8
    v = round(sqrt(r * g), 1)
    print(f"v = {v} km = {v * 3.6} m/s")


def task7():
    r = randint(2, 5) * 100
    f = randint(10, 20)

    print(f"Sedačka kolotoče je upevněna ve vzdálenosti {r} cm od středu otáčení a vykonává {f} otáček za minutu. Určitě jí obvodovou rychlost a dostředivé zrychlení")
    input()

    ## SOLUTION

    f = round(f / 60, 2)
    r = round(r / 100, 2)

    v = round(2 * pi * r * f, 2)
    a = round(v ** 2 / r, 2)

    print(f"v = {v} m/s")
    print(f"a = {a} m/s^2")


# choose a random task and execute it
task = choice([t for t in locals().keys() if t.startswith('task')])
locals()[task]()
