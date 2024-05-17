#!/usr/bin/env python

from random import uniform, randint, choice
from math import sqrt


def task1():
    t0, t1, t2 = [round(uniform(1.0, 5.0), 1) for i in range(3)]
    v0, v2 = [randint(50, 130) for i in range(2)]

    print(f"Na dovolenou jedete autem po dálnici {t0} hodin rychlostí {v0} km.h-1. Potom na {t1} hodin zastavíte. Pokračujete {t2} hodin stálou rychlostí {v2} km.h-1 až do cíle. Určete průměrnou rychlost cestování (v km/h).")
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
    s0, v0 = [randint(50, 130) for i in range(2)]
    t0 = randint(10, 120)

    print(f"Dálniční úsek má délku {s0} km. Největší povolená rychlost je {v0} km.hod-1. Řidič tento úsek projel za {t0} minut. Překročil největší povolenou rychlost na dálnici?")
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
    g = 9.8
    vA, tToB, tToGround = sorted([randint(1, 5) for i in range(3)])
    vB = round(vA + g * tToB, 2)

    print(f"Volně padající těleso má v bodě A rychlost {vA} ms-1, v níže položeném bodě B rychlost {vB} ms-1. Zjistěte, za jaký čas proletí vzdálenost A->B. Jaká je vzdálenost bodů A a B? Jakou rychlostí těleso dopadne, pokud jeho pohyb z bodu B na zem trvá ještě {tToGround} s. Předpokládej, že g = 9.8")
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
    v0, v1 = sorted([round(uniform(0.1, 1), 1) for i in range(2)], reverse=True)
    v0 = v0 + 0.1 if v1 == v0 else v0
    sAtoB = randint(50, 150)

    print(f"Plavec, jehož rychlost vzhledem na vodu je {v0} ms-1 plave v řece, v níž voda teče rychlostí {v1} ms-1. Určete čas, za který dopluje z místa A do B, vzdáleného {sAtoB} m, pokud plave:")
    print(f"\na) po proudu")
    print(f"\nb) proti proudu")
    print(f"\nc) kolmo na proud (vysledná rychlost je kolmá rychlosti proudu)")
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
    s0 = randint(100, 200)
    t0, t1 = sorted([randint(10, 30) for i in range(2)])

    print(f"Motorová loď plovoucí po řece projela vzdálenost {s0} m při plavbě po proudu za {t0}s, při plavbě proti proudu za {t1}s. Určitě rychlost loďky a proudu řeky")
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


def task6():
    s = randint(40, 80)
    vA, vM = [randint(50, 100) for i in range(2)]

    print(f"Ze dvou míst vzdálených od sebe {s} km vyjely současně proti sobě auto a motocykl. Auto se pohybovalo rychlostí {vA} km/h a motocykl rychlostí {vM} km/h. Kdy a kde se potkají?")
    input()

    ## SOLUTION

    # relativni rychlost
    v = vA + vM

    # dopocitame cas a vzdalenost
    t = round(s / v, 2)
    s = round(t * vA, 2)

    print(f"za {round(t * 60, 2)} minut ({t} hodin), {s} km od startu auta")


def task7():
    s = randint(100, 500)
    vM, vP = sorted([randint(2, 10) for i in range(2)], reverse=True)
    vM = vM + 1 if vM == vP else vM

    print(f"Ze dvou míst M a P vzdálených od sebe {s} m se současně pohybují dvě tělesa rovnoměrným přímočarým pohybem stejným směrem. Těleso pohybující se z místa M má rychlost {vM} m/s a z místa P se těleso pohybuje rychlostí {vP} m/s. Za jaký čas dosáhne první těleso druhé? Jaké vzdálenosti urazí obě tělesa za tuto dobu?")
    input()

    ## SOLUTION

    # relativni rychlost
    v = vM - vP

    # cas a vzdalenost
    t = round(s / v, 2)
    sM = vM * t
    sP = vP * t

    print(f"prvni teleso dosahne druhe za {t} sekund. teleso M urazi {sM} m, teleso P {sP} m.")


def task8():
    v0 = randint(50, 100)
    t = randint(5, 10)
    a = round(uniform(1, 4), 2)

    print(f"Autobus pohybující se rychlostí {v0} km/h zvyšuje svoji rychlost během {t} s se stálým zrychlením {a} m/s2. Jakou dráhu urazí za tuto dobu?")
    input()

    ## SOLUTION

    v0 *= 1000 / 3600

    # vysvetleno v task3()
    # $\Delta x = \frac{v_0 + at + v_0}{2} \times t$.
    deltaX = round((v0 + a * t + v0)/2 * t, 2)

    print(f"{deltaX} m")


def task9():
    ts = randint(1, 10)

    print(f"Jak velké je zrychlení pohybu, při kterém těleso pohybující se ze stavu klidu urazí během {ts}. sekundy vzdálenost {ts} m")
    input()

    ## SOLUTION

    # vysvetleno v task3()
    # $\Delta x = \frac{v_0 + at + v_0}{2} \times t$.
    a = (2 * ts - 2 * 0 * ts) / ts ** 2
    print(f"{a} m/s")


def task10():
    a = round(uniform(5, 10), 2)
    s = randint(30, 100)

    print(f"Řidič automobilu začne brzdit, přičemž velikost brždění je {a} m.s-2, a než zastaví, urazí dráhu {s} m. Za jakou dobu zastavil a jaká byla jeho počáteční rychlost?")
    input()

    ## SOLUTION

    # pokud misto zrychleni zpomalujem, tak muzene zrychleni nechat kladne,
    # pokud prohodime "zpomaleni" na "zrychleni z klidu" :D
    #
    # vysvetleno v task3()
    # $\Delta x = \frac{v_0 + at + v_0}{2} \times t$.
    t = round(sqrt((2 * s) / 6.5), 2)
    v = round((2 * s) /  t, 2)

    print(f"pocatecni rychlost byla {v} m/s, a zastavil za {t} sekund")


# choose a random task and execute it
if __name__ == "__main__":
    task = choice([t for t in locals().keys() if t.startswith('task')])
    locals()[task]()
