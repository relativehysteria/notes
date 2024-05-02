#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi, sin, cos, radians


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


def task4():
    task_text = "A box weighing {m} kg is standing on an inclined plane at the {angle} degree angle. What is the box's normal force and its inclined downwards force (perpendicular to the normal force)? What is its downwards acceleration?"

    m = randint(1, 10)
    angle = randint(20, 40)
    g = 9.8

    print(task_text.format(m=m, angle=angle))
    input()

    ## SOLUTION

    Fnorm = round(cos(radians(angle)) * m * g, 1)
    Fperp = round(sin(radians(angle)) * m * g, 1)
    a = round(Fperp / m, 1)

    print(f"F normal = {Fnorm} N")
    print(f"F perpendicular = {Fperp} N")
    print(f"a = {a} m/s")


def task5():
    task_text = "An initially stationary {m} kg refrigerator sits on the floor. The coefficiont of static friction is {static} and the coefficient of kinetic friction is {kinetic}. Calculate the minimum magnitude of the force needed to overcome static friction and the magnitude of the kinetic force when the fridge is moving."

    m = randint(10, 20) * 10
    static  = randint(5, 6) / 10
    kinetic = randint(3, 4) / 10
    g = 9.8

    print(task_text.format(m=m, static=static, kinetic=kinetic))
    input()

    ## SOLUTION

    Fnorm = m * g

    # minimum required force to start moving
    min_static = round(Fnorm * static, 1)
    kinetic = round(Fnorm * kinetic, 1)

    print(f"minimum force required to move: {min_static} N")
    print(f"kinetic force: {kinetic} N")

# choose a random task and execute it
task = choice([t for t in locals().keys() if t.startswith('task')])
locals()[task]()
