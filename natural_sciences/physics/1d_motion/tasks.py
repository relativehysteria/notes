#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt

def task1():
    task_text = "Na dovolenou jedete autem po dálnici {t0} hodin rychlostí {v0} km.h-1. Potom na {t1} hodin zastavíte. Pokračujete {t2} hodin stálou rychlostí {v2} km.h-1 až do cíle. Určete průměrnou rychlost cestování (v km/h)."

    t0, t1, t2 = [round(uniform(1.0, 5.0), 1) for i in range(3)]
    v0, v2 = [randint(50, 130) for i in range(2)]

    print(task_text.format(t0=t0, t1=t1, t2=t2, v0=v0, v2=v2))
    input()

    ## SOLUTION

    # prumerna rychlost pres ruzne vzdalenosti je harmonicky prumer vsech
    # vzdalenosti a jejich casu potrebneho k jejich prejezdu
    s0 = t0 * v0
    s1 = t1 *  0
    s2 = t2 * v2

    v = sum([s0, s1, s2]) / sum([t0, t1, t2])

    print(round(v, 2))


def task2():
    task_text = "Dálniční úsek má délku {s0} km. Největší povolená rychlost je {v0} km.hod-1. Řidič tento úsek projel za {t0} minut. Překročil největší povolenou rychlost na dálnici?"

    s0, v0 = [randint(50, 130) for i in range(2)]
    t0 = randint(10, 120)

    print(task_text.format(s0=s0, v0=v0, t0=t0))
    input()

    ## SOLUTION

    # nejdriv prevedem jednotky
    v0 *= 1000/3600
    s0 *= 1000
    t0 *= 60

    # pak zjistime ridicovu prumernou rychlost a checkneme, jestli prekracoval
    v = s0 / t0
    res = "ANO" if v > v0 else "NE"
    v = round(v * 3.6, 2)
    print(f"ridicova prumerna rychlost byla {v}km/h, takze {res}")


def task3():
    task_text = "Volně padající těleso má v bodě A rychlost {vA} ms-1, v níže položeném bodě B rychlost {vB} ms-1. Zjistěte, za jaký čas proletí vzdálenost A->B. Jaká je vzdálenost bodů A a B? Jakou rychlostí těleso dopadne, pokud jeho pohyb z bodu B na zem trvá ještě {tToGround} s. Předpokládej, že g = 9.8"

    g = 9.8
    vA, tToB, tToGround = sorted([randint(1, 5) for i in range(3)])
    vB = round(vA + g * tToB, 2)

    print(task_text.format(vA=vA, vB=vB, tToGround=tToGround))
    input()

    ## SOLUTION

    # vzdalenost mezi body: odvozeno od prumerne rychlosti, v latex syntaxu:
    # $\overline{v} = \frac{\Delta x}{t} = \frac{v_f + v_0}{2}$, z cehoz vychazi
    # $\Delta x = \frac{v_f + v_0}{2} \times t$
    deltaX = round(((vA + vB) / 2) * tToB, 2)

    # rychlost dopadu na zem je stejne pocitani, jako na zacatku,
    # jen se zacina od bodu B
    vGround = round(vB + g * tToGround, 2)

    print(f"casova vzdalenost mezi body: {tToB}s")
    print(f"prostorova vzdalenost mezi body: {deltaX}m")
    print(f"rychlost pri dopadu na zem: {vGround}ms-1")


def task4():
    task_text = "Plavec, jehož rychlost vzhledem na vodu je {v0} ms-1 plave v řece, v níž voda teče rychlostí {v1} ms-1. Určete čas, za který dopluje z místa A do B, vzdáleného {sAtoB} m, pokud plave:"
    task_text += "\na) po proudu"
    task_text += "\nb) proti proudu"
    task_text += "\nc) kolmo na proud (vysledná rychlost je kolmá rychlosti proudu)"

    v0, v1 = sorted([round(uniform(0.1, 1), 1) for i in range(2)], reverse=True)
    v0 = v0 + 0.1 if v1 == v0 else v0
    sAtoB = randint(50, 150)

    print(task_text.format(v0=v0, v1=v1, sAtoB=sAtoB))
    input()

    ## SOLUTION

    # a)
    t = round(sAtoB / (v0 + v1), 2)
    print(f"a) {t}s")

    # b)
    t = round(sAtoB / (v0 - v1), 2)
    print(f"b) {t}s")

    # c)
    t = round(sAtoB / sqrt(v0**2 - v1**2), 2)
    print(f"c) {t}s")


def task5():
    task_text = "Motorová loď plovoucí po řece projela vzdálenost {s0} m při plavbě po proudu za {t0}s, při plavbě proti proudu za {t1}s. Určitě rychlost loďky a proudu řeky"

    s0 = randint(100, 200)
    t0, t1 = sorted([randint(10, 30) for i in range(2)])

    print(task_text.format(s0=s0, t0=t0, t1=t1))
    input()

    ## SOLUTION

    # nejdrive urcime rychlost lodky vzhledem k vode; v0 = po proudu, v1 = proti
    v0 = round(s0 / t0, 2)
    v1 = round(s0 / t1, 2)

    # zbytek vyresime pres soustavu rovnic:
    #   vLodka + vProud = v0
    #   vLodka - vProud = v1
    # takze, v pripade dosazeni `vProud` z druhe rovnice do prvni
    #   vLodka + (vLodka - v1) = v0
    #   2 * vLodka = v0 + v1
    #   vLodka = (v0 + v1) / 2
    # a pak staci dosadit tento vysledek do jakekoliv z rovnic
    vLodka = (v0 + v1) / 2
    vProud = v0 - vLodka

    vLodka = round(vLodka, 2)
    vProud = round(vProud, 2)

    print(f"rychlost lodky:  {vLodka}ms-1")
    print(f"rychlost proudu: {vProud}ms-1")



# choose a random task and execute it
task = choice([t for t in locals().keys() if t.startswith('task')])
locals()[task]()
