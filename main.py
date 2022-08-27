%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

# Mock data
x = np.linspace(-1,3,1000)
def f(x):
    return 2*x**2

# plot
plt.plot(x,f(x))
plt.axhline(color = 'black')
plt.fill_between(x, f(x), where = [(x>0) and (x<2) for x in x])

# test for integration
x = sy.Symbol('x')
sy.integrate(f(x), (x,0,1))

def find_barycenter(fn, x, accuracy, x_left, x_right):
    x_center = (x_left + x_right) * 0.5
    left = sy.integrate(fn, (x, x_left, x_center))
    right = sy.integrate(fn, (x, x_center, x_right))
    old_left = x_left
    old_right = x_right
    while (np.abs(left-right) > accuracy):
        print(left, right, x_center)
        if left > right:
            old_right = x_center
            x_center = (old_right + old_left) * 0.5
        else:
            old_left = x_center
            x_center = (old_right + old_left) * 0.5
        left = sy.integrate(fn, (x, x_left, x_center))
        right = sy.integrate(fn, (x, x_center, x_right))

    return x_center
    
barycenter = find_barycenter(f(x),x,0.00001,0,3)
print(f'The barycenter is x = {barycenter}')
