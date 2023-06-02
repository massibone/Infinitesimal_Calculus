'''
Brent’s method is an improvement on the bisection method and is available in the optimize module
as brentq. It uses a combination of bisection and interpolation to quickly find the root of an equation:
'''
  
optimize.brentq(f, 1.0, 3.0)  # 1.9999999999998792
