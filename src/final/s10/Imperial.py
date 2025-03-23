# Imperial.py - Fractional Knapsack Problem

def fractional_knapsack(max_weight, items):
    # Calculate value/weight ratio for each item
    for item in items:
        item.append(item[0] / item[1])  # Append value/weight ratio
    
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0  # Maximum value of the knapsack
    remaining_weight = max_weight  # Remaining weight capacity of the knapsack
    
    for value, weight, ratio in items:
        if remaining_weight >= weight:
            # Take the whole item
            total_value += value
            remaining_weight -= weight
        else:
            # Take a fraction of the item
            fraction = remaining_weight / weight
            total_value += value * fraction
            remaining_weight = 0
            break  # Knapsack is full
    
    return total_value

# User input
n = int(input("Enter the number of items: "))
max_weight = float(input("Enter the maximum weight of the knapsack: "))

items = []
for i in range(n):
    value = float(input(f"Enter the value of item {i+1}: "))
    weight = float(input(f"Enter the weight of item {i+1}: "))
    items.append([value, weight])

# Print user input in tabular form
print("\nKnapsack Problem Table")
print("{:<10} {:<10} {:<10}".format("Item", "Value", "Weight"))
for i, (value, weight) in enumerate(items, start=1):
    print(f"{i:<10} {value:<10.2f} {weight:<10.2f}")

# Solve the problem
max_value = fractional_knapsack(max_weight, items)

# Output the result
print(f"\nThe maximum value that can be achieved is: {max_value:.2f}")
