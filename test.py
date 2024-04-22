# Define the parameters
p = 0.0329
i = 170
# Create a list to store the calculated values
##results = []

# Loop over the range from 1 to 7
##for i in range(38, 96500):
    # Calculate the value for each i using the given formula
value = (1 - p) ** (i - 1) * p
##results.append(value)

# Calculate the mean of the results
##sum = sum(results)

# Print the results and the mean
##print("Values:", results)
##print("Sum:", sum)
print(value*100)