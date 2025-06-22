# Learning Big O Notation 

######
# Big O Notation 
# 1. Worst Case - Always analyze the worst-case scenario.
# 2. Remove Constants - Drop constants from Big O expressions. We only care about how the algorithm scales, not exact operation counts.
# 3. Different terms for inputs - If your algorithm has multiple inputs with different sizes, use separate variables.
# 4. Drop Non Dominants - Only keep the most significant term as input grows.
##########

# O(1) Constant Time 
# The operations takes the same amount of time regardless of the input size.

# Data Structures:
     # * Hash maps give you constant time access to values. stores key-value pairs.

# 🧠 When Your Brain Should Think "Hash Map!" If a problem requires O(1) time for lookups, inserts, or updates.
# Keywords to look out for:
    # "Find in constant time"
    # "Check if exists"
    # "Count frequency"
    # "Avoid duplicates"
    # "Get index/value quickly"
    # "Map one thing to another"
    # "Return fast even with big input"

def get_first_element(arr):
    return arr[0]

my_list = ["Cat","Dog","Mouse"]
print (get_first_element(my_list))
    # No matter if there are 10 users or 10 million — this operation is always fast. It doesn’t "loop" through anything.

# For larger data instead of looping through everything use a Hash Map.
    # In Real Projects (What Companies Do):
        # * Use a database with indexes
        # * Load only what’s needed (pagination, filters)
        # * Cache frequent lookups (like Redis)
        # * Design systems around query speed, not brute force

###########################################

# 2. O(n) — Linear Time. This means the time grows linearly with the size of the input.
    # Example: Looping through all elements in a list.
def print_all_element(arr):
    for element in arr:
        print(element)
my_list = ["Cat","Dog","Mouse"]
print (print_all_element(my_list))
# Explanation: If the list size doubles, the time to print all elements roughly doubles too.

# ✅ When to use O(n):
    # You need to look at or check every item.
    # You're doing things like:
    # Finding the maximum or minimum
    # Searching through a list (without advanced structures like binary search trees)
    # Summing all the values
    # Filtering a list
    # Doing something with every element (e.g., printing, updating)
# 🧠 Mindset:
    # When you read a problem, ask:
    # ❓ Do I need to touch every element at least once?
    # If yes → that's your cue for O(n).

####################################

# 0(n^2) - Quadratic Time - Every time the number of elements increase by the power of 2.
    # Interview question ask to solve problem from Quadratic time to quicker. 
    # Nested loop become times (*). 
    # - One after another, you add.
    # - Any steps that happens one with indentation that is nested multiply.
def print_all_pairs(numbers):
    for i in numbers:                # O(n)
        for j in numbers:            # O(n)
            print(i, j)              # Total: O(n * n) → O(n²)

    #✅ Why it's O(n²):
        # The outer loop runs n times.
        # For each iteration of the outer loop, the inner loop runs n times.
        # So total operations = n * n = n²
            
# 🧠 Interview Tip:
    # If an interviewer wants you to optimize O(n²) to a faster solution (like O(n)), that usually means:
    # Try to remove the inner loop.
    # Consider using a hash map or sorting with two pointers to avoid nested iterations.

# Example: ❌ Brute Force (Quadratic Time — O(n²))
def has_pair_with_sum_brute_force(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

# Example
print(has_pair_with_sum_brute_force([2, 7, 11, 15], 9))  # True
    # ✅ Easy to understand
    # ❌ Inefficient for large inputs
    # ⏱️ Time Complexity: O(n²)

# ✅ Optimized with Hash Map (Linear Time — O(n))
def has_pair_with_sum_optimized(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example
print(has_pair_with_sum_optimized([2, 7, 11, 15], 9))  # True
# ✅ Much faster for large arrays
    # 🧠 Uses extra space (set) to remember elements
    # ⏱️ Time Complexity: O(n)
    # 🧮 Space Complexity: O(n)
####################

# O(n!) —> Factorial Time. Adding a loop for every element. You are doing something bad 🚨
from itertools import permutations

def generate_permutations(nums):
    return list(permutations(nums))

nums = [1, 2, 3]
print(generate_permutations(nums))

#❗ Why is O(n!) bad?
# It grows extremely fast.
# Even for small inputs like n = 10, you get 3,628,800 permutations.
# This kind of algorithm can become unusable beyond n = 10–11 in practice.

# 🚨 In interviews:
# If you write an O(n!) solution, you must mention it and explain:
# "This is a brute-force approach that generates all permutations — O(n!). We’d need to optimize this for larger inputs."
