from math import *


def tkGetMultipleFormula(input_multiple_formula):
    global multiple_formula
    multiple_formula = input_multiple_formula


def multiple_f(x, y):
    return eval(multiple_formula)


def re_integration(a, b, c, d, nx, ny):
    hx = (b - a)/nx
    hy = (d - c)/ny
    sx = 0
    x = a
    while x <= b - hx:
        sy = 0
        x += hx
        y = c
        while y <= d - hy:
            sy += abs(multiple_f(x, y))
            y += hy
        Iy = hy * sy
        sx += Iy
    Ix = hx * sx
    result = Ix
    return result
