from math import *
from integration import *


def var_left_rectangle(a, b, n, E):
    h = (b - a) / n
    r = 1
    In = 0
    I2n = 0
    while r > E:
        s2 = 0
        x = a
        while x <= b - h:
            s2 += f(x)
            x += h
        I2n = h * s2
        r = abs(I2n - In)
        In = I2n
        h = h/2
    result = I2n
    return result


def var_second_left_rectangle(a, b, n, E):
    hv = (b - a) / n
    hs = 0
    hd = hv
    I2 = 0
    s1 = 0
    x0 = a
    x = x0

    while x <= b - hv:
        s1 += f(x)
        x += hd

    I1 = s1 * hd
    r = abs(I2-I1)

    while r > E:

        s2 = 0
        x = x0 + hs
        hd = hv
        hv /= 2

        while x <= b - hv:
            s2 += f(x)
            x += hd

        I2 = s2 * hd
        r = abs(I2 - I1)
        I1 = I2
        hs = hd / 2

    result = I2
    return result
