# Imperial_Longquiz.py

## Fibonacci Sequence using Iterative Approach
def fibonacci(n):
    fib = [0, 1]  # Starting values for the Fibonacci sequence
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])  # Add the sum of the previous two terms
        
    return fib

## Knapsack Problem using Dynamic Programming
def knapsack(capacity, weights, values, n):
    # Create a 2D array for dynamic programming
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Print the DP table with aligned headers and data
    print("\nKnapsack Problem (Dynamic Programming) DP Table:")
    # Print the header row for capacity values
    print(f"{'Item':<5}{'Capacity':<10}", end="")
    for w in range(capacity + 1):
        print(f"{w:<5}", end="")
    print()
    
    # Print each row of the DP table with the item number and the corresponding capacity values
    for i in range(n + 1):
        print(f"{i:<15}", end="")
        for w in range(capacity + 1):
            print(f"{dp[i][w]:<5}", end="")
        print()

    # The value in dp[n][capacity] will be the maximum value
    return dp[n][capacity]


## Activity Selection Problem using Greedy Algorithm
def activity_selection(activities):
    # Sort the activities by their finish time
    activities.sort(key=lambda x: x[1])
    
    # Select the first activity
    selected_activities = [activities[0]]
    
    # Iterate through the sorted activities and select the ones that don't overlap
    for i in range(1, len(activities)):
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])
    
    return selected_activities

## Greedy Knapsack Problem
def greedy_knapsack(capacity, weights, profits, n):
    # Calculate profit-to-weight ratio for each item
    ratios = [(profits[i] / weights[i], profits[i], weights[i], i + 1) for i in range(n)]
    
    # Sort items by profit-to-weight ratio in descending order
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    remaining_capacity = capacity
    selected_items = []

    print("\nGreedy Knapsack Problem (Step-by-Step Selection):")
    print(f"{'Step':<5}{'Item':<5}{'Profit':<10}{'Weight':<10}{'Ratio':<15}{'Remaining Capacity':<20}{'Total Value':<15}")
    
    # Step-by-step item selection
    for step, (ratio, profit, weight, item) in enumerate(ratios, start=1):
        if remaining_capacity >= weight:
            # Take the entire item
            selected_items.append(item)
            total_value += profit
            remaining_capacity -= weight
            print(f"{step:<5}{item:<5}{profit:<10}{weight:<10}{ratio:<15.2f}{remaining_capacity:<20}{total_value:<15}")
        else:
            # Take a fraction of the remaining item
            selected_items.append(f"{item} (fraction)")
            total_value += profit * (remaining_capacity / weight)
            remaining_capacity = 0  # No more capacity left
            print(f"{step:<5}{item:<5}{profit:<10}{weight:<10}{ratio:<15.2f}{remaining_capacity:<20}{total_value:<15}")
            break
    
    return total_value, ratios


## Function to display the results
def main():
    # Generate Fibonacci sequence up to the 15th term
    n = 15
    fib_sequence = fibonacci(n)
    print("Fibonacci Sequence up to the 15th term:", fib_sequence)
    print("""\nThe sequence starts with 0 and 1.
Then, each subsequent number is the sum of the two preceding numbers.
The output will print the Fibonacci sequence up to the 15th term.
""")

    print("------------------------------------------")

    # Item values and weights for Knapsack Problem (Dynamic Programming)
    values = [12, 10, 20, 15, 8, 25, 18, 9]
    weights = [2, 1, 3, 2, 1, 4, 2, 2]
    capacity = 12
    n = len(values)

    # Tabulate the Knapsack Problem input
    print("\nKnapsack Problem (Dynamic Programming) Input Table:")
    print(f"{'Item':<5}{'Value':<10}{'Weight':<10}")
    for i in range(n):
        print(f"{i+1:<5}{values[i]:<10}{weights[i]:<10}")

    # Solve the knapsack problem (Dynamic Programming)
    max_value = knapsack(capacity, weights, values, n)
    print(f"The maximum value that can be achieved using Dynamic Programming is: {max_value}")
    print("""
    The time complexity of this dynamic programming approach is:
    O(n * W),
    
    where n is the number of items,
    and W is the maximum weight of the knapsack (12 in this case).
    
    This is because we iterate over all items and all possible weights.
    """)

    print("------------------------------------------")

    # Activity start and finish times for Activity Selection Problem
    activities = [(1, 1), (3, 2), (0, 6), (5, 7), (8, 4), (5, 9), (8, 10), (2, 14), 
                  (12, 16), (2, 5), (5, 9), (3, 7), (4, 6), (6, 8), (10, 10), (11, 13), 
                  (9, 13), (8, 12), (0, 2), (4, 6)]
    
    # Solve the Activity Selection Problem
    selected_activities = activity_selection(activities)
    
    # Tabulate the Activity Selection Problem input
    print("\nActivity Selection Problem Sorted Table:")
    print(f"{'Activity':<10}{'Start Time':<12}{'Finish Time':<12}")
    for i, activity in enumerate(activities):
        print(f"{i+1:<10}{activity[0]:<12}{activity[1]:<12}")

    # Output the selected activities
    print("\nSelected Activities from Activity Selection Problem:")
    for activity in selected_activities:
        print(f"Start: {activity[0]}, Finish: {activity[1]}")

    print("\nThe time complexity of the greedy approach is O(n log n) due to the sorting step. After sorting, we only need to iterate through the activities once.")

    print("------------------------------------------")

    # Item profits and weights for Greedy Knapsack Problem
    profits = [10, 20, 40, 40, 60, 10, 70, 15]
    weights = [2, 3, 4, 5, 6, 7, 3, 2]
    capacity = 12
    n = len(profits)

    # Solve the greedy knapsack problem
    max_value, sorted_ratios = greedy_knapsack(capacity, weights, profits, n)

    # Tabulate the sorted Greedy Knapsack Problem
    print("\nGreedy Knapsack Problem (Sorted Items by Profit-to-Weight Ratio):")
    print(f"{'Item':<5}{'Profit':<10}{'Weight':<10}{'Profit-to-Weight Ratio':<20}")
    for i, (ratio, profit, weight, item) in enumerate(sorted_ratios):
        print(f"{i+1:<5}{profit:<10}{weight:<10}{ratio:<20.2f}")

    print(f"\nThe maximum value that can be achieved using the Greedy algorithm is: {max_value:.2f}")

    print("""
In the greedy approach,
we calculate the profit-to-weight ratio for each item
and select items in decreasing order of this ratio
until the knapsack's weight capacity is reached.
    
The time complexity of the greedy algorithm is O(n log n)
due to the sorting step.
The selection of items happens in O(n) time.
    """)

# Run the main function
if __name__ == "__main__":
    main()
