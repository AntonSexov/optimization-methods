import math
import numpy as np

def newton_method(x, eps, f, derivative_f, second_derivative_f, out_file=None):
    output = ""
    iter_n = 1

    while True:

        if iter_n > 25:
            output += "Лимит итераций превышен \n"
            break
        
        if abs(derivative_f(x)) < eps:
            output += f"Ответ найден | Экстремум функции {f(x)} при x = {x} \n"
            break

        x_next = x - derivative_f(x) / second_derivative_f(x)
        output += f"Номер итерации: {iter_n} | x = {x} | f(x) = {f(x)} | f'(x) = {derivative_f(x)} | f''(x) = {second_derivative_f(x)} | x_next = {x_next} \n"

        x = x_next
        iter_n += 1

    if out_file is not None:
        with open(out_file, "w") as file:
            file.write(output)
    else:
        print(output)

if __name__ == "__main__":

    f = lambda x: np.log(1 + x**2) - np.sin(x)
    derivative_f = lambda x: (2*x)/(x**2 + 1) - np.cos(x)
    second_derivative_f = lambda x: np.sin(x) - (2*(x**2) - 2)/(x**4 + 2*(x**2) + 1)

    newton_method(0, 10**-10, f, derivative_f, second_derivative_f, "newton_output.log")