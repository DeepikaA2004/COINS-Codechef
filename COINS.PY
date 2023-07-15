# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of weeks and cost per week
    X, Y = map(int, input().split())
    
    # Calculate the total amount of money
    total_cost = X * Y
    
    # Output the total amount of money
    print(total_cost)
