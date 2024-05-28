import sympy as sp

# Define the symbols
p, delta, sigma_p_obs, sigma_delta_obs = sp.symbols('p delta sigma_p_obs sigma_delta_obs')
Cov_AB, Cov_AC, Cov_BC = sp.symbols('Cov_AB Cov_AC Cov_BC')

# Define the formula
term1 = (p - delta / 2) / (p + delta / 2)
term2 = 1 / 2 * (
    (-4 * delta / (2 * p + delta)**3) * sigma_p_obs**2 +
    (-4 * delta / (2 * p + delta)**3) * sigma_p_obs**2 +
    (8 * p / (2 * p + delta)**3) * sigma_delta_obs**2 +
    2 * (-4 * delta / (2 * p + delta)**3) * Cov_AB +
    2 * (2 * (2 * p - delta) / (2 * p + delta)**3) * Cov_AC +
    2 * (2 * (2 * p - delta) / (2 * p + delta)**3) * Cov_BC
)

formula = term1 + term2

# Substitute the values (initially all set to 0)
values = {
    p: 0.0329,
    delta: 0.064,
    sigma_p_obs: 0.00469,
    sigma_delta_obs: 0,
    Cov_AB: 0,
    Cov_AC: 0,
    Cov_BC: 0
}

# Evaluate the formula with the given values
result = formula.evalf(subs=values)

print("Result with initial values:", result)

# To use this script, replace the values in the dictionary with the actual values you have.
