import math
import sympy as sp

x0 = math.pi / 4 
x1 = math.pi / 3 
h = x1 - x0 
tolerancia = 0.0005  
# Define variable
x = sp.Symbol('x')

# Definir la función
def f(x):
    return sp.cos(x)

def taylor_expansion(f, x0, h, tolerancia):
    series = f.subs(x, x0) #f(pi/4)
    ef = float('inf')  # error con valor garnde
    i = 1
    print('f(x) = cos(x)')
    print('Xo= ',x0,' =  pi/4')
    print('cos(Xo)= ',series)
    print('X1= ',x1,' =  pi/3')
    print('cos(X1)= ',f.subs(x,x1))
    print('H: ', h)
    print('-----------------------------------------------------')
    while ef > tolerancia:
        deriv_i = f.diff(x, i)
        deriv_i_val = deriv_i.subs(x, x0)
        term = (deriv_i_val / math.factorial(i) * h**i)
        series += term #actualiza la serie
        print(f"Iteración {i}= {series}")
        print(f"Derivada {i} = {deriv_i}, valor = {deriv_i_val}")
        ef = abs(term)
        print(f"Error estimado en iteración {i}: {ef}")
        print('-----------------------------------------------------')
        i += 1
    return series
expansion = taylor_expansion(f(x), x0, h, tolerancia)
print(f"\nAproximación de Taylor en x = {x1} es: {expansion}")