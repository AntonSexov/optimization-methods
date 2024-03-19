import math
import numpy as np

def bisection_method(a, b, eps, f, out_file = None):

    output = ""
    iter_n = 1;
    mid = a
    while(np.abs(b - a) >= 2 * eps):

        if(iter_n>25):
            output += "Лимит итераций превышен \n"
            break

        x1 = (a+b - eps)/2
        x2 = (a+b + eps)/2
        
        output += f"n: {iter_n} | a = {a :.3f}| b = {b :.3f} |  f(x) = {f((b+a)/2) :.3f} \n"
        iter_n += 1

        if(np.abs(b - a)/2 < eps):
            break

        if(f(x1) <= f(x2)):
            b = x2
        else:
            a = x1
    
    if(out_file != None):
        output += f"Ответ найден | Экстремум функции {f((b+a)/2) :.10f} при x = {(b+a)/2  :.10f} \n"
        with open(out_file, "w") as file:
            file.write(output)
    else:
        print(output)



if __name__ == "__main__":

    f = lambda x: np.log(1 + x**2) - np.sin(x)
    
    bisection_method(0, np.pi/4, 10**-10, f, "bisection_output.log")


