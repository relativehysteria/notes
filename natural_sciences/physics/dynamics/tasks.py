#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt, pi, sin, cos, radians


def task1():
    m  = randint(300, 500)
    t  = randint(1, 5)
    v1 = randint(10, 30)
    v2 = randint(40, 80)

    print(f"Jak velkou silou působí lokomotiva na vagón hmotnosti {m} t, který jede po vodorovné rovině, jestliže se jeho rychlost zvýší za {t} minuty z {v1} km/h na {v2} km/h?")
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
    m  = round(uniform(3, 5), 1)
    a  = round(uniform(1, 5), 1)
    g  = 9.8
    Ff = randint(2, 10)

    print(f"A {m} kg package of kiwi flavored bubble gum is being delivered to the top floor of an office building. The box sits on the floor of an elevator which accelerates upward with an acceleration of magnitude a = {a} m/s^2. The delivery person is also resting one foot on the package exerting a downward force on the package of magnitude {Ff} N. What is the normal force on the package exerted by the floor of the elevator?")
    input()

    ## SOLUTION

    F = round(a * m + m * g + Ff, 2)
    print(f"F = {F} N")


def task3():
    m     = round(uniform(1, 2), 1)
    Fa    = randint(1, 20)
    angle = randint(10, 50)
    g     = 9.8
    a     = 0

    print(f"A person is pushing a {m} kg box of mint chocolate chip cookies across a frictionless table with a downward diagonal force Fa = {Fa} N at an angle of {angle} degrees. What is the normal force exerted on the box of cookies by the table?")
    input()

    ## SOLUTION

    F = round(a * m + g + Fa * sin(radians(angle)), 2)
    print(f"F = {F} N")


def task4():
    m = randint(1, 10)
    angle = randint(20, 40)
    g = 9.8

    print(f"A box weighing {m} kg is standing on an inclined plane at the {angle} degree angle. What is the box's normal force and its inclined downwards force (perpendicular to the normal force)? What is its downwards acceleration?")
    input()

    ## SOLUTION

    Fnorm = round(cos(radians(angle)) * m * g, 1)
    Fperp = round(sin(radians(angle)) * m * g, 1)
    a = round(Fperp / m, 1)

    print(f"F normal = {Fnorm} N")
    print(f"F perpendicular = {Fperp} N")
    print(f"a = {a} m/s")


def task5():
    m = randint(10, 20) * 10
    static  = randint(5, 6) / 10
    kinetic = randint(3, 4) / 10
    g = 9.8

    print(f"An initially stationary {m} kg refrigerator sits on the floor. The coefficiont of static friction is {static} and the coefficient of kinetic friction is {kinetic}. Calculate the minimum magnitude of the force needed to overcome static friction and the magnitude of the kinetic force when the fridge is moving.")
    input()

    ## SOLUTION

    Fnorm = m * g

    # minimum required force to start moving
    min_static = round(Fnorm * static, 1)
    kinetic = round(Fnorm * kinetic, 1)

    print(f"minimum force required to move: {min_static} N")
    print(f"kinetic force: {kinetic} N")


def task6():
    print("Tělesu o hmotnosti m uděluje síla o velikosti F zrychlení 2 m/s^2. Jak velké zrychlení uděluje témuž tělesu síla o velikosti a) 4F, b) F/4?")
    input()

    print("a) 8 m/s^2")
    print("b) 0.5 m/s^2")


def task7():
    print("Tělesu o hmotnosti m uděluje síla o velikosti F zrychlení 2 m/s^2. Jak velké zrychlení uděluje stejně velká síla tělesu o hmotnosti a) 4m, b) m/4?")
    input()

    print("a) 0.5 m/s^2")
    print("b) 8 m/s^2")


def task8():
    t  = randint(5, 20)
    d  = randint(10, 100)
    m  = randint(60, 90)
    Fr = randint(1, 20)

    print(f"Cyklista ujel při rozjíždění z klidu za {t} s vzdálenost {d} m. Jak velkou stálou sílu svým šlapáním vyvíjel, musel-li současně překonávat odporové síly o velikosti {Fr} N? Hmotnost cyklisty včetně kola je {m} kg.")
    input()

    ## SOLUTION

    # a = delta v / t
    # d / t = (vf + v0) / 2
    # delta v = 2d / t
    a = (2 * d) / t**2
    F = round(m * a + Fr, 2)

    print(f"F = {F} N")


def task9():
    m  = randint(10, 14) * 100
    v0 = randint(50, 70)
    vf = randint(75, 100)
    t  = randint(5, 20)

    print(f"Automobil o hmotnosti {m} kg zvětšil rychlost ze {v0} km/h na {vf} km/h za dobu {t} s. a) Jak velká síla tuto změnu rychlosti způsobila? b) Jakou vzdálenost při zvětšující se rychlosti automobil urazil?")
    input()

    ## SOLUTION

    v0 /= 3.6
    vf /= 3.6

    d = int(round(t * ((v0 + vf) / 2), 2))
    a = (vf - v0) / t
    F = int(round(m * a, 2))

    print(f"a) F = {F} N")
    print(f"b) d = {d} m")


def task10():
    m = randint(200, 500)
    F = randint(200, 250)
    t = 0.01

    print(f"Hráč vykopl míč o hmotnosti {m} g silou {F} N. Jak velkou rychlost bude mít míč při opuštění kopačky, jestliže na něj působila nárazová síla po dobu {t} s? Předpokládejte, že míč byl před vykopnutím v klidu.")
    input()

    ## SOLUTION

    m /= 1000
    v = round((F * t) / m, 1)

    print(f"v = {v} m/s")


def task11():
    g = 9.8
    mg = randint(8, 12) * 1000 * g
    F = randint(10, 18) * 1000
    vf = randint(40, 70)

    print(f"Motor auta o tíze {mg} N má tažnou sílu {F} N. Za jaký čas může auto z klidu dosáhnout rychlost {vf} km/h? Odpor vzduchu a tření zanedbejte.")
    input()

    ## SOLUTION

    vf /= 3.6

    a = F / (mg / g)
    t = round(vf / a, 1)

    print(f"t = {t} s")


def task12():
    m1 = randint(1, 10)
    m2 = randint(1, 10)
    g  = 9.8

    print(f"Dvě tělesa o hmotnostech {m1} kg a {m2} kg jsou spojena vláknem přes kladku o zanedbatelné hmotnosti. První těleso je položeno na stole a druhé těleso je z kladky vyvěšeno dolů. Určete velikost zrychlení jednotlivých těles a velikost tahové síly, kterou je napínáno vlákno. Tření neuvažujeme.")
    input()

    ## SOLUTION

    a = (m2 * g) / (m1 + m2)
    F = m1 * a

    print(f"a = {round(a, 1)} m/s")
    print(f"F = {round(F, 1)} N")


def task13():
    m1 = randint(1, 5)
    m2 = randint(6, 10)
    d  = randint(1, 3)
    g  = 9.8

    print(f"Na pevné kladce visí 2 tělesa o hmotnosti {m1} kg a {m2} kg. Těleso o menší hmotnosti se nachází ve vzdálenosti {d} m pod tělesem o větší hmotnosti. Za jakou dobu budou obě tělesa ve stejné výšce?")
    input()

    ## SOLUTION

    F = (m2 - m1) * g
    a = F / (m1 + m2)
    t = sqrt(d / a)

    print(f"t = {round(t, 2)} s")


def task14():
    m = randint(50, 80)
    angle = randint(5, 20)
    g = 9.8

    print(f"A person (m = {m} kg) is standing on a wire. The wire is bent at a {angle} degree angle. What is the tension in the wire?")
    input()

    ## SOLUTION
    # calculate the weight of the person. because they're supported by the
    # wire on both sides, their effective weight is halved
    F = (m * g) / 2

    # weight is the vertical component; tension is the hypotenuse,
    # so T * sin(radians(angle)) = m * g / 2
    T = F / sin(radians(angle))

    print(f"T = {round(T, 2)} N")


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    #locals()[task]()
    task14()
