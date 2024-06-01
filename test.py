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

covAC = delta_indep*(1/2 - p)/n
print(covAC)

variance_p = 0.0000252
variance_delta_diff = 0.0000458
variance_delta_same = 0.0001058

component0= (p - delta_same/2)/(p + delta_same/2)
print(component0)

component1 = ((-4*delta_same)/((2*p + delta_same)**3))*variance_p
print(component1)

component3 = ((8*p)/((2*p + delta_same)**3))*variance_delta_same
print(component3)

component4 = 2*(2*(2*p - delta_same)/((2*p + delta_same)**3))*covAC
print(component4)

print(component0 + 1/2*(2*component1 + component3 + 2*component4))
