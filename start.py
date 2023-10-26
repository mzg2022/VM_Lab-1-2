from tkinter import *
from tkinter import messagebox
from math import *
from multipleIntegration import *
from variablestep_algorithm import *
from constantstep_algorithm import *
from integration import *


def calculate():
    result = ' '
    match task_type_option.get():
        case 1:
            a_raw = a_input.get()
            b_raw = b_input.get()
            n_raw = n_input.get()
            formula_raw = formula_input.get()

            a = float(eval(a_raw))
            b = float(eval(b_raw))
            n = int(eval(n_raw))
            tkGetFormula(formula_raw)

            match methods_type_option.get():
                case 1:

                    match algorithm_type_option.get():
                        case 1:
                            result = f'Результат: {left_rectangle(a, b, n)}'
                        case 2:
                            E_raw = E_input.get()
                            E = float(E_raw)
                            result = f'Результат: {var_left_rectangle(a, b, n, E)}'
                        case 3:
                            E_raw = E_input.get()
                            E = float(E_raw)
                            result = f'Результат: {var_second_left_rectangle(a, b, n, E)}'
                case 2:

                    match algorithm_type_option.get():
                        case 1:
                            result = f'Результат: {right_rectangle(a, b, n)}'
                case 3:

                    match algorithm_type_option.get():
                        case 1:
                            result = f'Результат: {trapezoid(a, b, n)}'
                case 4:

                    match algorithm_type_option.get():
                        case 1:
                            result = f'Результат: {parabola(a, b, n)}'

        case 2:
            a_raw = a_input.get()
            b_raw = b_input.get()
            n_raw = n_input.get()
            c_raw = c_input.get()
            d_raw = d_input.get()
            ny_raw = ny_input.get()
            formula_raw = formula_input.get()

            a = float(eval(a_raw))
            b = float(eval(b_raw))
            n = int(eval(n_raw))
            c = float(eval(c_raw))
            d = float(eval(d_raw))
            ny = int(eval(ny_raw))
            tkGetMultipleFormula(formula_raw)

            result = f'Результат: {re_integration(a, b, c, d, n, ny)}'

    return result


def show_result():
    result = calculate()
    reslbl.configure(text=result)
    reslbl.grid(column=1, row=5)


def var_algorithm_frame_render():
    algorithm_type_option.set(0)
    for widget in algorithm_frame.winfo_children():
        widget.destroy()

    algorithmlbl = Label(algorithm_frame, text="Алгоритм:", padx=5, pady=5)
    double_algorithm_btn = Radiobutton(algorithm_frame, text="Двойной пересчет", variable=algorithm_type_option, value=2, command=input_frame_render)
    second_double_algorithm_btn = Radiobutton(algorithm_frame, text="Двойной пересчет с отступами", variable=algorithm_type_option, value=3, command=input_frame_render)
    algorithmlbl.grid(column=0, row=0)
    double_algorithm_btn.grid(column=0, row=1)
    second_double_algorithm_btn.grid(column=0, row=2)


def algorithm_frame_render():
    for widget in algorithm_frame.winfo_children():
        widget.destroy()
    match methods_type_option.get():
        case 1:
            algorithmlbl = Label(algorithm_frame, text="Алгоритм:", padx=5, pady=5)
            constantstep_btn = Radiobutton(algorithm_frame, text="Постоянный шаг", variable=algorithm_type_option, value=1, command= input_frame_render)
            variablestep_btn = Radiobutton(algorithm_frame, text="Переменный шаг", variable=algorithm_type_option, value=2, command= var_algorithm_frame_render)
            algorithmlbl.grid(column=0, row=0)
            constantstep_btn.grid(column=0, row=1)
            variablestep_btn.grid(column=0, row=2)
        case 2:
            algorithmlbl = Label(algorithm_frame, text="Алгоритм:", padx=5, pady=5)
            constantstep_btn = Radiobutton(algorithm_frame, text="Постоянный шаг", variable=algorithm_type_option, value=1, command=input_frame_render)
            algorithmlbl.grid(column=0, row=0)
            constantstep_btn.grid(column=0, row=1)
        case 3:
            algorithmlbl = Label(algorithm_frame, text="Алгоритм:", padx=5, pady=5)
            constantstep_btn = Radiobutton(algorithm_frame, text="Постоянный шаг", variable=algorithm_type_option, value=1, command= input_frame_render)
            algorithmlbl.grid(column=0, row=0)
            constantstep_btn.grid(column=0, row=1)
        case 4:
            algorithmlbl = Label(algorithm_frame, text="Алгоритм:", padx=5, pady=5)
            constantstep_btn = Radiobutton(algorithm_frame, text="Постоянный шаг", variable=algorithm_type_option, value=1, command= input_frame_render)
            algorithmlbl.grid(column=0, row=0)
            constantstep_btn.grid(column=0, row=1)


def methods_frame_render():
    methods_frame.grid_forget()
    methods_frame.grid(column=1, row=1)
    methodslbl = Label(methods_frame, text="Метод:", padx=5, pady=5)
    left_rectangle_btn = Radiobutton(methods_frame, text="Левых прямоугольников", variable=methods_type_option, value=1, command=algorithm_frame_render)
    right_rectangle_btn = Radiobutton(methods_frame, text="Правых прямоугольников", variable=methods_type_option, value=2, command=algorithm_frame_render)
    trapezoid_btn = Radiobutton(methods_frame, text="Трапеций", variable=methods_type_option, value=3, command=algorithm_frame_render)
    parabola_btn = Radiobutton(methods_frame, text="Парабол", variable=methods_type_option, value=4, command=algorithm_frame_render)
    methodslbl.grid(column=0, row=0)
    left_rectangle_btn.grid(column=0, row=1)
    right_rectangle_btn.grid(column=0, row=2)
    trapezoid_btn.grid(column=0, row=3)
    parabola_btn.grid(column=0, row=4)


def input_frame_render():
    for widget in input_frame.winfo_children():
        widget.grid_forget()

    match task_type_option.get():
        case 1:
            match algorithm_type_option.get():
                case 1:
                    blanklbl = Label(input_frame, text=" ", padx=5, pady=5)
                    albl = Label(input_frame, text="Введите a: ", padx=5, pady=5)
                    blbl = Label(input_frame, text="Введите b: ", padx=5, pady=5)
                    nlbl = Label(input_frame, text="Введите n: ", padx=5, pady=5)
                    formulalbl = Label(input_frame, text="Введите выражение: ", padx=5, pady=5)
                    blanklbl.grid(column=0, row=0)
                    albl.grid(column=0, row=1)
                    blbl.grid(column=0, row=2)
                    nlbl.grid(column=0, row=3)
                    formulalbl.grid(column=0, row=4)
                    a_input.grid(column=1, row=1)
                    b_input.grid(column=1, row=2)
                    n_input.grid(column=1, row=3)
                    formula_input.grid(column=1, row=4)

                case 2:
                    blanklbl = Label(input_frame, text=" ", padx=5, pady=5)
                    albl = Label(input_frame, text="Введите a: ", padx=5, pady=5)
                    blbl = Label(input_frame, text="Введите b: ", padx=5, pady=5)
                    nlbl = Label(input_frame, text="Введите n: ", padx=5, pady=5)
                    Elbl = Label(input_frame, text="Введите E: ", padx=5, pady=5)
                    formulalbl = Label(input_frame, text="Введите выражение: ", padx=5, pady=5)
                    blanklbl.grid(column=0, row=0)
                    albl.grid(column=0, row=1)
                    blbl.grid(column=0, row=2)
                    nlbl.grid(column=0, row=3)
                    Elbl.grid(column=0, row=4)
                    formulalbl.grid(column=0, row=5)
                    a_input.grid(column=1, row=1)
                    b_input.grid(column=1, row=2)
                    n_input.grid(column=1, row=3)
                    E_input.grid(column=1, row=4)
                    formula_input.grid(column=1, row=5)
                case 3:
                    blanklbl = Label(input_frame, text=" ", padx=5, pady=5)
                    albl = Label(input_frame, text="Введите a: ", padx=5, pady=5)
                    blbl = Label(input_frame, text="Введите b: ", padx=5, pady=5)
                    nlbl = Label(input_frame, text="Введите n: ", padx=5, pady=5)
                    Elbl = Label(input_frame, text="Введите E: ", padx=5, pady=5)
                    formulalbl = Label(input_frame, text="Введите выражение: ", padx=5, pady=5)
                    blanklbl.grid(column=0, row=0)
                    albl.grid(column=0, row=1)
                    blbl.grid(column=0, row=2)
                    nlbl.grid(column=0, row=3)
                    Elbl.grid(column=0, row=4)
                    formulalbl.grid(column=0, row=5)
                    a_input.grid(column=1, row=1)
                    b_input.grid(column=1, row=2)
                    n_input.grid(column=1, row=3)
                    E_input.grid(column=1, row=4)
                    formula_input.grid(column=1, row=5)

        case 2:
            blanklbl = Label(input_frame, text=" ", padx=5, pady=5)
            albl = Label(input_frame, text="Введите a: ", padx=5, pady=5)
            blbl = Label(input_frame, text="Введите b: ", padx=5, pady=5)
            clbl = Label(input_frame, text="Введите c: ", padx=5, pady=5)
            dlbl = Label(input_frame, text="Введите d: ", padx=5, pady=5)
            nlbl = Label(input_frame, text="Введите nX: ", padx=5, pady=5)
            nylbl = Label(input_frame, text="Введите nY: ", padx=5, pady=5)
            formulalbl = Label(input_frame, text="Введите выражение: ", padx=5, pady=5)
            blanklbl.grid(column=0, row=0)
            albl.grid(column=0, row=1)
            blbl.grid(column=0, row=2)
            nlbl.grid(column=0, row=3)
            formulalbl.grid(column=0, row=4)
            clbl.grid(column=2, row=1)
            dlbl.grid(column=2, row=2)
            nylbl.grid(column=2, row=3)
            formulalbl.grid(column=0, row=4)
            a_input.grid(column=1, row=1)
            b_input.grid(column=1, row=2)
            n_input.grid(column=1, row=3)
            c_input.grid(column=3, row=1)
            d_input.grid(column=3, row=2)
            ny_input.grid(column=3, row=3)
            formula_input.grid(column=1, row=4)


def render_control():
    match task_type_option.get():
        case 1:
            for widget in input_frame.winfo_children():
                widget.grid_forget()
            methods_frame.grid_forget()
            algorithm_frame.grid_forget()
            input_frame.grid(column=0, row=1)
            methods_frame.grid(column=1, row=1)
            algorithm_frame.grid(column=2, row=1)
            methods_frame_render()
        case 2:
            for widget in input_frame.winfo_children():
                widget.grid_forget()
            methods_frame.grid_forget()
            algorithm_frame.grid_forget()
            input_frame.grid(column=0, row=1)
            input_frame_render()


window = Tk()
window.title("Интегралы")
window.geometry('820x300')

task_type_option = IntVar()
methods_type_option = IntVar()
algorithm_type_option = IntVar()

Radiobutton(window, text="Численное интегрирование", variable=task_type_option, value=1, command=render_control).grid(column=0, row=0)
Radiobutton(window, text="Кратные интегралы ", variable=task_type_option, value=2, command=render_control).grid(column=1, row=0)
Button(window, text="Вычислить", command=show_result, padx=5, pady=5).grid(row=5, column=0)

input_frame = Frame(window)
methods_frame = Frame(window)
algorithm_frame = Frame(window)

formula_input = Entry(input_frame, width=20)
a_input = Entry(input_frame, width=5)
b_input = Entry(input_frame, width=5)
n_input = Entry(input_frame, width=5)
E_input = Entry(input_frame, width=5)
c_input = Entry(input_frame, width=5)
d_input = Entry(input_frame, width=5)
ny_input = Entry(input_frame, width=5)

reslbl = Label(window, text=' ', padx=5, pady=5)

window.mainloop()
