# sympy library essentially has programs for derivation and other more complex mathematical problem solving


from sympy import
x = symbol('x')

# our function

f = x**2+3
f_prime = f.diff(x)

print(“The derivative of”, f ,“is”, f_prime) 

