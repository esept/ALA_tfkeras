import sympy

J,w = sympy.symbols('J,w')
J = w**2
print(J)

dJ_dw = sympy.diff(J,w)
print(dJ_dw)