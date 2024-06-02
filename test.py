import math

p = 0.03514
formula = 2 * p * (1 - p)


n = 90240
variance_delta = 4*p*(1-p)*(1-2*p*(1-p))/n 

stdev_delta = math.sqrt(variance_delta)

delta_indep = 0.06781
delta_same = 0.04549
delta_diff = 0.05988
p1 = 1 - p - delta_diff/2

p2 = delta_diff/2

p3 = p - delta_diff/2

covAC_indep = delta_indep*(1/2 - p)/n

variance_p = 0.0000252
variance_delta_diff = 0.0000458
variance_delta_same = 0.0001058

covAB_same = 0.000022
covAB_diff = 0.000006
covAC_same = 0.000036
covAC_diff = 0.000026
covBC_same = 0.000036
covBC_diff = 0.000027

component0= (p - delta_diff/2)/(p + delta_diff/2)
print(component0)

component1 = ((-4*delta_diff)/((2*p + delta_diff)**3))*variance_p
print(component1)

component3 = ((8*p)/((2*p + delta_diff)**3))*variance_delta_diff
print(component3)

component4 = 2*(((-4)*delta_diff)/((2*p + delta_diff)**3))*covAB_diff
print(component4)

component5 = 2*(2*(2*p - delta_diff)/((2*p + delta_diff)**3))*covAC_diff
print(component5)

component6 = 2*(2*(2*p - delta_diff)/((2*p + delta_diff)**3))*covBC_diff
print(component6)

print(component0 + 1/2*(2*component1 + component3 + component4 + component5 + component6))
