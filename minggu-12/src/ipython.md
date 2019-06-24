In [1]: from scipy import special, optimize

In [2]: f = lambda x: -special.jv(3, x)

In [3]: sol = optimize.minimize(f, 1.0)

In [4]: x = linspace(0, 10, 5000)

In [5]: x
Out[5]:
array([  0.00000000e+00,   2.00040008e-03,   4.00080016e-03, ...,
         9.99599920e+00,   9.99799960e+00,   1.00000000e+01])