# Define the range of elements
element_range = range(1, 96501)

# Define the probability function
def calculate_probability(i, p):
    return (1 - p) ** (i - 1) * p

# Generate elements with probabilities
elements = [(i, calculate_probability(i, 0.0329)) for i in element_range]

num_sets = 4

# Greedy Algorithm
def greedy_algorithm(elements, num_sets):
    # Sort elements by probability in descending order
    sorted_elements = sorted(elements, key=lambda x: x[1], reverse=True)

    # Initialize empty sets
    sets = [[] for _ in range(num_sets)]

    # Assign elements greedily to sets
    for element, probability in sorted_elements:
        min_set_index = min(range(num_sets), key=lambda i: sum(prob for _, prob in sets[i]))
        sets[min_set_index].append(element)

    return sets

# Run greedy algorithm
greedy_solution = greedy_algorithm(elements, num_sets)

# Output the greedy solution
print("Greedy Solution:")
for i, s in enumerate(greedy_solution):
    print(f"Set {i+1}: {s}")
