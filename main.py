%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

# Mock data
x = np.linspace(-1,3,1000)
def f(x):
    return 2*x**2+1

# plot
plt.plot(x,f(x))
plt.axhline(color = 'black')
plt.fill_between(x, f(x), where = [(x > -1) and (x < 3) for x in x])

# test for integration
x = sy.Symbol('x')
area = sy.integrate(f(x), (x, -1, 3))
print(f'area = {area}')

# define a function to approach barycenter
def find_barycenter(fn, x, accuracy, x_left, x_right):
    x_center = (x_left + x_right) * 0.5
    left = sy.integrate(fn, (x, x_left, x_center))
    right = sy.integrate(fn, (x, x_center, x_right))
    old_left = x_left
    old_right = x_right
    while (np.abs(left-right) > accuracy):
        print(f'test for x={x_center}, the difference is {np.abs(left-right)}')
        if left > right:
            old_right = x_center
            x_center = (old_right + old_left) * 0.5
        else:
            old_left = x_center
            x_center = (old_right + old_left) * 0.5
        left = sy.integrate(fn, (x, x_left, x_center))
        right = sy.integrate(fn, (x, x_center, x_right))

    return x_center
    
# find_barycenter(fn, x, accuracy, x_left, x_right)

# fn: The spectrum function
# x: sy.Symbol('x')
# accuracy: (number) stop calculation when the left and right area difference is smaller than this value.
# x_left: (number) The lower limit of x
# r_right: (number) The upper limit of x

# return a barycenter value (number)

    
# find barycenter for f(x) with x = 0 ~ 3
barycenter = find_barycenter(f(x), x, 0.00001, -1, 3)
print(f'The barycenter is x = {barycenter}')
