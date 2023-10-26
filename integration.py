from math import *


# Получение выражения для пользовательского интерфейса
def tkGetFormula(input_formula):
    global formula
    formula = input_formula


# Воспроизведение выражения
def f(x):
    return eval(formula)
