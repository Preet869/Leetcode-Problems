# Learning Big O Notation 

# O(1) Constant Time 
# The operations takes the same amount of time regardless of the input size.
# Data Structures:
     # * Hash maps give you constant time access to values. stores key-value pairs.
# 🧠 When Your Brain Should Think "Hash Map!" If a problem requires O(1) time for lookups, inserts, or updates.
# Keywords to look out for:
    #"Find in constant time"
    #"Check if exists"
    #"Count frequency"
    #"Avoid duplicates"
    #"Get index/value quickly"
    #"Map one thing to another"
    #"Return fast even with big input"

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

