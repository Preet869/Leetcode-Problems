# Space Complexity

# Space complexity measures how much memory (or space) an algorithm uses relative to the size of its input. 
# It’s like asking, “How much room does this algorithm need to do its job?” 
# It’s usually expressed using Big O notation, just like time complexity, 
# to describe how memory usage grows as the input size increases.

#1. O(1) Space Complexity (Constant Space)
#Definition: The algorithm uses a fixed amount of memory, no matter how large the input is. It’s like using the same small notebook for any number of problems.
#Example Problem: Find the maximum number in a list.
def find_max(numbers):
    max_value = numbers[0]  # Single variable
    for num in numbers:
        if num > max_value:
            max_value = num  # Update the variable
    return max_value

# Test
numbers = [3, 1, 4, 1, 5, 9, 2]
print(find_max(numbers))  # Output: 9

# Space Complexity Explanation:
    # Variables: Only uses max_value (one integer) and num (one integer during the loop).
    # No extra data structures: The algorithm works directly on the input list without creating new arrays or structures.
    # Memory usage: Always the same (a few variables), whether the list has 10 or 10,000 elements.
    # Conclusion: Space complexity is O(1) because memory doesn’t grow with input size n.

# 2. O(n) Space Complexity (Linear Space)
 # Definition: Memory usage grows linearly with the input size. If the input doubles, the memory needed roughly doubles.
 # Example Problem: Create a new list containing the squares of the input numbers.
def square_numbers(numbers):
    squared = []  # New list to store results
    for num in numbers:
        squared.append(num * num)  # Add square to new list
    return squared

# Test
numbers = [1, 2, 3, 4]
print(square_numbers(numbers))  # Output: [1, 4, 9, 16]

# Space Complexity Explanation:
    # Variables: The loop variable num uses constant space (O(1)).
    # Data structure: The squared list grows with the input size. If the input list has n elements, squared will also store n elements.
    # Memory usage: The space needed for squared is proportional to n.
    # Conclusion: Space complexity is O(n) because the memory scales linearly with the input size.

# 3. O(n²) Space Complexity (Quadratic Space)
    # Definition: Memory usage grows quadratically with the input size. This often happens when you create a 2D data structure (like a matrix) based on the input size.
    # Example Problem: Create a multiplication table as a 2D list for numbers 1 to n.

def multiplication_table(n):
    table = [[0 for _ in range(n)] for _ in range(n)]  # n x n 2D list
    for i in range(n):
        for j in range(n):
            table[i][j] = (i + 1) * (j + 1)  # Fill with products
    return table
# Test
n = 3
result = multiplication_table(n)
for row in result:
    print(row)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Space Complexity Explanation:
    # Variables: Loop variables i and j use constant space (O(1)).
    # Data structure: The table is a 2D list of size n × n, which requires n² elements.
    # Memory usage: If n = 3, the table has 3 × 3 = 9 elements. For n = 10, it’s 100 elements.
    # Conclusion: Space complexity is O(n²) because memory grows quadratically with the input size.