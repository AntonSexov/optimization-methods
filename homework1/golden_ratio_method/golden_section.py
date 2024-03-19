import math
import numpy as np

def golden_section_search(a, b, eps, f, out_file=None):
    output = ""
    iter_n = 1

    phi = (1 + math.sqrt(5)) / 2
    c = b - (b - a) / phi
    d = a + (b - a) / phi

    while (b - a) >= 2 * eps:
        if iter_n > 25:
            output += "Лимит итераций превышен \n"
            break

        if f(c) < f(d):
            b = d
            d = c
            c = b - (b - a) / phi
        else:
            a = c
            c = d
            d = a + (b - a) / phi

        output += f"n: {iter_n} | a = {a :.3f} | b = {b :.3f} |\n"
        iter_n += 1

    if out_file is not None:
        min_value = min(f(c), f(d))
        min_x = c if f(c) < f(d) else d
        output += f"Ответ найден | Экстремум функции {min_value} при x = {min_x} \n"
        with open(out_file, "w") as file:
            file.write(output)
    else:
        print(output)

if __name__ == "__main__":
    f = lambda x: np.log(1 + x**2) - np.sin(x)
    golden_section_search(0, np.pi / 4, 10 ** -10, f, "golden_section_output.log")
