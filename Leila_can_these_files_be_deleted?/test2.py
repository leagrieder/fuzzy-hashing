import random
import math

# Define the range of elements
element_range = range(1, 96501)

# Define the probability function
def calculate_probability(i, p):
    return (1 - p) ** (i - 1) * p

# Generate elements with probabilities
#elements = [(i, calculate_probability(i, 0.0329)) for i in element_range]
elements = [('A', 0.2), ('B', 0.3), ('C', 0.1), ('D', 0.4), ('E', 0.5), ('F', 0.1)]


num_sets = 3

# Define the target sum probability for each set
target_sum_probability = sum(prob for _, prob in elements) / num_sets

# Define the initial solution (random assignment of elements to sets)
def initialize_solution(elements, num_sets):
    solution = [[] for _ in range(num_sets)]
    for element, _ in elements:
        set_index = random.randint(0, num_sets - 1)
        solution[set_index].append(element)
    return solution

# Define a function to calculate the sum probability of a set
def sum_probability_of_set(element_set, elements):
    return sum(prob for elem, prob in elements if elem in element_set)

# Define the objective function (variance of sum probabilities across sets)
def objective_function(solution, elements):
    set_probabilities = [sum_probability_of_set(s, elements) for s in solution]
    mean_probability = sum(set_probabilities) / len(set_probabilities)
    variance = sum((p - mean_probability) ** 2 for p in set_probabilities) / len(set_probabilities)
    return variance

# Define a function to generate neighboring solutions
def generate_neighbor(solution):
    neighbor = [set(s) for s in solution]
    # Randomly select an element to move
    element_to_move = random.choice([elem for s in neighbor for elem in s])
    # Randomly select a different set to move it to
    current_set_index = next(i for i, s in enumerate(neighbor) if element_to_move in s)
    new_set_index = random.randint(0, len(neighbor) - 1)
    while new_set_index == current_set_index:
        new_set_index = random.randint(0, len(neighbor) - 1)
    neighbor[current_set_index].remove(element_to_move)
    neighbor[new_set_index].add(element_to_move)
    return neighbor

# Simulated Annealing Algorithm
def simulated_annealing(elements, num_sets, target_sum_probability, initial_temperature, cooling_rate, max_iterations):
    current_solution = initialize_solution(elements, num_sets)
    current_cost = objective_function(current_solution, elements)
    best_solution = current_solution
    best_cost = current_cost

    temperature = initial_temperature
    iteration = 0
    while temperature > 0 and iteration < max_iterations:
        neighbor_solution = generate_neighbor(current_solution)
        neighbor_cost = objective_function(neighbor_solution, elements)

        if neighbor_cost < current_cost or random.random() < math.exp(-(neighbor_cost - current_cost) / temperature):
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        if neighbor_cost < best_cost:
            best_solution = neighbor_solution
            best_cost = neighbor_cost

        temperature *= cooling_rate
        iteration += 1

    return best_solution

# Parameters for simulated annealing
initial_temperature = 1000
cooling_rate = 0.95
max_iterations = 1000

# Run simulated annealing
best_solution = simulated_annealing(elements, num_sets, target_sum_probability, initial_temperature, cooling_rate, max_iterations)

# Output the best solution
print("Best Solution:")
for i, s in enumerate(best_solution):
    sum_prob = sum(prob for _, prob in elements if _ in s)
    print(f"Set {i+1}: {s}, Sum Probability: {sum_prob}")
