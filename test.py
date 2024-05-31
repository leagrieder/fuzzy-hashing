import math

p = 0.03514
formula = 2 * p * (1 - p)
print(formula)


n = 90240
variance_delta = 4*p*(1-p)*(1-2*p*(1-p))/n 
print(variance_delta)

stdev_delta = math.sqrt(variance_delta)
print(stdev_delta)

delta_indep = 0.06781
delta_same = 0.04549
delta_diff = 0.05988
p1 = 1 - p - delta_diff/2
print(p1)

p2 = delta_diff/2
print(p2)

p3 = p - delta_diff/2
print(p3)