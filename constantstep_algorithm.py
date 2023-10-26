from math import *
from integration import *


def left_rectangle(a, b, n):
    s = 0
    h = (b - a) / n
    x = a

    while x <= b - h:
        s += f(x)
        x += h

    result = h * s
    return result


def right_rectangle(a, b, n):
    s = 0
    h = (b - a) / n
    x = a + h

    while x <= b:
        s += f(x)
        x += h

    result = h * s
    return result


def trapezoid(a, b, n):
    s = 0
    h = (b - a) / n
    y1 = f(a)
    y2 = f(b)
    x = a + h
    while x <= b - h:
        s = s + f(x)
        x += h
    result = h * ((y1 + y2) / 2 + s)
    return result


def parabola(a, b, n):
    s1 = 0
    s2 = 0
    h = (b - a) / n
    x = a
    s = f(x)
    x = b
    s += f(x)
    x = a + h
    while x <= b - h:
        s1 += f(x)
        x += 2 * h
    i1 = 4 * s1
    x = a + 2 * h
    while x <= b - 2 * h:
        s2 += f(x)
        x += 2 * h
    i2 = 2 * s2
    result = h * (i1 + i2 + s) / 3
    return result
