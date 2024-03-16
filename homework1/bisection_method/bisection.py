import math
import numpy as np

def bisection_method(a, b, eps, f, der_f , out_file = None):

    output = ""
    iter_n = 1;
    mid = a
    while(np.abs(b - a) >= 2 * eps):

        if(iter_n>25):
            output += "Лимит итераций превышен \n"
            break

        mid = (a+b)/2
        output += f"Номер итерации: {iter_n} | x = {mid} |  f(x) = {f(mid)} | f\'(x) = {der_f(mid)} \n"
        iter_n += 1

        if(der_f(mid) == 0.0):
            break

        if(der_f(mid) * f(a) < 0):
            b = mid
        else:
            a = mid
    
    if(out_file != None):
        output += f"Ответ найден | Минимум функции {f(mid)} при x = {mid} \n"
        with open(out_file, "w") as file:
            file.write(output)
    else:
        print(output)



if __name__ == "__main__":
    f = lambda x: np.log(1 + x**2) - np.sin(x)
    derivative_f = lambda x: (2*x)/(x**2 + 1) - np.cos(x)
    bisection_method(0, np.pi/4, 10**-10, f,derivative_f, "bisection_output.log")


